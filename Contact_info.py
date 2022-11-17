def contact_field ():
    lst1 = []
    last_name = input('Введите фамилию: ')
    lst1.append(last_name)
    first_name = input('Введите имя: ')
    lst1.append(first_name)
    phone_numb = ''
    valid =False
    while not valid:
        try:
            phone_numb = input('Введите номер телефона: ')
            if len(phone_numb) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_numb = int(phone_numb)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    lst1.append(phone_numb)
    type_numb = input('Введите описание: ')
    lst1.append(type_numb)
    return lst1