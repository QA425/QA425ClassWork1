# counter = 0
# while counter < 5:
#     print("Inside Cycle")
#     counter += 1
#
# for i in range(5):
#     print("Inside range")
#
# some_list = ['item_1', 'item_2', 'item_3']
# for item in some_list:
#     print(item)

try:
    print('Провокация')
except:
    print("Исключение если провокация сработала")
else:
    print("Выполняем если исключения не было")
finally:
    print("Выполняем в любом случае")


def some_function():
    print("внутри функции")


class ExampleClass(object):

    def __init__(self, attr):
        self.attr = attr
        print("Внутри __init__")

    def some_method(self):
        print(self.attr)

    def __str__(self):
        return "Класс для примера по блокам выполнения"


my_object = ExampleClass('Some_Attr')
print(my_object)
