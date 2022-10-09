'''
La funcion compara cada elemento de la cadena y obtiene el valor del diccionario,
suma o resta el valor dependiendo de la posicion y la cadena la invierte primero 
para no comparar el ultimo elemento. 
'''
class Solution:
    def romanToInt(self, s: str) -> int:
#se crea el diccionario con su equivalente en decimal. 
        sym ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
# Se inicializa la suma en cero       
        result = 0
# Se inicia una variable pivote, con valor cero.
        prev = 0
# Se recorre cada uno de los elementos del string pero se invierte el orden       
        for c in reversed(s):
# se compara si el valor esta antes o despues y se suma o resta.
            if sym[c] >= prev:
                result += sym[c]
            else:
                result -= sym[c]
# el pivote se actualiza para poder realizar las comparaciones. 
            prev = sym[c]
            
        return result