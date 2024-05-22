#Creación de un bucle for
lista_numeros=[1,2,3,4,5]
for num in lista_numeros:
    print(num)
#Función que suma 3 números
def sumar(a,b,c):
    suma= a+b+c
    print(suma)
sumar(1,2,3)
#Función lambda que suma 3 números
sumar_tres_numeros= lambda a,b,c,:a+b+c
resultado = sumar_tres_numeros(1,2,3)
print(resultado)
#Comprobación de nombre en la lista
nombre= "Enrique"
lista_nombre= ["Jessica","Paul","George","Henry","Adán"]
def comprobar_nombre(n):
    lista_contiene= None
    for item in lista_nombre:
        if n == item:
            lista_contiene= True
            break
    if lista_contiene:
        print("El nombre está en la lista!")     
    else:
        print ("El nombre no está en la lista")

comprobar_nombre(nombre)
