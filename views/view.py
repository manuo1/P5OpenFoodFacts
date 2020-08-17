class View():
    def __init__(self):
        pass

    def ask_to_instal_data_base(self):
        self.double_line_msg('Voulez vous installer la base de donnée ? (O/N)')
        user_answer = input()
        return user_answer

    def choose_scenario(self):
        self.double_line_msg('Que souhaitez vous faire ?')
        print('1 - Remplacer un aliment \n'
              '2 - Retrouver mes aliments substitués.')
        try:
            user_answer = int(input())
        except:
            self.wrong_user_response_message(2)
            user_answer = self.choose_scenario()
        if user_answer != 1 and user_answer != 2:
            self.wrong_user_response_message(2)
            user_answer = self.choose_scenario()
        return user_answer

    def choose_category(self, categories_dict):
        max_key = max(categories_dict.keys())
        self.double_line_msg("Dans quelle categorie voulez"
                             " vous substituer l'aliment ?")
        for id, category in categories_dict.items():
            print('{} : {}'.format(id, category))
        try:
            user_answer = int(input())
        except:
            self.wrong_user_response_message(max_key)
            user_answer = self.choose_category(categories_dict)
        if user_answer not in categories_dict.keys():
            self.wrong_user_response_message(max_key)
            user_answer = self.choose_category(categories_dict)
        return user_answer

    def choose_product(self, random_object_dict):
        """ask user to choose a product"""
        max_key = max(random_object_dict.keys())
        self.double_line_msg("Liste d'aliments de la catégorie :")
        for key,product in random_object_dict.items():
            print("{} : {} (nutriscore {})".format(key,
                                                   product.generic_name_fr,
                                                   product.nutriscore_grade))
        self.double_line_msg("Quel aliment voulez vous substituer ?")
        try:
            chosen_product = int(input())
            if chosen_product not in random_object_dict.keys():
                self.wrong_user_response_message(max_key)
                product_to_replace = self.choose_product(random_object_dict)
            else:
                product_to_replace = random_object_dict[chosen_product]
        except:
            self.wrong_user_response_message(max_key)
            product_to_replace = self.choose_product(random_object_dict)
        return product_to_replace

    def choose_replacment_product(self, product_to_replace, random_replacement_object_dict):
        max_key = max(random_replacement_object_dict.keys())
        self.double_line_msg("les produits suivant appartiennent à la meme\n"
                             "categorie mais on un meilleur nutriscore que\n"
                             "{} (nutriscore {})".format(product_to_replace.generic_name_fr,
                                                         product_to_replace.nutriscore_grade))
        for key,product in random_replacement_object_dict.items():
            print("{} : {} (nutriscore {})".format(key,
                                                   product.generic_name_fr,
                                                   product.nutriscore_grade))
        self.double_line_msg("Quel aliment voulez vous sauvegarder ?")
        try:
            chosen_product = int(input())
            if chosen_product not in random_replacement_object_dict.keys():
                self.wrong_user_response_message(max_key)
                product_to_save = self.choose_replacment_product(product_to_replace, random_replacement_object_dict)
            else:
                product_to_save = random_replacement_object_dict[chosen_product]
        except:
            self.wrong_user_response_message(max_key)
            product_to_save = self.choose_replacment_product(product_to_replace, random_replacement_object_dict)
        return product_to_save

    def no_replacment_product(self, product_to_replace):
        self.double_line_msg("désolé mais il n'existe pas de produit\n"
                             "de remplacement dans cette categorie pour\n"
                             "{} (nutriscore {})".format(product_to_replace.generic_name_fr,
                                                         product_to_replace.nutriscore_grade))

    def wrong_user_response_message(self,number):
        print("\n#####################################################\n"
              "Votre reponse doit être un chifre de 1 à {}\n"
              "#####################################################\n"
              .format(number))
    def double_line_msg(self,msg):
        print('\n---------------------------------------------------------\n'
              '{} \n'
              '---------------------------------------------------------\n'
              .format(msg))
