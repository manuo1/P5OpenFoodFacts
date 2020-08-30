import mysql.connector

from ressources.constants import (QUERY_CREATION_LIST,
                                  QUERY_INSERT_DATA_TO_FAVORITES_TABLE,
                                  QUERY_INSERT_DATA_TO_PRODUCTS_TABLE,
                                  QUERY_USE_DATABASE)
from ressources.settings import CONNECTION_DATA


class DataBase:
    """all database requests"""

    # mysql connection
    try:
        # create connection
        connection = mysql.connector.connect(
            host=CONNECTION_DATA['host'],
            user=CONNECTION_DATA['user'],
            password=CONNECTION_DATA['password'],
        )
        cursor = connection.cursor()
    # if connection error return the error
    except mysql.connector.Error as connect_error:
        print(connect_error)
        quit()

    def __init__(self):
        self.categories_dict = {}

    def create_data_base(self):
        """create data base and tables"""
        try:
            for request in QUERY_CREATION_LIST:
                DataBase.cursor.execute(request)
            DataBase.connection.commit()
        except mysql.connector.Error as connect_error:
            print(connect_error)
            quit()

    def select_database(self):
        DataBase.cursor.execute(QUERY_USE_DATABASE)

    def get_categories_dict(self):
        """get all categories from categories table"""
        request = 'SELECT * FROM categories'
        DataBase.cursor.execute(request)
        categories_list = DataBase.cursor.fetchall()
        for list in categories_list:
            self.categories_dict[list[0]] = list[1]
        return self.categories_dict

    def add_products(self, products):
        """add product to products table"""
        try:
            insert_request = QUERY_INSERT_DATA_TO_PRODUCTS_TABLE
            for product in products:
                try:
                    data_to_add = (
                        product.product_name_fr,
                        product.nutriscore_grade,
                        product.url,
                        product.stores,
                        product.code,
                        product.id_category,
                    )
                    DataBase.cursor.execute(insert_request, data_to_add)
                except mysql.connector.Error as connect_error:
                    print(connect_error)
            DataBase.connection.commit()
        except mysql.connector.Error as connect_error:
            print('Impossible d\'ajouter les produits à la table')
            print(connect_error)
            quit()

    def add_favorites(self, id_product_S, id_product_R):
        """add favorites to products table"""
        try:
            insert_request = QUERY_INSERT_DATA_TO_FAVORITES_TABLE
            try:
                data_to_add = (
                    id_product_S.id_product,
                    id_product_R.id_product,
                )
                DataBase.cursor.execute(insert_request, data_to_add)
            except mysql.connector.Error as connect_error:
                print(connect_error)
            DataBase.connection.commit()
        except mysql.connector.Error as connect_error:
            print(connect_error)

    def get_category_product_list(self, chosen_category):
        """ get a product list from one categorie saved in products table"""
        request = 'SELECT * FROM products WHERE id_category = "{}"'.format(
            chosen_category
        )
        DataBase.cursor.execute(request)
        category_product_list = DataBase.cursor.fetchall()
        return category_product_list

    def get_product_by_nutriscore(self, product_to_replace):
        """get a product list from one categorie with better nutriscore"""
        request = (
            'SELECT * FROM products '
            'WHERE id_category = "{}"'
            'AND nutriscore_grade < "{}"'.format(
                product_to_replace.id_category,
                product_to_replace.nutriscore_grade,
            )
        )
        DataBase.cursor.execute(request)
        replacement_product_list = DataBase.cursor.fetchall()
        return replacement_product_list

    def get_all_favorites(self):
        """get list of all favorites"""
        request = 'SELECT * FROM favorites'
        DataBase.cursor.execute(request)
        favorites = DataBase.cursor.fetchall()
        return favorites

    def get_product_by_id(self, id_product):
        """ get the product with the given id """
        request = 'SELECT * FROM products ' 'WHERE id_product = "{}"'.format(
            id_product
        )
        DataBase.cursor.execute(request)
        product = DataBase.cursor.fetchall()
        return product
