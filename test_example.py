import json
import logging
import datetime

logging.basicConfig(filename='logger.log', level=logging.INFO)

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logging.info(f"{datetime.datetime.now()}: {func.__name__}({args}, {kwargs}) = {result}")
            return result
        except Exception as e:
            logging.error(f"{datetime.datetime.now()}: {func.__name__}({args}, {kwargs}) raised an exception: {str(e)}")
            return None
    return wrapper

@error_handler
def save_student_info(name, last_name, age):
    try:
        with open('information.json', 'r') as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []

    for student in students:
        if student['name'] == name and student['last_name'] == last_name and student['age'] == age:
            print('This student already exists in the list.')
            return None

    student = {
        'name': name,
        'last_name': last_name,
        'age': age,
        'is_adult': age >= 18
    }
    students.append(student)
    with open('information.json', 'w') as file:
        json.dump(students, file)
    return student

def show_student_list():
    try:
        with open('information.json', 'r') as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    
    if not students:
        print("There are no students in the list.")
    else:
        print("List of students:")
        for student in students:
            print(f"Name: {student['name']}, Last name: {student['last_name']}, Age: {student['age']}, Is adult: {student['is_adult']}")

name = input('Enter your name: ')
last_name = input('Enter your last name: ')
try:
    age = int(input('Enter your age: '))
except ValueError:
    logging.warning(f"{datetime.datetime.now()} Klaida! : Invalid input for age. Please enter a number.")
    print('Invalid input for age. Please enter a number.')
else:
    save_student_info(name, last_name, age)
    
show_student_list()
