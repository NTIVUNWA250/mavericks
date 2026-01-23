# MOMO SMS DATA

This is a project designated to design a website that processes MoMo SMS data in XML format, clean and categorize the data, store it in a relational database, and offer a frontend interface to analyze and visualize the data to the user

## Group

### Group name

Group 10

### Members of the group

- NTIVUNWA Gilbert
- MUNEZERO Bonheur Divin
- CYUZUZO BANA Terance
- NIYONKURU MITALI Tony Robert

## Links

### System Archtecture

<a href="https://drive.google.com/file/d/1-cw2b646HtTUPMaN5KLjdWXnr5V8eOKA/view?usp=drive_link">https://drive.google.com/file/d/1-cw2b646HtTUPMaN5KLjdWXnr5V8eOKA/view?usp=drive_link</a>

### Scrum board

<a href="https://trello.com/invite/b/69653651397005213e652d1a/ATTI1da4cb5334fc2e4b318a55886313ada03D049AB5/momo-sms-processor-dashboard">Scrum Board Link...

### ERD Link

<a href="https://app.diagrams.net/#G1DYrXlf6Sy5uW1_Pp3c6_f7Q1TlZ7xHAt#%7B%22pageId%22%3A%22qkKeDmOhXN2t1sRSeOZN%22%7D">ERD DIAGRAM ON PAGE 2...</a>

### DATABASE DESIGN DOCUMENT LINK

<a href="https://docs.google.com/document/d/16oIJLtl-AD3HwPKPV8Ql4VqmlUuKjbo4LZriNAMn1_w/edit?usp=sharing">Database Design Document on GOOGLE DRIVE</a>

## Usage

...

## Features

- **DATABASE** :
  1.  Our Database is set to a 3rd Normal Form to minimise redundacy
  2.  It contains `UserRoles` as the junction table which managesthe many to many relationship between Users table and Roles table
  3.  It contains two foreign keys (`sender_id`, `receiver_id`) in the `Transactions table` and they point to the `Users` entity.
  4.  It Contains a `System Logs` table to track API interaction with regard to the user activity
