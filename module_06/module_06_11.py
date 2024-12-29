def get_total_paint(width, height, consumption=0.2, layers=2):
    total_paint = width * height * consumption * layers
    return round(total_paint, 2)


print(f"Итого литров краски: {get_total_paint(3, 4)}")
print(f"Итого литров краски: {get_total_paint(3, 4, 0.4)}")
print(f"Итого литров краски: {get_total_paint(3, 4, 0.4, 3)}")
print(f"Итого литров краски: {get_total_paint(3, 4, 0.2, 3)}")
print(f"Итого литров краски: {get_total_paint(width=3, height=4, layers=3)}")
print(f"Итого литров краски: {get_total_paint(width=3, height=4, layers=3, consumption=0.3)}")

my_layers = 3
my_consumption = 0.4

# my_consumption = 0.4
# my_layers = 3
