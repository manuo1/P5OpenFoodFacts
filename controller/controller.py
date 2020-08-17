from random import sample
from database.database import DataBase
from views.view import View
from api.api import Api
from models.product import Product
from ressources.constants import (PRODUCT_QUANTITY_FOR_CHOOSE)


class Controller():

    def __init__(self):
        self.database = DataBase()
        self.api = Api()
        self.view = View()

    def process(self):
        """principal menu"""
        #ask user if the system should reinstall the database
        user_answer = self.view.ask_to_instal_data_base()
        self.install_data_base(user_answer)
        #choice of scenario
        scenario = self.view.choose_scenario()
        if scenario == 1:
            self.scenario_substitute_a_product()
        elif scenario == 2:
            #self.view.scenario_2()
            print('scenario 2')

    def scenario_substitute_a_product(self):
        categories_dict = self.database.get_categories_dict()
        chosen_category = self.view.choose_category(categories_dict)
        category_product_list = self.database.get_category_product_list(chosen_category)
        category_object_list = self.transform_into_object(category_product_list)
        random_object_dict = self.choose_random_products(category_object_list, PRODUCT_QUANTITY_FOR_CHOOSE)
        product_to_replace = self.view.choose_product(random_object_dict)
        replacement_product_list = self.database.get_product_by_nutriscore(product_to_replace)
        if replacement_product_list:
            replacement_object_list =self.transform_into_object(replacement_product_list)
            random_replacement_object_dict = self.choose_random_products(replacement_object_list, 3)
            chosen_replacment_product = self.view.choose_replacment_product(product_to_replace, random_replacement_object_dict)
        else:
            self.view.no_replacment_product(product_to_replace)
            self.scenario_substitute_a_product()

    def install_data_base(self, instal_msg):
        if instal_msg =='O' or instal_msg =='o':
            self.database.create_data_base()
            categories_dict = self.database.get_categories_dict()
            raw_api_products = self.api.download_products(categories_dict)
            cleaned_products_list = self.api.clean_products(raw_api_products)
            product_list = self.transform_into_object(cleaned_products_list)
            self.database.add_products(product_list)
        else:
            self.database.select_database()

    def transform_into_object(self, products_list):
        """transform products into objects"""
        product_list = []
        for product in products_list:
            product_to_add = Product()
            product_to_add.id_product =  product[0]
            product_to_add.generic_name_fr = product[1]
            product_to_add.nutriscore_grade = product[2]
            product_to_add.url = product[3]
            product_to_add.purchase_places = product[4]
            product_to_add.code = product[5]
            product_to_add.id_category = product[6]
            product_list.append(product_to_add)
        return product_list

    def choose_random_products(self, object_list, quantity):
        random_object_dict = {}
        if len(object_list) < quantity:
            random_list_size = len(object_list)
        else:
            random_list_size = quantity
        random_list = (sample(object_list, random_list_size))
        for index, product in enumerate(random_list):
            random_object_dict[index+1] = product
        return random_object_dict
