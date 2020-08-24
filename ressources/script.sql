DROP DATABASE IF EXISTS P5_data_base;
CREATE DATABASE IF NOT EXISTS P5_data_base;
USE P5_data_base;

DROP TABLE IF EXISTS categories;
CREATE TABLE IF NOT EXISTS categories(
	id_category	SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	category_name	VARCHAR(40) NOT NULL,
	PRIMARY KEY(id_category)
)
ENGINE=INNODB;

DROP TABLE IF EXISTS products;
CREATE TABLE IF NOT EXISTS products(
	id_product	SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	product_name_fr	VARCHAR(255) NOT NULL,
	nutriscore_grade	CHAR(1) NOT NULL,
	url	VARCHAR(255) NOT NULL,
	stores	VARCHAR(100),
	code BIGINT UNSIGNED,
	id_category SMALLINT UNSIGNED,
	CONSTRAINT fk_categories_id_category
	        FOREIGN KEY (id_category)
	        REFERENCES categories(id_category),
	PRIMARY KEY(id_product)
)
ENGINE=INNODB;

DROP TABLE IF EXISTS favorites;
CREATE TABLE IF NOT EXISTS favorites(
  id_favorite	SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	id_product_S SMALLINT UNSIGNED NOT NULL,
	id_product_R SMALLINT UNSIGNED NOT NULL,
	CONSTRAINT fk_products_id_product
	        FOREIGN KEY (id_product_S)
	        REFERENCES products(id_product),
					FOREIGN KEY (id_product_R)
	        REFERENCES products(id_product),
	PRIMARY KEY(id_favorite)
)
ENGINE=INNODB;

INSERT INTO categories (category_name)
VALUES
("Aliments d'origine végétale"),
('Boisson'),
('Céréales et pommes de terre'),
('Poissons'),
('Viande');
