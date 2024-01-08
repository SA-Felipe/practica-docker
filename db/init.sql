-- init.sql

-- Crea la base de datos
CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

-- Crea una tabla
CREATE TABLE usuarios (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50)
);

-- Inserta valores por defecto
INSERT INTO usuarios (nombre) VALUES ('Juan');
INSERT INTO usuarios (nombre) VALUES ('Marta');
INSERT INTO usuarios (nombre) VALUES ('Pedro');
INSERT INTO usuarios (nombre) VALUES ('Laura');
