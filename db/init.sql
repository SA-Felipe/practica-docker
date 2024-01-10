-- init.sql

-- Crea la base de datos
CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

-- Tabla de usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50)
);

-- Tabla de productos
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10, 2)
);

-- Tabla de compras
CREATE TABLE compras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    producto_id INT,
    cantidad INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

-- Inserta datos de ejemplo
INSERT INTO usuarios (nombre) VALUES ('Juan'), ('Marta'), ('Pedro'), ('Laura');
INSERT INTO productos (nombre, precio) VALUES ('Producto1', 10.50), ('Producto2', 20.75);
INSERT INTO compras (usuario_id, producto_id, cantidad) VALUES (1, 1, 2), (2, 2, 1), (3, 1, 1);
