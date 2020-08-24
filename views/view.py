import os

from ressources.constants import YES_NO_ANSWERS


class View():
    def __init__(self):
        pass

    def ask_to_instal_data_base(self):
        """ view to ask if user really want to reinstal the database"""
        self.double_line_msg(
            'Voulez vous vraiement réinstaller la base de donnée ? (O/N)')
        try:
            db_install = input()
        except:
            self.incorrect_entry_msg_y_n()
            db_install = self.ask_to_instal_data_base()
        if db_install not in YES_NO_ANSWERS:
            self.incorrect_entry_msg_y_n()
            db_install = self.ask_to_instal_data_base()
        return db_install

    def choose_scenario(self):
        """ view to choose the scenario"""
        self.double_line_msg('Que souhaitez vous faire ?')
        print('1 - Remplacer un aliment \n'
              '2 - Retrouver mes aliments substitués \n'
              '3 - Réinstaller la base de donnée \n'
              '4 - Quitter le programe')
        try:
            user_answer = int(input())
        except:
            self.incorrect_entry_msg(4)
            user_answer = self.choose_scenario()
        if user_answer not in [1, 2, 3, 4]:
            self.incorrect_entry_msg(4)
            user_answer = self.choose_scenario()
        return user_answer

    def choose_category(self, categories_dict):
        """ view to choose the category"""
        max_key = max(categories_dict.keys())
        self.double_line_msg("Dans quelle categorie voulez"
                             " vous substituer l'aliment ?")
        for id, category in categories_dict.items():
            print('{} : {}'.format(id, category))
        try:
            user_answer = int(input())
        except:
            self.incorrect_entry_msg(max_key)
            user_answer = self.choose_category(categories_dict)
        if user_answer not in categories_dict.keys():
            self.incorrect_entry_msg(max_key)
            user_answer = self.choose_category(categories_dict)
        return user_answer

    def choose_product(self, random_object_dict):
        """ view to choose the product"""
        max_key = max(random_object_dict.keys())
        self.double_line_msg("Liste d'aliments de la catégorie :")
        for key, product in random_object_dict.items():
            print("{} : {} (nutriscore {})".format(
                                                key,
                                                self.limit_string_size(
                                                    product.product_name_fr),
                                                product.nutriscore_grade))
        self.double_line_msg("Quel aliment voulez vous substituer ?")
        try:
            chosen_product_number = int(input())
            if chosen_product_number not in random_object_dict.keys():
                self.incorrect_entry_msg(max_key)
                product_to_replace = self.choose_product(random_object_dict)
            else:
                product_to_replace = random_object_dict[chosen_product_number]
        except:
            self.incorrect_entry_msg(max_key)
            product_to_replace = self.choose_product(random_object_dict)
        return product_to_replace

    def choose_replacement_product(self, product_to_replace,
                                   random_replacement_object_dict):
        """ view to choose one of the 3 best replacement product"""
        max_key = max(random_replacement_object_dict.keys())
        self.double_line_msg("les produits suivant appartiennent à la meme\n"
                             "categorie mais on un meilleur nutriscore que\n"
                             "{} (nutriscore {})"
                             .format(
                                self.limit_string_size(
                                    product_to_replace.product_name_fr),
                                product_to_replace.nutriscore_grade))
        for key, product in random_replacement_object_dict.items():
            print("{} : {} (nutriscore {})"
                  .format(
                    key,
                    self.limit_string_size(
                        product.product_name_fr),
                    product.nutriscore_grade))
        self.double_line_msg("Quel aliment voulez vous afficher ?")
        try:
            chosen_product_number = int(input())
            if chosen_product_number not in (
                    random_replacement_object_dict.keys()):
                self.incorrect_entry_msg(max_key)
                product_to_save = self.choose_replacment_product(
                    product_to_replace, random_replacement_object_dict)
            else:
                product_to_save = random_replacement_object_dict[
                                                        chosen_product_number]
        except:
            self.incorrect_entry_msg(max_key)
            product_to_save = self.choose_replacment_product(
                product_to_replace, random_replacement_object_dict)
        return product_to_save

    def no_replacement_product(self, product_to_replace):
        """ view if there is no replacement product"""
        self.double_line_msg(
            "désolé mais il n'existe pas de produit\n"
            "de remplacement dans cette categorie pour\n"
            "{} (nutriscore {})".format(
                self.limit_string_size(product_to_replace.product_name_fr),
                product_to_replace.nutriscore_grade))

    def save_chosen_replacement_product(self, product_A, product_B):
        """ view display the better replacement product and
            to ask if user want to save this product"""
        self.double_line_msg('vous pouvez remplacer')
        print('{} (nutriscore {})'.format(
            self.limit_string_size(product_A.product_name_fr),
            product_A.nutriscore_grade))
        self.double_line_msg('par :')
        print('   {} (nutriscore {})\n'
              "magasin ou l'acheter :\n   {}\n"
              "Lien vers la page d'Open Food Facts :\n   {}\n"
              .format(self.limit_string_size(product_B.product_name_fr),
                      product_B.nutriscore_grade,
                      product_B.stores,
                      product_B.url))

        self.double_line_msg('Voulez vous sauvergarder ce résultat ? (O/N)')
        try:
            need_to_save = input()
        except:
            self.incorrect_entry_msg_y_n()
            need_to_save = self.save_chosen_replacement_product(
                product_A, product_B)
        if need_to_save not in YES_NO_ANSWERS:
            self.incorrect_entry_msg_y_n()
            need_to_save = self.save_chosen_replacement_product(
                product_A, product_B)
        return need_to_save

    def display_favorites(self, favorite_objects_dict):
        """ view to display the favorites"""
        self.double_line_msg('liste des produits sauvegarés :')
        for object_product_S in favorite_objects_dict.keys():
            object_product_R_list = favorite_objects_dict[object_product_S]
            size = self.terminal_width() - 5
            print('\n' + ('-' * size))
            print('le produits :\n   {}\npeut etre remplacé par:'.format(
                self.limit_string_size(object_product_S.product_name_fr)))
            for product in object_product_R_list:
                print('   {}'
                      .format(self.limit_string_size(product.product_name_fr)))

    def incorrect_entry_msg_y_n(self):
        """ message for incorrect user answer"""
        size = self.terminal_width() - 5
        print('\n' * 100)
        print('\n' + ('#' * size))
        print("Votre reponse doit être la lettre O pour Oui ou N pour Non)")
        print(('#' * size) + '\n')

    def incorrect_entry_msg(self, number):
        """ message for incorrect user answer"""
        size = self.terminal_width() - 5
        print('\n' * 100)
        print('\n' + ('#' * size))
        print("Votre reponse doit être un chifre de 1 à {}".format(number))
        print(('#' * size) + '\n')

    def double_line_msg(self, msg):
        """ write message betwen 2 ligne"""
        size = self.terminal_width() - 5
        print('\n' + ('-' * size))
        print(msg)
        print(('-' * size) + '\n')

    def limit_string_size(self, string):
        """ cut string if it's too long"""
        size = self.terminal_width() - 30
        if len(string) > size:
            limited_string = string[:size] + '(...)'
        else:
            limited_string = string
        return limited_string

    def terminal_width(self):
        """get terminal size"""
        terminal_size = os.get_terminal_size()
        terminal_width = terminal_size.columns
        return terminal_width
