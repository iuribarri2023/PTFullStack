class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

# Crear una instancia de la clase User
usuario = User("iuribarri007", "mi_contraseña")

# Acceder y mostrar los atributos del objeto 'usuario'
print(f"Nombre de usuario: {usuario.name}")
print(f"Contraseña: {usuario.password}")