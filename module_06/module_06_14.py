def remove_from_string(string, *args):
    print(string)
    print(args)

    for symbol in args:
        string = string.replace(symbol, '')

    return string


print(remove_from_string('О! Смотри, можно удалить все знаки: препинания сразу?', '!', ',', ':', '?'))
