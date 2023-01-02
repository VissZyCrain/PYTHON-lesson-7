def get_info ():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    middle_name = input('Введите отчество: ')
    info.append(middle_name)
    phone_number = input('Введите номер телефона: ')
    info.append(phone_number)
    decription = input('Введите описание: ')
    info.append(decription)
    return info