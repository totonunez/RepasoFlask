from faker import Faker
from time import time 
from random import choice, random, randint
import csv



results = []

with open('ListaDeDatos.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row['Ciudades'])
    

santiago = []
concepcion = []
valparaiso = []
serena = []
antofagasta = []
temuco = []
rancagua = []
iquique = []
talca = []
arica = []
puertomontt = []
chillan = []
angeles = []
calama = []
copiapo = []
osorno = []
quillota = []
valdivia = []
puntaarenas = []
sanantonio = []
curico = []
ovalle = []
linares = []
andes = []
melipilla = []
sanfelipe = []


with open('Ciudades.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        santiago.append(row['Gran Santiago'])
        concepcion.append(row['Gran Concepcion'])
        valparaiso.append(row['Gran Valparaiso'])
        serena.append(row['Gran La Serena'])
        antofagasta.append(row['Antofagasta'])
        temuco.append(row['Gran Temuco'])
        rancagua.append(row['Gran Rancagua'])
        iquique.append(row['Gran Iquique'])
        talca.append(row['Talca'])
        arica.append(row['Arica'])
        puertomontt.append(row['Gran Puerto Montt'])
        chillan.append(row['Gran Chillan'])
        angeles.append(row['Los Angeles'])
        calama.append(row['Calama'])
        copiapo.append(row['Copiapo'])
        osorno.append(row['Osorno'])
        quillota.append(row['Gran Quillota'])
        valdivia.append(row['Valdivia'])
        puntaarenas.append(row['Punta Arenas'])
        sanantonio.append(row['Gran San Antonio'])
        curico.append(row['Curico'])
        ovalle.append(row['Ovalle'])
        linares.append(row['Linares'])
        andes.append(row['Los Andes'])
        melipilla.append(row['Melipilla'])
        sanfelipe.append(row['San Felipe'])


calles = {}
calles['Gran Santiago'] = santiago
calles['Gran Concepcion'] = concepcion
calles['Gran Valparaiso'] = valparaiso
calles['Gran La Serena'] = serena
calles['Antofagasta'] = antofagasta
calles['Gran Temuco'] = temuco
calles['Gran Rancagua'] = rancagua
calles['Gran Iquique'] = iquique
calles['Talca'] = talca
calles['Arica'] = arica
calles['Gran Puerto Montt'] = puertomontt
calles['Gran Chillan'] = chillan
calles['Los Angeles'] = angeles
calles['Calama'] = calama
calles['Copiapo'] = copiapo
calles['Osorno'] = osorno
calles['Gran Quillota'] = quillota
calles['Valdivia'] = valdivia
calles['Punta Arenas'] = puntaarenas
calles['Gran San Antonio'] = sanantonio
calles['Curico'] = curico
calles['Ovalle'] = ovalle
calles['Linares'] = linares
calles['Los Andes'] = andes
calles['Melipilla'] = melipilla
calles['San Felipe'] = sanfelipe 



fake = Faker()
tiempo = time()
print("CHOQUES")
print("insert into choques (id_evento, ciudad,calle, numeracion, fecha, hora) values")

for x in range(0,10):
    ciudad = choice(results)
    print("({},'{}','{}','{}','{}','{}'),".format(x,ciudad,choice(calles[ciudad]), randint(20,3000),fake.date(),fake.time() ))

print(")")

final = time()- tiempo
print("Tiempo total en crearse todos los datos es ", final)


