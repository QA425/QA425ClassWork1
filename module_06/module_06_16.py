def display_planet_space_address(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)


display_planet_space_address(planet="Земля", star="Солнце", galaxy="Млечный путь", age=round(4.543e9))
