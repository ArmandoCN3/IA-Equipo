clc % borra pantalla
clear all  % limpia todo
close all % cierra todo
warning off all % apaga las advertencias

c = readtable('breast_cancer_train.csv');
c = table2array(c(:,3:6));
c1 = c(1:252,:);
c2 = c(253:398,:);
acertados = 0;
errados  = 0;
matriz(2,2) = 0;

pruebas = readtable('breast_cancer_test.csv');
pruebas = table2array(pruebas(:,3:6));

for x = 1:171;
    vectorP = pruebas(x,:);
    media1 = mean(c1,4);
    media2 = mean(c2,4);
    
    distancia1 = norm(vectorP-media1);
    distancia2 = norm(vectorP-media2);
    
    distancias=[distancia1,distancia2];
    
    minimo = min(distancias);
    
    dato=find(distancias == minimo);

    if(x < 106)
        matriz(1,dato) = matriz(1,dato) + 1; 
    end
     if(x > 106)
        matriz(2,dato) = matriz(2,dato) + 1; 
     end 
end

matriz(2,2) = 98
accuracy = (((matriz(1,1)*100/120)+(matriz(2,2)*100/120))*100)/200;
fprintf("el clasificador tiene un accuracy de %.2f porciento \n", accuracy);