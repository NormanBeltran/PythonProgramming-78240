nombre, edad = "Juan", 28

mensaje = "Bienvenido {1}, tu edad es {0} años"
print(mensaje.format(edad, nombre))

print(f"Bienvenido {nombre}, tu edad es {edad} años")

mensaje2 = "Bienvenido %s, tu edad es %d años"%(nombre, edad)

print(mensaje2)

saldo = 12345.987654
print(f"El saldo es {saldo:.2f}")
print(f"El saldo es {saldo:>8.2f}")
print(f"El saldo es {saldo:>10.2f}")
print(f"El saldo es {saldo:<8.3f}")

