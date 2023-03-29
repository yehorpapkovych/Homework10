import json
import sys
import os

# if you need to create a json file, uncomment the lines below
# after the file is ready, comment these lines

# data_list = []
# with open('phonebook.json', 'w') as phonebook:
#   json.dump(data_list, phonebook)

phone = sys.argv[1]


# starter function
def choose():
    with open(phone, 'r') as phonebook:
        data = json.load(phonebook)

    print('To add new entries, press 1', '\nTo search by the first name, press 2',
          '\nTo search by the last name, press 3')
    print('To search by the full name, press 4', '\nTo search by the telephone number, press 5')
    print('To search by the city, press 6', '\nTo delete a record for a given telephone number, press 7')
    print('To update a record for a given telephone number, press 8', '\nTo exit the program, press 9 or anything else',
          '\n')
    for i in data:
        print(i, '\n')
    number = input('Press the number: ')
    if number == '1':
        add_new()
    elif number == '2':
        search_firstname()
    elif number == '3':
        search_lastname()
    elif number == '4':
        search_fullname()
    elif number == '5':
        search_number()
    elif number == '6':
        search_city()
    elif number == '7':
        delete()
    elif number == '8':
        update()
    else:
        print('\nThank you, goodbye!\n')


# to go back to menu
def goback():
    word = input('Press "Enter"')
    print()
    choose()


# adding new entries
def add_new():
    cont = {}
    while True:
        tel_num = input('Write the number: ')
        if tel_num.isdigit():
            cont['telephone number'] = tel_num
            break
        else:
            print('Try again!')
    cont['first name'] = input('Write the first name: ')
    cont['last name'] = input('Write the last name: ')
    cont['full name'] = input('Write the full name: ')
    cont['city'] = input('Write the city: ')
    with open(phone, 'r') as phonebook:
        data = json.load(phonebook)

    data.append(cont)

    with open(phone, 'w') as phonebook:
        json.dump(data, phonebook)

    goback()


# searching by the first name
def search_firstname():
    with open(phone, 'r') as phonebook:
        data = json.load(phonebook)

    firstname = input('Write the first name: ')
    for i in data:
        if i['first name'] == firstname:
            print(i)
            break
    goback()


# searching by the last name
def search_lastname():
    with open(phone, 'r') as phonebook:
        data = json.load(phonebook)

    lastname = input('Write the last name: ')
    for i in data:
        if i['last name'] == lastname:
            print(i)
            break
    goback()


# searching by the full name
def search_fullname():
    with open(phone, 'r') as phonebook:
        data = json.load(phonebook)

    fullname = input('Write the fullname name: ')
    for i in data:
        if i['full name'] == fullname:
            print(i)
            break
    goback()


# searching by the number
def search_number():
    with open(phone, 'r') as phonebook:
        data = json.load(phonebook)

    number = input('Write the number: ')
    for i in data:
        if i['telephone number'] == number:
            print(i)
            break
    goback()


# searching by the city
def search_city():
    with open(phone, 'r') as phonebook:
        data = json.load(phonebook)

    city = input('Write the city: ')
    for i in data:
        if i['city'] == city:
            print(i)
            break
    goback()


# deleting
def delete():
    number = input('Write the number to delete: ')
    with open(phone, 'r') as phonebook:
        data = json.load(phonebook)

    for i in data:
        if i['telephone number'] == number:
            data.remove(i)
            break

    with open(phone, 'w') as phonebook:
        json.dump(data, phonebook)
    goback()


# updating
def update():
    number = input('Write the number to update: ')
    with open(phone, 'r') as phonebook:
        data = json.load(phonebook)
    for i in data:
        if i['telephone number'] == number:
            print('To update the number, press 1', '\nTo update the first name, press 2',
                  '\nTo update the last name, press 3')
            print('To update the full name, press 4', '\nTo update the city, press 5')
            num = input('Press the number: ')
            if num == '1':
                n = input('Update the number: ')
                i['telephone number'] = n
            elif num == '2':
                n = input('Update the first name: ')
                i['first name'] = n
            elif num == '3':
                n = input('Update the last name: ')
                i['last name'] = n
            elif num == '4':
                n = input('Update the full name: ')
                i['full name'] = n
            elif num == '5':
                n = input('Update the city: ')
                i['city'] = n
            break

    with open(phone, 'w') as phonebook:
        json.dump(data, phonebook)
    goback()


if __name__ == '__main__':
    choose()
