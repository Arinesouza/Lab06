class Sorter:
    def __init__(self):
        pass

    def particiona(self, valores, inicio, fim):
       pivo = valores[inicio]
       i = inicio
       for j in range(inicio+1,fim+1):
           if valores[j] < pivo:
              i +=1
              aux = valores[i]
              valores[i] = valores[j]
              valores[j] = aux
              

       aux = valores[i]
       valores[i] = valores[inicio]
       valores[inicio] = aux
       
       return valores, i
               
       
              
    def quick_sort(self, valores, inicio, fim):
        if inicio < fim:
            pivo = valores[inicio]
            i = inicio
            for j in range(inicio + 1, fim + 1):
                if valores[j] < pivo:
                    i += 1
                    aux = valores[i]
                    valores[i] = valores[j]
                    valores[j] = aux
            aux = valores[i]
            valores[i] = pivo
            valores[inicio] = aux
            self.quick_sort(valores, inicio, i - 1)
            self.quick_sort(valores, i + 1, fim)
        return valores
    
    def merge(self, esquerda, direita):
       lista = esquerda + direita
       n = len(lista)
       for i in range(n):
          for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
       return lista
    
           

    def merge_sort(self, valores):
        n = len(valores)
        if n <= 1:
            return valores
        meio = n // 2
        metade_esquerda = valores[:meio]
        metade_direita = valores[meio:]
        metade_esquerda = self.merge_sort(metade_esquerda)
        metade_direita = self.merge_sort(metade_direita)

        lista_ordenada = self.merge(metade_esquerda, metade_direita)
        return lista_ordenada

 





