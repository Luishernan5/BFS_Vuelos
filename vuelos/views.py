from django.shortcuts import render
from .bfs.vuelos_bfs import buscar_solucion_BFS
def index(request):
    resultado = None

    conexiones = {
        'Jiloyork': {'Celaya','Queretaro'},
        'Sonora': {'Zacatecas', 'Sinaloa'},
        'Guanajuato': {'Aguascalientes'},
        'Oaxaca': {'Queretaro'},
        'Sinaloa': {'Celaya', 'Sonora', 'Jiloyork'},
        'Celaya': {'Jiloyork', 'Sinaloa'},
        'Zacatecas': {'Sonora', 'Monterrey', 'Queretaro'},
        'Monterrey': {'Zacatecas', 'Sinaloa'},
        'Tamaulipas': {'Queretaro'},
        'Queretaro': {'Tamaulipas', 'Zacatecas', 'Sinaloa','Jiloyork', 'Oaxaca'}
    }

    ciudades = list(conexiones.keys())

    if request.method == "POST":
        inicio = request.POST.get("inicio")
        destino = request.POST.get("destino")

        nodo_solucion = buscar_solucion_BFS(conexiones, inicio, destino)

        if nodo_solucion:
            camino = []
            nodo = nodo_solucion
            while nodo.get_padre() != None:
                camino.append(nodo.get_datos())
                nodo = nodo.get_padre()
            camino.append(inicio)
            camino.reverse()

            resultado = camino

    return render(request, "vuelos/index.html", {
        "resultado": resultado,
        "ciudades": ciudades
    })