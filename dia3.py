#ejercicio 1
usuario = {
    "nombre": "Yanet",
    "email": "yanet@ejemplo.com",
    "password": "test_clave",
    "activo": True
}
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

#ejercicio 2
usuario = {
    "nombre": "Yanet",
    "email": "yanet@ejemplo.com",
    "password": "test_clave",
    "activo": True
}
usuario["rol"] = "tester" 
usuario["activo"] = False

# lectura de claves inexistente de dos formas
# print(usuario["telefono"]) #esta linea produce un KeyError
print(usuario.get("telefono", "Desconocido")) # evita que se detenga la ejecución al devolver el texto cuando la clave no existe

#ejericio 3
usuarios = [
    {"nombre": "Yanet", "email": "yanet@ejemplo.com", "activo": True}, 
    {"nombre": "Carlos", "email": "carlos@ejemplo.com", "activo": False}, 
    {"nombre": "Marlon", "email": "marlon@ejemplo.com", "activo": True}
    ]
for usuario in usuarios:
    if usuario["activo"]:
        print(usuario["nombre"])
    
#ejercicio 4
usuarios = [
    {"nombre": "Yanet", "email": "yanet@ejemplo.com", "activo": True}, 
    {"nombre": "Carlos", "email": "carlos@ejemplo.com", "activo": False}, 
    {"nombre": "Marlon", "email": "marlon@ejemplo.com", "activo": True}
    ]
correos = []
for usuario in usuarios:
    if not usuario["activo"]:
        correos.append(usuario["email"])
if not correos:
    print("No hay usuarios inactivos")
else:
    print(correos)

# ejercicio 5

test_cases = [
    ("yanet", "clave_prueba", "Login exitoso"),
    ("marlon", "incorrect_pass", "Error, credenciales inválidas"),
    ("", "password", "Error, campo obligatorio está vacío")
]
for usuario, password, resultado in test_cases:
    print(f"Probando {usuario} se espera → {resultado}")