#This is a mysql code to make MOMO transanction database using MySQL

CREATE DATABASE IF NOT EXISTS momodb;
USE momodb;

CREATE TABLE User (
	user_id INT AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(50),
	phone VARCHAR(50),
	password VARCHAR(50)
);

CREATE TABLE Role (
	role_id INT AUTO_INCREMENT PRIMARY KEY,
	role_name VARCHAR(50)
);

CREATE TABLE UserRole (
	user_id INT NOT NULL,
	role_id INT NOT NULL,
	PRIMARY KEY (user_id, role_id),
	FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (role_id) REFERENCES Role(role_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Categories (
	category_id INT AUTO_INCREMENT PRIMARY KEY,
	category_name VARCHAR(50)
);

CREATE TABLE Transactions (
	transaction_id INT AUTO_INCREMENT PRIMARY KEY,
	amount FLOAT NOT NULL,
	timestamp DATETIME NOT NULL,
	currency VARCHAR(50),
	reciever_id INT NOT NULL,
	sender_id INT NOT NULL,
	category_id INT NOT NULL,
	FOREIGN KEY (reciever_id) REFERENCES User(user_id),
	FOREIGN KEY (sender_id) REFERENCES User(user_id),
	FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

CREATE TABLE System_logs (
	log_id INT AUTO_INCREMENT PRIMARY KEY,
	user_id INT NOT NULL,
	endpoint VARCHAR(50),
	status_code INT NOT NULL,
	execution_time_ms FLOAT,
	FOREIGN KEY (user_id) REFERENCES User(user_id)
);
