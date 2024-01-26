def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Encontra o índice do menor elemento na parte não ordenada
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Troca os elementos usando uma variável auxiliar
        aux = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = aux

# Exemplo de uso:
arr = [64, 25, 12, 22, 11]
print("Array não ordenado:", arr)
selection_sort(arr)
print("Array ordenado:", arr)