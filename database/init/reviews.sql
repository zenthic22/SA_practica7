create database if not exists reviews_db;

use reviews_db;

CREATE TABLE reviews (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    movie_id INT,
    comment TEXT,
    rating INT
);