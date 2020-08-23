QUERY_DROP_DATABASE = (
                    'DROP DATABASE IF EXISTS P5_data_base')
QUERY_CREATE_DATABASE = (
                    'CREATE DATABASE IF NOT EXISTS P5_data_base')
QUERY_USE_DATABASE = (
                    'USE P5_data_base')
QUERY_DROP_TABLE_CATEGORIES = (
                    'DROP TABLE IF EXISTS categories')
QUERY_CREATE_TABLE_CATEGORIES = (
                    'CREATE TABLE IF NOT EXISTS categories('
                    'id_category	SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,'
                    'category_name	VARCHAR(40) NOT NULL,'
                    'PRIMARY KEY(id_category))'
                    'ENGINE=INNODB')
QUERY_DROP_TABLE_PRODUCTS = (
                    'DROP TABLE IF EXISTS products')
QUERY_CREATE_TABLE_PRODUCTS = (
                    'CREATE TABLE IF NOT EXISTS products('
                    'id_product	SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,'
                    'generic_name_fr	VARCHAR(255) NOT NULL,'
                    'nutriscore_grade	CHAR(1) NOT NULL,'
                    'url	VARCHAR(255) NOT NULL,'
                    'purchase_places	VARCHAR(100),'
                    'code BIGINT UNSIGNED,'
                    'id_category SMALLINT UNSIGNED,'
                    'CONSTRAINT fk_categories_id_category'
                    '        FOREIGN KEY (id_category)'
                    '        REFERENCES categories(id_category),'
                    'PRIMARY KEY(id_product))'
                    'ENGINE=INNODB')
QUERY_DROP_TABLE_FAVORITES = (
                    'DROP TABLE IF EXISTS favorites')
QUERY_CREATE_TABLE_FAVORITES = (
                    'CREATE TABLE IF NOT EXISTS favorites('
                    'id_favorite	SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,'
                	'id_product_S SMALLINT UNSIGNED NOT NULL,'
                    'id_product_R SMALLINT UNSIGNED NOT NULL,'
                    'CONSTRAINT fk_products_id_product'
	                '  FOREIGN KEY (id_product_S)'
	                '  REFERENCES products(id_product),'
			        '  FOREIGN KEY (id_product_R)'
	                '  REFERENCES products(id_product),'
                    '  PRIMARY KEY(id_favorite))'
                    '  ENGINE=INNODB')
QUERY_INSERT_CATEGORIES_VALUES = (
                    'INSERT INTO categories (category_name)'
                    'VALUES'
                    '("Aliments d\'origine végétale"),'
                    '("Boisson"),'
                    '("Céréales et pommes de terre"),'
                    '("Poissons"),'
                    '("Viande")')
QUERY_INSERT_DATA_TO_PRODUCTS_TABLE = (
                    "INSERT INTO products ("
                    "generic_name_fr, "
                    "nutriscore_grade, "
                    "url, "
                    "purchase_places, "
                    "code, "
                    "id_category) "
                    "VALUES (%s, %s, %s, %s, %s, %s)")
PAYLOAD = {"search_terms": "",
           #categories contient :
           "tagtype_0": "categories",
           "tag_contains_0": "contains",
           "tag_0": "",
           #produits avec un nutriscore
           "nutriment_0": "nutrition-score-fr",
           "nutriment_compare_0": "gt",
           "nutriment_value_0": 0,
           #trié par popularité
           "sort_by": "Popularity",
           #500 resultat sur la page
           "page_size": 1,
           #resultat en json
           "json": 1}
ESSENTIAL_PRODUCT_KEYS = ['generic_name_fr', 'nutriscore_grade',
                          'url', 'purchase_places', 'code']
ESSENTIAL_PRODUCT_DATA = ['generic_name_fr', 'nutriscore_grade', 'url', 'code']

QUERY_CREATION_LIST = [QUERY_DROP_DATABASE, QUERY_CREATE_DATABASE,
                       QUERY_USE_DATABASE, QUERY_DROP_TABLE_CATEGORIES,
                       QUERY_CREATE_TABLE_CATEGORIES,
                       QUERY_DROP_TABLE_PRODUCTS, QUERY_CREATE_TABLE_PRODUCTS,
                       QUERY_DROP_TABLE_FAVORITES, QUERY_CREATE_TABLE_FAVORITES,
                       QUERY_INSERT_CATEGORIES_VALUES]
QUANTITIES_OF_PRODUCTS_FOR_EACH_CATEGORY = 200
PRODUCT_QUANTITY_FOR_CHOOSE = 20
