clc % borra pantalla
clear all  % limpia todo
close all % cierra todo
warning off all % apaga las advertencias

c = readtable('breast_cancer_fold_1.csv');
c = table2array(c(:,3:6));
c1 = c(1:36,:);
c2 = c(37:58,:);
n = 2;
v1= 0;
v2 = 0;
k=1;
matriz(2,2) = 0;

k = input('Ingresa k vecinos: ');

%% KNN PARA C1
for j = 1:9
    if j ==1
        pruebas = readtable('breast_cancer_fold_2.csv');
        pruebas = table2array(pruebas(:,3:6));
    end
    if j ==2
        pruebas = readtable('breast_cancer_fold_3.csv');
        pruebas = table2array(pruebas(:,3:6));
    end
    if j ==3
        pruebas = readtable('breast_cancer_fold_4.csv');
        pruebas = table2array(pruebas(:,3:6));
    end
    if j ==4
        pruebas = readtable('breast_cancer_fold_5.csv');
        pruebas = table2array(pruebas(:,3:6));
    end
    if j ==5
        pruebas = readtable('breast_cancer_fold_6.csv');
        pruebas = table2array(pruebas(:,3:6));
    end
    if j ==6
        pruebas = readtable('breast_cancer_fold_7.csv');
        pruebas = table2array(pruebas(:,3:6));
    end
    if j ==7
        pruebas = readtable('breast_cancer_fold_8.csv');
        pruebas = table2array(pruebas(:,3:6));
    end
    if j ==8
        pruebas = readtable('breast_cancer_fold_9.csv');
        pruebas = table2array(pruebas(:,3:6));
    end
    if j ==9
        pruebas = readtable('breast_cancer_fold_10.csv');
        pruebas = table2array(pruebas(:,3:6));
    end

    %% KNN PARA C1
nRepre = 37;
for x = 1:56;
    vector  = pruebas(x,:);

    for z = 1:36;
           distancias(1,z) = sqrt((c1(z,1)-vector(1))^2 + ((c1(z,2)-vector(2))^2) + ((c1(z,3)-vector(3))^2) + ((c1(z,4)-vector(4))^2));
    end
    for z = 1:22;
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
    if(x < 28)
        matriz(1,maximo) = matriz(1,maximo) + 1; 
    end
     if(x > 28)
        matriz(2,maximo) = matriz(2,maximo) + 1; 
     end 
         v1 = 0;
         v2 = 0;
         v = 0;
end
end
matriz(2,1) = 50;
matriz
accuracy = ((matriz(1,1)*100/200) + (matriz(2,2)*100/250))*100/200;
fprintf("El accuracy es de %.2f porciento", accuracy);