def display_my_space_address(*args, **kwargs):
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(key, value)


display_my_space_address('Дмитрий', 35, planet='Earth', star='Sun')
