import getpass

def login():
 usuario= "Christian"
 password= "ABSOLUTO DESTELLO"

 nombre_usuario=input("Ingrese su nombre de usuario")
 contraseña= getpass.getpass("Ingrese su contraseña")

 if usuario == nombre_usuario and password == contraseña:
  print("Inicio exitoso. puedes ingresar", nombre_usuario)
  return True
 else:
     print("Inicio de sesion fallido.")
     return False
if __name__ == "__main__":
   login() 