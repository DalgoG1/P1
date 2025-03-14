def min_energia_algormar(n, j, m, pesos):
    try:
        if j == 0:
            return 0
        
        # Memoria: dp[i][k][s] = suma mínima usando primeros i jugadores, k elementos sumados, s swaps
        dp = [[[float('inf') for _ in range(m + 1)] for _ in range(j + 1)] for _ in range(n + 1)]
        
        # Casos base
        for i in range(n + 1):
            for s in range(m + 1):
                dp[i][0][s] = 0  # Sumar 0 elementos siempre suma 0
        
        for i in range(1, n + 1):
            for k in range(1, j + 1):
                for s in range(m + 1):
                    # Caso base: k > i, imposible seleccionar más elementos que los disponibles
                    if k > i:
                        dp[i][k][s] = float('inf')
                        continue
                    
                    # Caso base: k == i, seleccionar todos los primeros k elementos
                    if k == i:
                        dp[i][k][s] = sum(pesos[:k])
                        continue
                    
                    # Caso base: k < i y s == 0, sin swaps disponibles
                    if k < i and s == 0:
                        dp[i][k][s] = sum(pesos[:k])
                        continue
                    
                    # Caso recursivo 1: No incluir al jugador i
                    option1 = dp[i-1][k][s]
                    
                    # Caso recursivo 2: Incluir al jugador i, con posible intercambio
                    option2 = float('inf')
                    
                    # Si tenemos suficientes swaps para mover al jugador i a una posición válida
                    swaps_needed = i - k
                    if s >= swaps_needed:
                        option2 = dp[i-1][k-1][s-swaps_needed] + pesos[i-1]
                    else:
                        # No suficientes swaps, no podemos incluir este jugador
                        option2 = float('inf')
                    
                    dp[i][k][s] = min(option1, option2)
        
        # Encontrar el mínimo entre todos los swaps posibles
        resultado = min(dp[n][j][s] for s in range(m + 1))
        return resultado if resultado != float('inf') else 0
        
    except MemoryError:
        print("Error: Memoria insuficiente para procesar la entrada.")
        return 0
    except Exception as e:
        print(f"Error inesperado: {e}")
        return 0
    
def main():
    # Lectura de entrada
    num_casos = int(input())

    for _ in range(num_casos):
        datos = list(map(int, input().split()))
        n, j, m = datos[0], datos[1], datos[2]
        pesos = datos[3:3 + n]
        
        # Calculamos y mostramos el resultado
        resultado = min_energia_algormar(n, j, m, pesos)
        print(resultado)

if __name__ == "__main__":
    main()
    
# Pruebas
# print(min_energia_algormar(5, 2, 3, [3, 1, 4, 2, 5]))  # Salida: 3

# print(min_energia_algormar(13, 7, 20, [57,27,13,91,73,1,13,1,43,21,31,3,7]))  # Salida: 79

# print(min_energia_algormar(8, 3, 6, [57,43,31,21,13,1,7,3]))  # Salida: 65

# print(min_energia_algormar(23, 11, 19, [127,103,1,23,81,43,61,153,181,47,7,3,27,91,43,57,21,1,73,13,13,1,31]))  # Salida: 463
# # 17,2,2 [43 81 103 13 27 61 43 31 21 13 1 7 1 3 91 73 57]
# print(min_energia_algormar(17, 2, 2, [43,81,103,13,27,61,43,31,21,13,1,7,1,3,91,73,57]))  # Salida: 56