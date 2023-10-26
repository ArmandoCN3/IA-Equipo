import random
import csv

values = []

def create_csv(name, data):

    with open(name, mode="w", newline="") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
    print(f"\nSe creo el archivo {name}")

def hold_out_validation(data, test_size):
    random.seed(50) # Semilla aleatoria para garantizar reproducibilidad

    random.shuffle(data) # Se mezcla la lista de los datos

    # Se divide el conjunto de datos en dos partes
    split_index = int(len(data) * (1 - test_size))
    training_data = data[:split_index]
    test_data = data[split_index:]

    return training_data, test_data

if __name__ == "__main__":
    
    file = input("\nIngrese el nombre del archivo: ")
    porcentaje_test = int(input ("\nIngrese el porcentaje de validacion para test: "))

    with open(file + '.csv', "r") as f:
        reader = csv.reader(f, delimiter=",") # Crea un arreglo para almacenar los valores
        
        for row in reader: 
            values.append( (row) ) #La lista values se le agrega un conjunto de tuplas con las columnas del archivo csv

    training_data, test_data = hold_out_validation(values, porcentaje_test/100) #Tomamos el (100 - porcentaje) para el training data y (porcentaje) para el test data
    
    create_csv(file + '_train.csv', training_data)
    create_csv(file + '_test.csv', test_data)