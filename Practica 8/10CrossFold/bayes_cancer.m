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

for x = 1:56;
    vectorP = pruebas(x,:);
    media1 = mean(c1,4);
    media2 = mean(c2,4);
    
    distancia1 = norm(vectorP-media1);
    distancia2 = norm(vectorP-media2);
    
    distancias=[distancia1,distancia2];
    
    minimo = min(distancias);
    
    dato=find(distancias == minimo);

    if(x < 28)
        matriz(1,dato) = matriz(1,dato) + 1; 
    end
     if(x > 28)
        matriz(2,dato) = matriz(2,dato) + 1; 
     end 
end
end

matriz(2,1) = 53
accuracy = (((matriz(1,1)*100/250)+(matriz(2,2)*100/200))*100)/200;
fprintf("el clasificador tiene un accuracy de %.2f porciento \n", accuracy);