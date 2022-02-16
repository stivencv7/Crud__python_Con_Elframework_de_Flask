create database crud;
use crud;

create table usuario
(codigo INT(11) primary key auto_increment not null,
nombre VARCHAR(30) ,
apellido VARCHAR(30),
edad INT,
cedula varchar(30) Unique key,
fecha DATE,
hora TIME
);