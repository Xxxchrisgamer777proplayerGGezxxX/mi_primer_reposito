import login
import numero_magico

print ("Bienvenidos al juego, advina el numero magico")
if login.login():
    numero_magico.jugar_numero_magico()
