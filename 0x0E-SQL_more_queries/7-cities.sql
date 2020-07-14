-- cities

-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Select database
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS cities ( id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENTED, state_id INT NOT NULL FOREIGN_KEY(state_id) REFERENCE states(id), name VARCHAR(256) NOT NULL);
