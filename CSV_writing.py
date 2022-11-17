import csv
import Contact_info as ci
def writing_csv ():
    lst = ci.contact_field()
    with open (r'Phonebook.csv', 'a', encoding = 'utf-8') as csv_file:
        data = csv.writer(csv_file, lineterminator="\n")
        #data.writeheader()
        data.writerow(lst)
    