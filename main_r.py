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

milesima = {
    1000:'M',2000:'MM',3000:'MMM'
}

unidades={
    1:'I',2:'II',3:'III',
    4:'IV',5:'V',6:'VI',
    7:'VII',8:'VIII',9:'IX'
}

decenas={
    10:'X',20:'XX',30:'XXX',
    40:'XL',50:'L',60:'LX',
    70:'LXX',80:'LXXX',90:'XC'
}

centenas={
    100:'C',200:'CC',300:'CCC',
    400:'CD',500:'D',600:'DC',
    700:'DCC',800:'DCCC',900:'CM'  
}

#meta cumplir con esta funcion 
def entero_a_romano(num):
   
    lista = []
    num = str(num)

    if len(num)<4:
       num = "{:0>4s}".format(num)
    lista = list(num) 
    for i in range(len(lista)):
        lista[i] = lista[i]+"0"*((len(lista)-1 )-i)
    print(lista)

    numero_romano=""
    for i in range(len(lista)):
        
        if i == 0:
            if milesima.get(int(lista[i])) != None:
                numero_romano += milesima.get(int(lista[i]) )

        elif i == 1:
            if centenas.get(int(lista[i])) != None:
                numero_romano += centenas.get( int(lista[i]) ) 
        elif i == 2:
            if decenas.get(int(lista[i])) != None:
                numero_romano += decenas.get( int(lista[i]) ) 
        elif i == 3:
            if unidades.get(int(lista[i])) != None:
                numero_romano += unidades.get( int(lista[i]) )    

    return numero_romano




print("funcion en accion",entero_a_romano(2022))
 