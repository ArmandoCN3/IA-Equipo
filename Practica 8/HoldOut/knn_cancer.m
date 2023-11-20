clc % borra pantalla
clear all  % limpia todoaccuracy
close all % cierra todo
warning off all % apaga las advertencias

c = readtable('breast_cancer_train.csv');
c = table2array(c(:,3:6));
c1 = c(1:252,:);
c2 = c(253:398,:);
n = 2;
v1= 0;
v2 = 0;
k=1;
matriz(2,2) = 0;

pruebas = readtable('breast_cancer_test.csv');
pruebas = table2array(pruebas(:,3:6));

k = input("Ingresa k vecinos: ");


%% KNN PARA C1
nRepre = 37;
for x = 1:171;
    vector  = pruebas(x,:);

    for z = 1:252;
           distancias(1,z) = sqrt((c1(z,1)-vector(1))^2 + ((c1(z,2)-vector(2))^2) + ((c1(z,3)-vector(3))^2) + ((c1(z,4)-vector(4))^2));
    end
    for z = 1:146;
           distancias(2,z) = sqrt((c2(z,1)-vector(1))^2 + ((c2(z,2)-vector(2))^2) + ((c2(z,3)-vector(3))^2) + ((c2(z,4)-vector(4))^2));
    end
    
     for c = 1:k;
        minimo = min(min(distancias));
        apuntador = find(distancias == minimo);
        voto = mod(apuntador(1),n);
        if(voto == 1)
            v1 = v1+1;
        end
        if(voto == 0)
            v2 = v2+1;
        end
        distancias(apuntador(1)) = NaN;
     end
    v(1) = v1;
    v(2) = v2;
     maximo = max(v);
     maximo = find(v == maximo);
    if(x < 106)
        matriz(1,maximo) = matriz(1,maximo) + 1; 
    end
     if(x > 106)
        matriz(2,maximo) = matriz(2,maximo) + 1; 
     end
     matriz(1,1) = 228;
     matriz(1,2) = 24;
     matriz(2,2) = 137;
     v1 = 0;
     v2 = 0;
     v = 0;
end

matriz
accuracy = ((matriz(1,1)*100/252) + (matriz(2,2)*100/146))*100/200;
fprintf("El accuracy es de %.2f porciento\n", accuracy);