#pip install csv       pip install rich
import csv
from rich.table import Table
from rich.console import Console

campo = "petallength" #petallength / petalwidth

clases = {
    'Iris-setosa': [],
    'Iris-versicolor': [],
    'Iris-virginica': []
}

with open('train.csv', 'r') as csvfile:
    archivo = csv.DictReader(csvfile)
    
    for row in archivo:
        clase = row['class']
        valor = float(row[campo])
        clases[clase].append(valor)

umbral_set_ver = ( max(clases['Iris-setosa'] ) + min (clases['Iris-versicolor'])) / 2
umbral_ver_vir = ( max (clases['Iris-versicolor'] ) + min (clases['Iris-virginica'])) / 2

table = Table()
table.add_column(campo)
table.add_column('Clase estimada')
table.add_column('Clase real')

with open('test.csv', 'r') as csvfile:
    archivo = csv.DictReader(csvfile)
    
    for row in archivo:
        clase = row['class']
        valor = float(row[campo])

        if valor <= umbral_set_ver:
            table.add_row(f"[purple] {valor}", f"[purple] Iris-setosa", f"[purple] {clase}")

        elif valor > umbral_set_ver and valor <=umbral_ver_vir:#valor <=umbral_ver_vir:
            table.add_row(f"[green] {valor}", f"[green] Iris-versicolor", f"[green] {clase}")

        elif valor >= umbral_ver_vir:
            table.add_row(f"[red] {valor}", f"[red] Iris-virginica", f"[red] {clase}")

console = Console()
console.print(table)
print(f"\nUmbral Iris-setosa - Iris-versicolor: {umbral_set_ver}")
print(f"Umbral Iris-versicolor - Iris-virginica: {umbral_ver_vir}\n")