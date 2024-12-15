my_str_alnum = 'Helloworld12345'
print(my_str_alnum.isalnum())

my_str_alnum = 'Helloworld'
print(my_str_alnum.isalnum())

my_str_alnum = '1234'
print(my_str_alnum.isalnum())
print()

my_str_alpha = "Helloworld"
print(my_str_alpha.isalpha())
my_str_alpha = "Helloworld123"
print(my_str_alpha.isalpha())
print()

my_str_digit = '1234567890546164'
print(my_str_digit.isdigit())
my_str_digit = '1234567890546164'
print(my_str_digit.isdigit())
print()

my_space_string = ' \n\t\r'
print(my_space_string)
print(my_space_string.isspace())
print()

my_str_alnum = 'Helloworld12345*_$'
print(not my_str_alnum.isalnum())
