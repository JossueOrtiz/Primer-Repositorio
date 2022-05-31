#Este es mi primer programa en phyton 
#Lo primero que imprimi fue un hola mundo
print("Hello World")
nombre = input("Como te llamas: ")
print ("Hola ", nombre)
calificacion = input("Introduce tu calificacion: ")
calificacion = int(calificacion)
if calificacion <700:
    print("No pasaste por no estudiar master")    #Utilizamos el operador if para saber un rango de cosas
    print("Intentalo el siguiente año master")
elif calificacion > 1000:
    print("No es muy creible mi estimado")
elif calificacion == 700:
    print(("Pasaste de panzaso master"))
else : 
    print("Felicidades pasa por tu certificado")
#En python no existe el switch case lamentablemente 
#me quede en el minuto 1.22
