clc % borra pantalla
clear all  % limpia todo
close all % cierra todo
warning off all % apaga las advertencias

c = readtable('iris_fold_1.csv');
c = table2array(c(:,2:5));
c1 = c(1:5,:);
c2 = c(6:10,:);
c3 = c(11:15,:);
n = 3;
v1= 0;
v2 = 0;
v3 = 0;
k=1;
matriz(3,3) = 0;

%% KNN PARA C1
for j = 1:9
    if j ==1
        pruebas = readtable('iris_fold_2.csv');
        pruebas = table2array(pruebas);
    end
    if j ==2
        pruebas = readtable('iris_fold_3.csv');
        pruebas = table2array(pruebas);
    end
    if j ==3
        pruebas = readtable('iris_fold_4.csv');
        pruebas = table2array(pruebas);
    end
    if j ==4
        pruebas = readtable('iris_fold_5.csv');
        pruebas = table2array(pruebas);
    end
    if j ==5
        pruebas = readtable('iris_fold_6.csv');
        pruebas = table2array(pruebas);
    end
    if j ==6
        pruebas = readtable('iris_fold_7.csv');
        pruebas = table2array(pruebas);
    end
    if j ==7
        pruebas = readtable('iris_fold_8.csv');
        pruebas = table2array(pruebas);
    end
    if j ==8
        pruebas = readtable('iris_fold_9.csv');
        pruebas = table2array(pruebas);
    end
    if j ==9
        pruebas = readtable('iris_fold_10.csv');
        pruebas = table2array(pruebas);
    end

    for x = 1:15;
        vector  = pruebas(x,2:5);
    
        for z = 1:5;
               distancias(1,z) = sqrt((c1(z,1)-vector(1))^2 + ((c1(z,2)-vector(2))^2) + ((c1(z,3)-vector(3))^2) + ((c1(z,4)-vector(4))^2));
        end
        for z = 1:5;
               distancias(2,z) = sqrt((c2(z,1)-vector(1))^2 + ((c2(z,2)-vector(2))^2) + ((c2(z,3)-vector(3))^2) + ((c2(z,4)-vector(4))^2));
        end
        for z = 1:5;
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
end
matriz
accuracy = ((matriz(1,1)*100/45) + (matriz(2,2)*100/45) + (matriz(3,3)*100/45))*100/300;
fprintf("El accuracy es de %.2f porciento", accuracy);