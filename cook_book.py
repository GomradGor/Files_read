from pprint import pprint

import os

#  Ппрочитаем файл Recipes.txt
path = os.path.join(os.getcwd(), 'Recipes.txt')
with open(path) as cook_file:
    cook_book = {}  # Создаем пустой словарь для поваренной книги
    for string in cook_file:
        dish = string.strip()  # Выбираем из файла название блюда
        ingredients_count = int(cook_file.readline().strip())  # Выбираем из файла количество ингредиентов для блюда
        dish_dict = []  # Создаем пустой список для словарей с блюдами поваренной книги
        for item in range(ingredients_count):
            #  Выбираем из файла ингредиенты по разделителю '|'
            ingredient_name, quantity, measure = cook_file.readline().strip().split('|')
            #  Добавляем в список словари с ингредиентами
            dish_dict.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish] = dish_dict  #  Добавляем в поваренную книгу блюда и их ингредиенты
        cook_file.readline()  # Пропускаем пустую строку
    pprint(cook_book)


print()
print()
#  Создаем функцию для получения списка покупок исходя из заказанных блюд и количества персон
def get_shop_list_by_dishes(dishes, person_count):
    dish_dict = {}  # Создаем пустой словарь для хранения списка покупок
    for dish in dishes:
        for ingredient in cook_book[dish]:  # Выбираем ингредиенты для блюд из поваренной книги
            #  Добавляем ингредиеты, увеличивая их количество на число персон
            ingredient_list = dict([(ingredient['ingredient_name'],
                                     {'quantity': int(ingredient['quantity']) * person_count,
                                      'measure': ingredient['measure']})])
            if dish_dict.get(ingredient['ingredient_name']) == 'None':
                merger = (int(dish_dict[ingredient['ingredient_name']]['quantity']) +
                           int(ingredient_list[ingredient['ingredient_name']]['quantity']))
                dish_dict[ingredient['ingredient_name']]['quantity'] = merger
            else:
                dish_dict.update(ingredient_list)
    return dish_dict


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3))