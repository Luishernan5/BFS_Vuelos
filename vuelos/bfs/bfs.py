from .arbol import Nodo

def buscar_solucion_BFS(estado_inicial, solucion):
    nodos_visitados = []
    nodos_frontera = []

    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)

    while len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            return nodo
        else:
            dato_nodo = nodo.get_datos()

            # Operador izquierdo
            hijo_izq = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]])

            # Operador central
            hijo_cen = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]])

            # Operador derecho
            hijo_der = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]])

            for hijo in [hijo_izq, hijo_cen, hijo_der]:
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)

            nodo.set_hijos([hijo_izq, hijo_cen, hijo_der])

    return None