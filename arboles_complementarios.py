import sys

# Aumentar el límite de recursión para árboles profundos (Sugerencia IA)
sys.setrecursionlimit(2000)


# CLASE NODO E IMPRESIÓN

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def imprimir_arbol(nodo, prefijo="", es_ultimo=True):
    """
    Visualizar árbol en consola (Ayuda de IA)
    """
    if not nodo:
        print(prefijo + "└── (Vacío)")
        return

    print(prefijo + ("└── " if es_ultimo else "├── ") + str(nodo.valor))

    hijos = [hijo for hijo in [nodo.izquierdo, nodo.derecho] if hijo]
    for i, hijo in enumerate(hijos):
        es_ultimo_hijo = (i == len(hijos) - 1)
        imprimir_arbol(
            hijo,
            prefijo + ("    " if es_ultimo else "│   "),
            es_ultimo_hijo
        )


# FASE OPTIMIZACIÓN (Elimina hojas que estan en un árbol pero no en el otro, recursivamente)


def obtener_todos_valores(nodo):
    """
    Recorre el árbol y devuelve un set() con todos los valoresde nodos
    """
    if nodo is None:
        return set()

    return {nodo.valor} | \
           obtener_todos_valores(nodo.izquierdo) | \
           obtener_todos_valores(nodo.derecho)

def podar_hojas_inviables(nodo, valores_del_otro_arbol):

    if nodo is None:
        return None

    # Limpiar subárboles primero (post-orden)
    nodo.izquierdo = podar_hojas_inviables(nodo.izquierdo, valores_del_otro_arbol)
    nodo.derecho = podar_hojas_inviables(nodo.derecho, valores_del_otro_arbol)

    # Revisar este nodo DESPUÉS de limpiar a sus hijos
    es_hoja_ahora = (nodo.izquierdo is None and nodo.derecho is None)

    if es_hoja_ahora:
        # sirve?
        if nodo.valor not in valores_del_otro_arbol:
            # No sirve entonces se poda este nodo devolviendo None al padre
            return None

    # Si no es una hoja o si es viable entonces se conserva
    return nodo

def pre_proceso_iterativo(raiz_A, raiz_B):
    """
    Aplica la poda de optimización iterativamente hasta que
    los árboles se estabilicen (no haya más podas).
    """

    while True:
        # 1. Obtener los conjuntos de valores ACTUALES
        valores_A = obtener_todos_valores(raiz_A)
        valores_B = obtener_todos_valores(raiz_B)

        # Algún árbol vacio?
        if not valores_A or not valores_B:
            break

        # Podar A respecto B y visceversa
        raiz_A = podar_hojas_inviables(raiz_A, valores_B)
        raiz_B = podar_hojas_inviables(raiz_B, valores_A)

        # Si los conjuntos de valores son iguales a como empezaron, no se podó nada y hemos terminado.
        nuevos_valores_A = obtener_todos_valores(raiz_A)
        nuevos_valores_B = obtener_todos_valores(raiz_B)

        if valores_A == nuevos_valores_A and valores_B == nuevos_valores_B:
            break

    return raiz_A, raiz_B


# FASE GENERAR Y COMPARAR


def generar_secuencias(nodo):
    """
    Genera todas las secuencias de hojas posibles desde este nodo. Devuelve un set de tuplas
    """

    # Nodo Nulo?
    if nodo is None:
        return { tuple() }

    # Nodo Hoja. Una hoja puede ser conservada o podada
    if nodo.izquierdo is None and nodo.derecho is None:
        return { (nodo.valor,), tuple() }

    # Nodo Interno

    resultados = set()

    # Opción: Podar este nodo

    resultados.add( (nodo.valor,) )

    # Opción: Conservar este nodo
    set_izq = generar_secuencias(nodo.izquierdo)
    set_der = generar_secuencias(nodo.derecho)

    # Unir todas las secuencias de hijos
    for seq_i in set_izq:
        for seq_d in set_der:
            resultados.add( seq_i + seq_d )

    return resultados

def encontrar_mejor_secuencia(raiz_A, raiz_B):
    """
    Comparar
    """
    set_A = generar_secuencias(raiz_A)

    set_B = generar_secuencias(raiz_B)

    interseccion = set_A.intersection(set_B)

    if not interseccion:
        print("No se encontraron secuencias complementarias.")
        return []

    mejor_secuencia = max(interseccion, key=len)

    return list(mejor_secuencia)

