CREATE DATABASE IF NOT EXISTS travel_guide;
USE travel_guide;

CREATE TABLE IF NOT EXISTS destinations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    location VARCHAR(100),
    weather VARCHAR(100)
);
