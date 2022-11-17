import CSV_writing as writing
import CSV_reading as reading
print('Выберите действие:')
print('Найти номер - 1')
print('Создать контакт - 2')
a = int(input())
if a==1:
    reading.reading_csv()
elif a==2:
    writing.writing_csv()
