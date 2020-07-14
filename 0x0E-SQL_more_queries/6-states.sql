-- states

-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- select database
use hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);