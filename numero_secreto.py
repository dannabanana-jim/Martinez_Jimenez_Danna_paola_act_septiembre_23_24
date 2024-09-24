print (" ")
print("Danna Paola Martinez Jimenez")
print (" ")
numero_secreto = 42  # Número que el usuario tiene que adivinar
#Solicita un numero al usuario
adivinanza = int(input("Adivina el número que he elegido entre 1 y 100: "))

if adivinanza < numero_secreto:
    print("Demasiado bajo. Intenta de nuevo.")
elif adivinanza > numero_secreto:
    print("Demasiado alto. Intenta de nuevo.")
else:
    print("¡Felicidades! Has adivinado el número.")

print (" ")
