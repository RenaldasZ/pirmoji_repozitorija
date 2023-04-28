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
    student = {
        'name': name,
        'last_name': last_name,
        'age': age,
        'is_adult': age >= 18
    }
    with open('information.json', 'w') as file:
        json.dump(student, file)
    return student

name = input('Enter your name: ')
last_name = input('Enter your last name: ')
try:
    age = int(input('Enter your age: '))
except ValueError:
    print('Invalid input for age. Please enter a number.')
else:
    save_student_info(name, last_name, age)
