create database if not exists projeto_db
default character set utf8
default collate utf8_general_ci;

use projeto_db;

create table if not exists usuario (
	id			int not null auto_increment,
	nome 		varchar(80) not null,
	senha		varchar(20) not null,
    sexo 		enum('M', 'F'),
	nivel		int not null,
	endereco	varchar(300),
	primary key (id)
) engine = innoDB default charset = utf8; # Por Default o banco criado já vem com engine innoDB, mas quis deixar isso explícito.

insert into usuario values (default, 'admin', '1234', 'M', '2', '-----');
insert into usuario values (default, 'user', '1234', 'M', '1', '-----');

create table if not exists produto(
	id int not null auto_increment,
	nome varchar(100) not null,
	grupo varchar(100),
	preco decimal(4, 2) unsigned not null,
	primary key (id)
) engine = innoDB default charset = utf8;

insert into produto values (default, 'Pizza de Calabresa', 'Pizzas', '26.90');
insert into produto values (default, 'Pizza de Mussarela', 'Pizzas', '26.90');
insert into produto values (default, 'Coca-Cola', 'Bebidas', '08.50');

create table if not exists pedido(
	id int not null auto_increment,
	nome_pessoa_pedido varchar(100) not null,
    produto_requerido varchar(200) not null,
    usuario	varchar(80) not null,
    senha varchar(20) not null,
	localEntrega varchar(500),
	observacoes text,
    primary key(id)
) engine = innoDB default charset = utf8;

insert into pedido values (default, 'Leonaldo', 'pizza de calabresa, coca-cola', 'user', '1234', '-------', 'pizza sem cebola e sem tomate, coca de 2 litros');

create table if not exists ProdutoPedidos (
	id int not null auto_increment,
    data_hora datetime,
    id_produto int,
    id_pedido int,
    foreign key (id_produto) references produto (id),
    foreign key (id_pedido) references pedido (id),
    primary key(id)
) engine = innoDB default charset = utf8;
