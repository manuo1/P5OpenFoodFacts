import requests
from ressources.constants import (PAYLOAD,
                                  ESSENTIAL_PRODUCT_DATA,
                                  ESSENTIAL_PRODUCT_KEYS,
                                  QUANTITIES_OF_PRODUCTS_FOR_EACH_CATEGORY)

class Api():
    def __init__(self):
        pass

    def download_products(self, categories_dict):
        """get products of a category from open food fact api"""
        raw_api_products =[]
        for category_id, category_name in categories_dict.items():
            PAYLOAD["tag_0"] = category_name
            PAYLOAD["page_size"] = QUANTITIES_OF_PRODUCTS_FOR_EACH_CATEGORY*2
            server_response = requests.get(
                                "https://fr.openfoodfacts.org/cgi/search.pl?",
                                params=PAYLOAD)
            if server_response.status_code==200:
                results = server_response.json()
                temp_raw_api_products = results["products"]
                #add category_id to product
                for product in temp_raw_api_products:
                    product['id_category'] = category_id
                    raw_api_products.append(product)
            else:
                print(server_response.status_code)
        return raw_api_products


    def clean_products(self, raw_api_products):
        """keeps only usable products and data"""
        cleaned_products_list = []
        for raw_product in raw_api_products:
            cleaned_product=[]
            if (all(key in raw_product for key in ESSENTIAL_PRODUCT_KEYS) and
                all(raw_product[data]!='' for data in ESSENTIAL_PRODUCT_DATA)):
                #add useful product data in cleaned product list
                cleaned_product.append('NULL')
                for product_keys in ESSENTIAL_PRODUCT_KEYS:
                    cleaned_product.append(raw_product[product_keys])
                cleaned_product.append(raw_product['id_category'])
                cleaned_products_list.append(cleaned_product)
        return cleaned_products_list
