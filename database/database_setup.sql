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

-- AI advised to add constraints and comments and below are its codes
ALTER TABLE Transactions
ADD CONSTRAINT chk_positive_amount CHECK (amount > 0),
ADD CONSTRAINT chk_different_parties CHECK (sender_id <> reciever_id);

CREATE INDEX idx_transaction_id ON Transactions(transaction_id);
CREATE INDEX idx_user_phone ON User(phone);

ALTER TABLE User MODIFY COLUMN phone VARCHAR(50) COMMENT 'Unique phone number from SMS';
ALTER TABLE Transactions MODIFY COLUMN transaction_id INT COMMENT 'Maps to TxId from MoMo SMS';

ALTER TABLE Transactions
MODIFY COLUMN transaction_id INT AUTO_INCREMENT COMMENT 'Maps to TxId from MoMo SMS';

-- AI advised to set foreign key checks to 0 and 1 between our delete from codes
SET FOREIGN_KEY_CHECKS=0;
DELETE FROM Transactions;
DELETE FROM UserRole;
DELETE FROM System_logs;
DELETE FROM User;
DELETE FROM Role;
DELETE FROM Categories;
SET FOREIGN_KEY_CHECKS=1;

--AI advised to set the Reset auto-increment counters
ALTER TABLE Role AUTO_INCREMENT = 1;
ALTER TABLE User AUTO_INCREMENT = 1;
ALTER TABLE Categories AUTO_INCREMENT = 1;
ALTER TABLE Transactions AUTO_INCREMENT = 1;
ALTER TABLE System_logs AUTO_INCREMENT = 1;

INSERT INTO Role (role_name) VALUES ('Admin'), ('Receiver'), ('Sender');

INSERT INTO Categories (category_name) VALUES ('Transfer'), ('Payment'), ('Bank Deposit');

INSERT INTO USER (username, phone, password) VALUES
('Group_10', '+250780000000', 'password@123'),
('Robert', '+250780000001', 'password@124'),
('Terance', '+250780000002', 'password@125'),
('Bonheur', '+250780000003', 'password@126'),
('Gilbert', '+250780000004', 'password@127');

INSERT INTO UserRole (user_id, role_id) VALUES
(5,3), (5,2), (5,1), -- Admin and receiver and sender
(2,3), (3,3), (4,3), (1,1);

INSERT INTO Transactions (amount, timestamp, currency, reciever_id, sender_id, category_id) VALUES
(2000.0, '2024-05-10 16:30:00', 'RWF', 2, 5, 1),
(1000.0, '2024-05-10 16:32:00', 'RWF', 3, 1, 2),
(20000.0, '2024-05-10 17:30:00', 'RWF', 4, 2, 3),
(600.0, '2024-05-11 19:00:00', 'RWF', 2, 3, 1),
(1500.0, '2024-05-11 20:30:00', 'RWF', 2, 5, 3);
