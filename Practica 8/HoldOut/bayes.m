clc % limpia pantalla
clear all % limpia todo
close all %cierra todo
warning off all  % apaga los warnings

c = readtable('iris_train.csv');
c = table2array(c(:,2:5));
c1 = c(1:37,:);
c2 = c(37:74,:);
c3 = c(74:105,:);
matriz(3,3) = 0;
pruebas = readtable('iris_test.csv');
pruebas = table2array(pruebas);
probabilidads = 0;
prob_n = [];
n = 3;

media1 = mean(c1);
media2 = mean(c2);
media3 = mean(c3);

for x = 1:45
    vector  = pruebas(x,2:5);
      
      dato1_tot_c1 = c1 - media1;
      dato2_tot_c1=dato1_tot_c1';
      varianza1=(1/5)*dato1_tot_c1*dato2_tot_c1;

      dato1_tot_c2 = c2 - media2;
      dato2_tot_c2=dato1_tot_c2';
      varianza2=(1/5)*dato1_tot_c2*dato2_tot_c2;

      dato1_tot_c3 = c3 - media3;
      dato2_tot_c3=dato1_tot_c3';
      varianza3=(1/5)*dato1_tot_c3*dato2_tot_c3;
    
      %%CALCULA PROBABILIDADES
      dato1_c1=vector(:,:)-media1(:,:);
      dato1_c1=dato1_c1';
      dato2_c1=dato1_c1';
      inv_varianza1=inv(varianza1);
      a_c1=exp(-0.5*dato1_c1*dato2_c1);      
      b_c1=(1/(2*pi)*det(varianza1)^(-0.5));
      probabilidads(1)=b_c1*a_c1;

      dato1_c2=vector(:,:)-media2(:,:);
      dato1_c2=dato1_c2';
      dato2_c2=dato1_c2';
      inv_varianza2=inv(varianza2);
      a_c2=exp(-0.5*dato1_c2*inv_varianza2*dato2_c2);      
      b_c2=(1/(2*pi)*det(varianza2)^(-0.5));
      probabilidads(2)=b_c2*a_c2;

      dato1_c3=vector(:,:)-media3(:,:);
      dato1_c3=dato1_c3';
      dato2_c3=dato1_c3';
      inv_varianza3=inv(varianza3);
      a_c3=exp(-0.5*dato1_c3*inv_varianza3*dato2_c3);      
      b_c3=(1/(2*pi)*det(varianza3)^(-0.5));
      probabilidads(3)=b_c3*a_c3;
    
    for c = 1:n;
        %%NORMALIZANDO
      prob_n(c) = (probabilidads(c)/(sum(probabilidads)))*100;
    end
    
    maximo=max(max(prob_n))
    valor=find(prob_n==maximo)
    
    matriz(pruebas(x),maximo) = matriz(pruebas(x),maximo) + 1;
end

matriz
accuracy = ((matriz(1,1)*100/13) + (matriz(2,2)*100/14) + (matriz(3,3)*100/19))*100/300;
fprintf("El accuracy es de %.2f porciento\n", accuracy);