def display_my_space_address_mix(name: str, age: int = 35, city=None, *args, **kwargs):
    print(name)
    print(age)
    if city:
        print(city)
    for item in args:
        print(item)
    for k, v in kwargs.items():
        print(k, v)


display_my_space_address_mix('Дмитрий', 36, "Минск", "Беларусь", "Восточная Европа", planet='Earth', star='Sun')
display_my_space_address_mix('Петр')
