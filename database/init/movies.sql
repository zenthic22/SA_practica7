create database if not exists movies_db;

use movies_db;

CREATE TABLE movies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    year INT,
    genre VARCHAR(100)
);

CREATE TABLE movies_actors (
    movie_id INT,
    actor_id INT,
    PRIMARY KEY(movie_id, actor_id)
);