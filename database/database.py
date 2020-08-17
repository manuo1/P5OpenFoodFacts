import mysql.connector
from ressources.settings import CONNECTION_DATA
from ressources.constants import (QUERY_CREATION_LIST,QUERY_USE_DATABASE,
                                  QUERY_INSERT_DATA_TO_PRODUCTS_TABLE)

class DataBase():
    #mysql connection
    try:
        #create connection
        connection = mysql.connector.connect(
                host = CONNECTION_DATA['host'],
                user = CONNECTION_DATA['user'],
                password = CONNECTION_DATA['password']
        )
        cursor = connection.cursor()
    #if connection error return the error
    except mysql.connector.Error as connect_error:
        print(connect_error)

    def __init__(self):
        self.categories_dict ={}

    def create_data_base(self):
        """create data base and tables"""
        try:
            for request in QUERY_CREATION_LIST:
                DataBase.cursor.execute(request)
            DataBase.connection.commit()
        except mysql.connector.Error as connect_error:
            print(connect_error)

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
                    data_to_add = ( product.generic_name_fr,
                                    product.nutriscore_grade,
                                    product.url,
                                    product.purchase_places,
                                    product.code,
                                    product.id_category)
                    DataBase.cursor.execute(insert_request, data_to_add)
                except:
                    pass
            DataBase.connection.commit()
        except mysql.connector.Error as connect_error:
            print(connect_error)

    def get_category_product_list(self, chosen_category):
        request = 'SELECT * FROM products WHERE id_category = "{}"'.format(chosen_category)
        DataBase.cursor.execute(request)
        category_product_list = DataBase.cursor.fetchall()
        return category_product_list

    def get_product_by_nutriscore(self, product_to_replace):
        request = ('SELECT * FROM products '
                   'WHERE id_category = "{}"'
                   'AND nutriscore_grade < "{}"'
                   .format(product_to_replace.id_category, product_to_replace.nutriscore_grade))
        DataBase.cursor.execute(request)
        replacement_product_list = DataBase.cursor.fetchall()
        return replacement_product_list
