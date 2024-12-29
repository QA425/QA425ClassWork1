def display_personal_data(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['surname'])
    print(kwargs['age'])
    if 'phone' in kwargs:
        print(kwargs['phone'])


display_personal_data(name='Василий', surname='Иванов', age=35)
