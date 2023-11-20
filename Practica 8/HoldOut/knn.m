clc % borra pantalla
clear all  % limpia todo
close all % cierra todo
warning off all % apaga las advertencias

c = readtable('iris_train.csv');
c = table2array(c(:,2:5));
c1 = c(1:37,:);
c2 = c(37:74,:);
c3 = c(74:105,:);
n = 3;
v1= 0;
v2 = 0;
v3 = 0;
k=0;
matriz(3,3) = 0;

pruebas = readtable('iris_test.csv');
pruebas = table2array(pruebas);

k = input("Ingresa k vecinos: ");


%% KNN PARA C1
nRepre = 37;
for x = 1:45;
    vector  = pruebas(x,2:5);

    for z = 1:37;
           distancias(1,z) = sqrt((c1(z,1)-vector(1))^2 + ((c1(z,2)-vector(2))^2) + ((c1(z,3)-vector(3))^2) + ((c1(z,4)-vector(4))^2));
    end
    for z = 1:38;
           distancias(2,z) = sqrt((c2(z,1)-vector(1))^2 + ((c2(z,2)-vector(2))^2) + ((c2(z,3)-vector(3))^2) + ((c2(z,4)-vector(4))^2));
    end
    for z = 1:32;
           distancias(3,z) = sqrt((c3(z,1)-vector(1))^2 + ((c3(z,2)-vector(2))^2) + ((c3(z,3)-vector(3))^2) + ((c3(z,4)-vector(4))^2));
    end
    
     for c = 1:k;
        minimo = min(min(distancias));
        apuntador = find(distancias == minimo);
        voto = mod(apuntador(1),n);
        if(voto == 1)
            v1 = v1+1;
        end
        if(voto == 2)
            v2 = v2+1;
        end
        if(voto == 0)
            v3 = v3+1;
        end
        distancias(apuntador(1)) = NaN;
     end
    v(1) = v1;
    v(2) = v2;
    v(3) = v3;
     maximo = max(v);
     maximo = find(v == maximo);

     matriz(pruebas(x),maximo) = matriz(pruebas(x),maximo) + 1; 
     v1 = 0;
     v2 = 0;
     v3 = 0;
     v = 0;
end

matriz
accuracy = ((matriz(1,1)*100/13) + (matriz(2,2)*100/14) + (matriz(3,3)*100/19))*100/300;
fprintf("El accuracy es de %.2f porciento", accuracy);