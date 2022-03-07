person = int(input('Enter number of quest:'))
cook_book = [
    ['салат',
     [
         ['картофель', 100, 'гр.'],
         ['морковь', 50, 'гр.'],
         ['огурцы', 50, 'гр.'],
         ['горошек', 30, 'гр.'],
         ['майонез', 70, 'мл.'],
     ]
     ],
    ['пицца',
     [
         ['сыр', 50, 'гр.'],
         ['томаты', 50, 'гр.'],
         ['тесто', 100, 'гр.'],
         ['бекон', 30, 'гр.'],
         ['колбаса', 30, 'гр.'],
         ['грибы', 20, 'гр.'],
     ],
     ],
    ['фруктовый десерт',
     [
         ['хурма', 60, 'гр.'],
         ['киви', 60, 'гр.'],
         ['творог', 60, 'гр.'],
         ['сахар', 10, 'гр.'],
         ['мед', 50, 'мл.'],
     ]
     ]
]

for dish in cook_book:
    for name_dish in dish[0:-1]:
        print()
        print(f'{name_dish.capitalize()}:') # выводим наименование блюда
        for name_dish in dish[1]:
            product = ''
            weight = 0
            unit = ''
            dish_parametrs = name_dish
            product = dish_parametrs[0]
            weight = dish_parametrs[1] * person
            unit = dish_parametrs[2]

            print(f'{product}, {weight}{unit}') # вывод общего кол-ва ингридиентов