# FUNCIÓN PRINCIPAL Y EJECUCIÓN

def encontrar_mejor_secuencia_completo(raiz_A, raiz_B):

    print("--- Fase: Optimizando Árboles ---")
    print("\nÁrbol A (Original):")
    imprimir_arbol(raiz_A)
    print("\nÁrbol B (Original):")
    imprimir_arbol(raiz_B)

    raiz_A_opt, raiz_B_opt = pre_proceso_iterativo(raiz_A, raiz_B)

    print("\n-------------------------------------------")
    print("Optimización completada.")
    print("Árbol A (Optimizado):")
    imprimir_arbol(raiz_A_opt)
    print("\nÁrbol B (Optimizado):")
    imprimir_arbol(raiz_B_opt)

    print("\n--- Fase: Buscando Secuencia ---")
    mejor_secuencia = encontrar_mejor_secuencia(raiz_A_opt, raiz_B_opt)

    return mejor_secuencia

# Ejemplo de Ejecución
if __name__ == "__main__":

    # Ejemplo 1
    print("\n\n--- Ejemplo 1 ---")
    # Árbol A
    A = Nodo(5)
    A.izquierdo = Nodo(2)
    A.derecho = Nodo(7)
    A.izquierdo.izquierdo = Nodo(1)
    A.izquierdo.derecho = Nodo(3)

    # Árbol B
    B = Nodo(6)
    B.izquierdo = Nodo(2)
    B.derecho = Nodo(8)
    B.izquierdo.izquierdo = Nodo(1)
    B.izquierdo.derecho = Nodo(3)

    resultado = encontrar_mejor_secuencia_completo(A, B)

    print("\n===========================================")
    print(f" Resultado Final: La mejor secuencia complementaria es:")
    print(resultado)
    print(f"Número de hojas: {len(resultado)}")
    print("===========================================")

    # Ejemplo 2
    print("\n\n--- Ejemplo 2 ---")

    # Árbol T1
    T1 = Nodo(10)
    T1.izquierdo = Nodo(5)
    T1.derecho = Nodo(3)
    T1.izquierdo.izquierdo = Nodo(9)
    T1.izquierdo.derecho = Nodo(2)
    T1.izquierdo.derecho.izquierdo = Nodo(8)
    T1.izquierdo.derecho.derecho = Nodo(6)
    T1.derecho.izquierdo = Nodo(1)
    T1.derecho.derecho = Nodo(0)
    T1.derecho.derecho.derecho = Nodo(4)

    # Árbol T2
    T2 = Nodo(4)
    T2.izquierdo = Nodo(1)
    T2.derecho = Nodo(3)
    T2.izquierdo.izquierdo = Nodo(8)
    T2.izquierdo.derecho = Nodo(11)
    T2.izquierdo.derecho.izquierdo = Nodo(7)
    T2.izquierdo.derecho.derecho = Nodo(6)
    T2.izquierdo.derecho.derecho.izquierdo = Nodo(2)

    resultado_2 = encontrar_mejor_secuencia_completo(T1, T2)

    print("\n===========================================")
    print(f" Resultado Final (Ejemplo 2):")
    print(resultado_2)
    print(f"Número de hojas: {len(resultado_2)}")
    print("===========================================")

    # Ejemplo 3
    print("\n\n--- Ejemplo 3 ---")

    A_force = Nodo(3)
    A_force.izquierdo = Nodo(2)
    A_force.izquierdo.derecho = Nodo(4)
    A_force.izquierdo.derecho.derecho = Nodo(7)
    A_force.derecho = Nodo(1)
    A_force.derecho.izquierdo = Nodo(8)


    B_force = Nodo(10)
    B_force.izquierdo = Nodo(5)
    B_force.izquierdo.izquierdo = Nodo(11)
    B_force.izquierdo.derecho = Nodo(6)
    B_force.derecho = Nodo(3)
    B_force.derecho.derecho = Nodo(9)

    resultado_3 = encontrar_mejor_secuencia_completo(A_force, B_force)

    print("\n===========================================")
    print(f" Resultado Final (Ejemplo 3):")
    print(resultado_3)
    print(f"Número de hojas: {len(resultado_3)}")
    print("===========================================")
