CREATE DATABASE fooddb;
\c fooddb;

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    dish VARCHAR(50),
    username VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE menu (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    image VARCHAR(100)
);

INSERT INTO menu (name, image) VALUES
('Masala Dosa','dosa.jpg'),
('Soft Idli','idli.jpg'),
('Medu Vada','vada.jpg'),
('Sambar','sambar.jpg');

