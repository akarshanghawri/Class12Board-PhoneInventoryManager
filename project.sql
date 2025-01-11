CREATE DATABASE clgws;

USE clgws;

CREATE TABLE inventory (phone_id INT,
    model VARCHAR(255),
    brand VARCHAR(255),
    storage_capacity INT,
    color VARCHAR(50),
    quantity INT,
    price INT,
    date_added DATE);

INSERT INTO inventory VALUES(1, 'iPhone 13', 'Apple', 128, 'Blue', 10, 50999, '2023-10-01'),
    (2, 'Galaxy S21', 'Samsung', 256, 'Black', 15, 32999, '2023-10-05'),
    (3, 'iPhone 14', 'Apple', 64, 'Silver', 8, 81900, '2023-10-12'),
    (4, 'Galaxy S22', 'Samsung', 128, 'White', 7, 62999, '2023-10-15'),
    (5, 'iPhone 15', 'Apple', 512, 'Red', 12, 109900, '2023-10-20');

CREATE TABLE customer (customer_id INT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    phone_no VARCHAR(15));

INSERT INTO customer VALUES(01, 'Parvati', 'Shailat', 'parvati@gmail.com', '+91 12345 67890'),
    (02, 'Virat', 'Kohli', 'virat@gmail.com', '+91 98765 43210'),
    (03, 'Ayaan', 'Raazi', 'raazi@gmail.com', '+91 99999 55555'),
    (04, 'Ankit', 'Baiyanpuria', 'ankit@gmail.com', '+91 88888 44444'),
    (05, 'David', 'Laid', 'david@gmail.com', '+91 77777 33333');

CREATE TABLE orders (order_id INT,
    customer_id INT,
    phone_id INT,
    order_date DATE,
    total_amount INT,
    payment_status VARCHAR(20));
   
CREATE TABLE bill (bill_id INT,
    order_id INT,
    model VARCHAR(255),
    total_amount INT,
    payment_date DATE);
