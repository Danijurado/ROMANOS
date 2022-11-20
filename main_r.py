'''
1-Crear una funcion que pase de entero > 0 y < 4000 a romano

2-Cualquier otra entrada debe dar error

Casos de prueba

a) 1994 -> MCMXCIV
b) 4000->RomanNumberError("el valor debe ser menor de 4000")
c)"unacadena" -> RomanNumberErro("debe ser un entero")
d)0-> RomanNumberError("el valor debe ser mayor a cero")
e)-3 ->RomanNumberError("el valor debe ser mayor de cero")
f)4.5 -> RomanNumberError("Debe ser un entero")
'''

class RomanNumberError( Exception ):
    pass

dic_entero_a_romano = {
    1:'I',2:'II',3:'III',
    4:'IV',5:'V',6:'VI',
    7:'VII',8:'VIII',9:'IX',
    10:'X',20:'XX',30:'XXX',
    40:'XL',50:'L',60:'LX',
    70:'LXX',80:'LXXX',90:'XC',
    100:'C',200:'CC',300:'CCC',
    400:'CD',500:'D',600:'DC',
    700:'DCC',800:'DCCC',900:'CM', 
    1000:'M',2000:'MM',3000:'MMM'
    }

dic_romano_a_entero = {
    'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
}
def entero_a_romano(num:int)->str:
   

    num = "{:0>4d}".format(num)
    lista = list(num) 
    longitud = len(lista)
    numero_romano = ""
    
    for i in range(longitud):
        longitud -= 1
        lista[i] +="0"*longitud
        
        numero_romano += dic_entero_a_romano.get(int(lista[i]), '' )

    
    return numero_romano
    
print("funcion en accion",entero_a_romano(3))


def romano_a_entero(rom:str) -> int:
    lista = list(rom)
    
    valor_entero = 0
    
    for i in rom:
        ''''
        if i != len(lista)-1:
            
            if dic_romano_a_entero.get(lista [i]) < dic_romano_a_entero.get(lista[i+1]):
                valor_entero += dic_romano_a_entero.get(lista [i+1]) - dic_romano_a_entero.get(lista[i])
            else:
                valor_entero += dic_romano_a_entero.get(lista[i])
        '''
        valor_entero +=dic_romano_a_entero.get(i)       
    return valor_entero
        
print('romano a entero:', romano_a_entero('XI'))

 