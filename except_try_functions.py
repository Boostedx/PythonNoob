try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(risk)
except ZeroDivisionError:
    print('Age cannot be equal to 0.')
except ValueError:
    print('Invalid value')


