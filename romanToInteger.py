'''
La funcion compara cada elemento de la cadena y toma su valor equivalente en 
entero decimal, para asi realizar una suma y nos de su equivalencia.
'''
class Solution:
    def romanToInt(self, s: str) -> int:
# se crea un diccionario con la equivalencia de los numeros en decimal
        numequiv={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
# de crea un arreglo donde se guarda los nuevos valores en decimal
        nums=[]
        numero=s
# se genera una lista con las equivalencias y posicion de los caracteres
# del numero romano
        for i in range(len(numero)):
            nums.append(numequiv[numero[i]])
# Se recorre los elementos de la nueva lista
        for i in range(len(nums)):
# Se verifica que se llego al ultimo caracter del numero romano, no hace nada
            if i==len(nums)-1:
                pass
# se compara si el elemento actual es menor al elemento siguiente
            elif nums[i]<nums[i+1]:
# Se multiplica por -1 el elemento actual
                nums[i]*=-1
# se regresa la suma del arreglo que es el numero ya convertido
        return sum(nums)