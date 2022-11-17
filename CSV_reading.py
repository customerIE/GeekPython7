import csv
def reading_csv():
    print('Введите фамилию:')
    b = input()
    with open (f'Phonebook.csv', 'r', encoding = 'utf-8') as csv_file:
        data = list(csv.reader(csv_file))
        for i in range(len(data)):
            if b == data[i][0]:
                print(data[i])
    return 
 
  