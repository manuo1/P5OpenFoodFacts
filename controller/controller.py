from random import sample

from api.api import Api
from database.database import DataBase
from models.product import Product
from ressources.constants import PRODUCT_QUANTITY_FOR_CHOOSE
from views.view import View


class Controller:
    def __init__(self):
        self.database = DataBase()
        self.api = Api()
        self.view = View()

    def process(self):
        """principal menu"""
        self.database.select_database()
        scenario = self.view.choose_scenario()
        if scenario == 1:
            self.scenario_substitute_a_product()
            self.process()
        elif scenario == 2:
            self.scenario_display_favorites()
            self.process()
        elif scenario == 3:
            db_install = self.view.ask_to_instal_data_base()
            self.install_data_base(db_install)
            self.process()
        elif scenario == 4:
            quit()

    def scenario_display_favorites(self):
        """scenario if user want to display favorites"""
        favorite_objects_dict = self.get_favorite_objects_dict()
        self.view.display_favorites(favorite_objects_dict)
        self.process()

    def get_favorite_objects_dict(self):
        """create a dictionary with favorites"""
        favorites = self.database.get_all_favorites()
        favorite_products_id_dict = {}
        favorite_objects_dict = {}
        if favorites:
            for raw in favorites:
                if raw[1] in favorite_products_id_dict.keys():
                    product_R_list = favorite_products_id_dict[raw[1]]
                    product_R_list.append(raw[2])
                else:
                    product_R_list = [raw[2]]
                favorite_products_id_dict[raw[1]] = product_R_list
        for product_S_id in favorite_products_id_dict.keys():
            product_S = self.database.get_product_by_id(product_S_id)
            object_product_S = self.transform_product_into_object(product_S[0])
            object_product_R_list = []
            for product_R_id in favorite_products_id_dict[product_S_id]:
                product_R = self.database.get_product_by_id(product_R_id)
                object_product_R = self.transform_product_into_object(
                    product_R[0]
                )
                object_product_R_list.append(object_product_R)
            favorite_objects_dict[object_product_S] = object_product_R_list
        return favorite_objects_dict

    def scenario_substitute_a_product(self):
        """ scenario if user want to substitute a product"""
        categories_dict = self.database.get_categories_dict()
        chosen_category = self.view.choose_category(categories_dict)
        category_product_list = self.database.get_category_product_list(
            chosen_category
        )
        category_object_list = self.transform_prod_list_into_obj_list(
            category_product_list
        )
        random_object_dict = self.choose_random_products(
            category_object_list, PRODUCT_QUANTITY_FOR_CHOOSE
        )
        product_to_replace = self.view.choose_product(random_object_dict)
        replacement_product_list = self.database.get_product_by_nutriscore(
            product_to_replace
        )
        if replacement_product_list:
            replacement_object_list = self.transform_prod_list_into_obj_list(
                replacement_product_list
            )
            best_replacement_object_dict = self.choose_best_replacement(
                replacement_object_list
            )
            chosen_replacement_product = self.view.choose_replacement_product(
                product_to_replace, best_replacement_object_dict
            )
            if chosen_replacement_product:
                need_to_save = self.view.save_chosen_replacement_product(
                    product_to_replace, chosen_replacement_product
                )
                if need_to_save == 'O' or need_to_save == 'o':
                    self.database.add_favorites(
                        product_to_replace, chosen_replacement_product
                    )
        else:
            self.view.no_replacement_product(product_to_replace)

    def install_data_base(self, instal_msg):
        """ clear an reinstal database and product from api """
        if instal_msg == 'O' or instal_msg == 'o':
            categories_dict = self.database.get_categories_dict()
            raw_api_products = self.api.download_products(categories_dict)
            if not raw_api_products:
                self.view.connection_off_impossible()
            else:
                cleaned_products_list = self.api.clean_products(
                    raw_api_products
                )
                product_list = self.transform_prod_list_into_obj_list(
                    cleaned_products_list
                )
                self.database.create_data_base()
                self.database.add_products(product_list)

    def transform_prod_list_into_obj_list(self, products_list):
        """transform products list into objects list"""
        object_product_list = []
        for product in products_list:
            product_to_add = self.transform_product_into_object(product)
            object_product_list.append(product_to_add)
        return object_product_list

    def transform_product_into_object(self, product):
        """transform products into objects"""
        product_object = Product()
        product_object.id_product = product[0]
        product_object.product_name_fr = product[1]
        product_object.nutriscore_grade = product[2]
        product_object.url = product[3]
        product_object.stores = product[4]
        product_object.code = product[5]
        product_object.id_category = product[6]
        return product_object

    def choose_random_products(self, object_list, quantity):
        """choose a random quantity of objects in a list"""
        random_object_dict = {}
        if len(object_list) < quantity:
            random_list_size = len(object_list)
        else:
            random_list_size = quantity
        random_list = sample(object_list, random_list_size)
        for index, product in enumerate(random_list):
            random_object_dict[index + 1] = product
        return random_object_dict

    def choose_best_replacement(self, replacement_object_list):
        """ select the 3 best replacement product"""
        sorted_replacement_object_list = sorted(
            replacement_object_list,
            key=lambda product: product.nutriscore_grade,
        )
        if len(sorted_replacement_object_list) > 3:
            best_replacement_object_list = sorted_replacement_object_list[0:3]
        else:
            best_replacement_object_list = sorted_replacement_object_list
        best_replacement_object_dict = {}
        for index, product in enumerate(best_replacement_object_list):
            best_replacement_object_dict[index + 1] = product
        return best_replacement_object_dict
