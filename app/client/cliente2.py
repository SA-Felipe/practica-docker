import requests
import random
import time
import logging as log

log.basicConfig(level=log.INFO)

# URL de tu servidor Flask
server_url = 'http://servidor:5000'

def generate_random_username():
    # Genera un nombre de usuario aleatorio
    return 'user' + str(random.randint(1, 1000))

def generate_random_product():
    # Genera un nombre y precio aleatorio para un producto
    product_name = 'product' + str(random.randint(1, 100))
    product_price = round(random.uniform(5.0, 100.0), 2)
    return {'name': product_name, 'price': product_price}

def send_request():
    # Decide aleatoriamente si enviar una solicitud de usuario, producto o compra
    choice = random.choice(['user', 'product', 'purchase'])

    if choice == 'user':
        # Envia una solicitud al servidor Flask con un nombre de usuario aleatorio
        username = generate_random_username()
        log.info("Registering User: %s", username)
        response = requests.post(f'{server_url}/formulario', data={'nombre': username})
        log.info("SUCCESFULLY REGISTERED User: %s", username)
    elif choice == 'product':
        # Envia una solicitud al servidor Flask con un nuevo producto aleatorio
        product_data = generate_random_product()
        log.info("Adding Product: %s", product_data)
        response = requests.post(f'{server_url}/add_producto', data=product_data)
        log.info("SUCCESFULLY ADDED Product: %s", product_data)
    elif choice == 'purchase':
        # Envia una solicitud al servidor Flask con una compra aleatoria
        user_id = random.randint(1, 1000)
        product_id = random.randint(1, 100)
        quantity = random.randint(1, 10)
        log.info("Making Purchase: User ID %s, Product ID %s, Quantity %s", user_id, product_id, quantity)
        response = requests.post(f'{server_url}/compra', data={'usuario_id': user_id, 'producto_id': product_id, 'cantidad': quantity})
        log.info("SUCCESFULLY MADE Purchase: User ID %s, Product ID %s, Quantity %s", user_id, product_id, quantity)

if __name__ == '__main__':
    while True:
        # Envia solicitudes indefinidamente
        send_request()

        # Duerme un tiempo aleatorio entre 10 y 15 segundos
        sleep_time = random.uniform(10, 15)
        time.sleep(sleep_time)
