from model import get_info as info

def read_contact():
    with open('Phonebook.csv', encoding ='utf=8') as f:
        return f.read()

def writing_scv (info):
    file = 'phonebook.csv'
    with open (file, 'a', encoding ='utf-8') as data:
        data.write(f'Фамилия: {info[0]}; Имя: {info[1]}; Отчество: {info[2]}; Номер телефона: {info[3]}; Описание: {info[4]}\n')

def writing_txt (info):
    file = 'phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n Имя: {info[1]}\n Отчество: {info[2]}\n Номер телефона: {info[3]}\n Описание: {info[4]}\n\n')