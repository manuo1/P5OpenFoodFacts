-- -----------------------------------------------------
-- DataBase p5_data_base
-- -----------------------------------------------------
DROP DATABASE IF EXISTS P5_data_base;

CREATE SCHEMA IF NOT EXISTS `p5_data_base` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `p5_data_base` ;

-- -----------------------------------------------------
-- Table `p5_data_base`.`categories`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `categories` ;

CREATE TABLE IF NOT EXISTS `categories` (
  `id_category` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `category_name` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`id_category`))
ENGINE = INNODB;

-- -----------------------------------------------------
-- Table `products`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `products` ;

CREATE TABLE IF NOT EXISTS `products` (
  `id_product` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `product_name_fr` VARCHAR(255) NOT NULL,
  `nutriscore_grade` CHAR(1) NOT NULL,
  `url` VARCHAR(255) NOT NULL,
  `stores` VARCHAR(100),
  `code` BIGINT UNSIGNED,
  `id_category` SMALLINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_product`),
  CONSTRAINT `fk_categories_id_category`
    FOREIGN KEY (`id_category`)
    REFERENCES `categories` (`id_category`))
ENGINE = INNODB;

-- -----------------------------------------------------
-- Table `favorites`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `favorites` ;

CREATE TABLE IF NOT EXISTS `favorites` (
  `id_product_S` SMALLINT UNSIGNED NOT NULL,
  `id_product_R` SMALLINT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_product_S`,`id_product_R`),
  CONSTRAINT `fk_products_id_product_id_product_S`
    FOREIGN KEY (`id_product_S`)
    REFERENCES `products` (`id_product`),
  CONSTRAINT `fk_products_id_product_id_product_R`
    FOREIGN KEY (`id_product_R`)
    REFERENCES `products` (`id_product`))
ENGINE = INNODB;

-- -----------------------------------------------------
-- INSERT table categories
-- -----------------------------------------------------
INSERT INTO categories (category_name)
VALUES
("Aliments d'origine végétale"),
('Boisson'),
('Céréales et pommes de terre'),
('Poissons'),
('Viande');
