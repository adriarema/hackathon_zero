'''
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable
sin tener en cuenta mayúsculas y minúsculas.
'''

password = 'contraseña'

password_del_usuario = input('Introduzca la contraseña: ')

if password == password_del_usuario.lower():
    print('El password es correcto.')
else:
    print('El password no coincide.')