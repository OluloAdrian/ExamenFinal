from django.shortcuts import render
from django.http import HttpResponse

def hello(request,*cadena,**cadenaID):
    return render(request,"index.html")
def libro(request,*cadena,**cadenaID):
    return render(request,"libros.html",{'libros':libros,'chequeo_libros':chequeo_libros,})
def acerca(request,*cadena,**cadenaID):
    return render(request,"acerca.html")
def admisión(request,*cadena,**cadenaID):
    return render(request,"admision.html")
# Create your views here.

#Lista de libros (estructura repetitiva for)
libros = ["Crimen y Castigo (libro1)", "Bodas de Sangre (libro2)", "El Caballero Carmelo (libro3)","Tradiciones peruanas (libro4)","La ciudad y los perros (libro5)"]
for i in libros:
    print(i)


#Disponibilidad de libros
libros_stock = ["disponible", "no disponible", "no disponible", "disponible", "no disponible","disponible"]

chequeo_libros = []
compare_status = "encendido"


i = 0
while i < len(libros_stock):

    print(f"Libro {i+1} está {libros_stock[i]}")
    chequeo_libros.append(f"Libro {i+1} está {libros_stock[i]}")

    if libros_stock[i] == len(libros_stock):
        break 
    
    i += 1 

