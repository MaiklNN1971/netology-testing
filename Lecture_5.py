documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "passport", "number": "1207 876234", "name": "Василий Петров"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': ['2222']
}

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
#  Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
def name_person(document):
    number_doc = input('Введите номер документа: ')

    for doc in document:
        name_people = ''
        if doc['number'] == number_doc:
            name_people = doc['name']
            return (f' Данный документ принадлежит: {name_people}')

    if name_people == '':
        return ('Документа с таким номером нет')

# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
def number_shelf(list_directories):
    number_doc = input('Введите номер документа: ')
    for number_shelf, number_doc1 in list_directories.items():
        number = ''
        for number1 in number_doc1:
            if number1 == number_doc:
                number = number_shelf
                return (f'Документ находится на полке № {number}')
    if number =='':
        return ('Документа с таким номером нет')

#-----------------------------------------------------------

def find_shelf(number, directories):
        res = 'Документ не найден в базе'
        for i in directories:
            if number in directories[i]:
                res = 'Документ хранится на полке: ' + i
        return res
#-----------------------------------------------------------


#     l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
def list_doc(document):
    for doc in document:
        print (f'''{doc['type']} "{doc['number']}" "{doc['name']}"''')

#     a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки,
#     на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
def add_new_doc(doc,dir):
    num_doc = input('Введите номер документа:')
    type_doc = input('Введите тип документа:')
    name_doc = input('Введите имя владельца:')
    num_shelf = input('Введите номер полки:')

    res = 'Такой полки нет'
    for i in dir:
        print('i==',type(i),'````','num_shelf==',type(num_shelf))
        print(i,'---',num_shelf)
        print('dir[i]=',dir[i])
        if num_shelf in dir:
            doc.append({'type': type_doc, 'number': num_doc, 'name': name_doc})
            dir[num_shelf].append(num_doc)
            res = 'Добавлен новый документ: '
            return res
    return res


def main():
    while True:
        user_input = input('Введите команду (возможные варианты: p, s, l, a): ')
        if user_input == 'p':
            print(name_person(documents))
        elif user_input == 's':
            number_s = input('введите номер документа:')
            print(find_shelf(number_s, directories))
            # print(number_shelf(directories))
        elif user_input == 'l':
            list_doc(documents)
        elif user_input == 'a':
           print(add_new_doc(documents, directories))
        elif user_input == 'q':
            print('Работа закончена.')
            break
        else:
            print('не верная команда!')


main()