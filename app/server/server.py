from flask import Flask, request, render_template
import logging as log
import mysql.connector

log.basicConfig(level=log.INFO)

app = Flask(__name__)

# Configura la conexion a la base de datos MySQL
db_config = {
    'host': 'mysql',
    'user': 'root',
    'password': 'ejemplo',
    'database': 'mydatabase'
}

def store_user_data(data):
    try:
        # Conecta a la base de datos MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Inserta los datos en la tabla de usuarios
        cursor.execute("INSERT INTO usuarios (nombre) VALUES (%s);", (data,))
        
        # Realiza commit y cierra la conexión
        conn.commit()
        conn.close()
        log.info("Succesfully registered user: %s", data)
    except Exception as e:
        log.warning("Could not insert user in database (%s): %s", data, str(e))

def store_purchase_data(user_id, product_id, quantity):
    try:
        # Conecta a la base de datos MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Inserta los datos en la tabla de compras
        cursor.execute("INSERT INTO compras (usuario_id, producto_id, cantidad) VALUES (%s, %s, %s);", (user_id, product_id, quantity))
        
        # Realiza commit y cierra la conexión
        conn.commit()
        conn.close()
        log.info("Succesfully registered purchase: User ID %s, Product ID %s, Quantity %s", user_id, product_id, quantity)
    except Exception as e:
        log.warning("Could not insert purchase in database (User ID %s, Product ID %s, Quantity %s): %s", user_id, product_id, quantity, str(e))

@app.route('/')
def index():
    return "Bienvenido a mi aplicacion web!"

@app.route('/formulario', methods=['POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        store_user_data(nombre)
        mensaje = f"Hola, {nombre}. Bienvenido a mi app web."
        return mensaje

@app.route('/compra', methods=['POST'])
def compra():
    if request.method == 'POST':
        # Suponiendo que el formulario tiene campos 'usuario_id', 'producto_id' y 'cantidad'
        usuario_id = request.form['usuario_id']
        producto_id = request.form['producto_id']
        cantidad = request.form['cantidad']

        store_purchase_data(usuario_id, producto_id, cantidad)
        mensaje = f"Compra registrada para el usuario {usuario_id}."
        return mensaje

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
