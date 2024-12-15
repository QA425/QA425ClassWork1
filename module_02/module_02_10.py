# car_speed = 100
# if car_speed > 50:
#     print('Машина движется быстрее 50 км/ч')
#
#
# car_speed = 120
# motorcycle_speed = 120
# if car_speed > motorcycle_speed:
#     print('Машина движется быстрее мотоцикла км/ч')
# elif car_speed < motorcycle_speed:
#     print('Мотоцикл движется быстрее машины')
# else:
#     print('Скорости равны')

car_speed = 150
motorcycle_speed = 120
if car_speed > motorcycle_speed:
    print('Машина движется быстрее мотоцикла км/ч')
    motorcycle_speed += 50
if car_speed < motorcycle_speed:
    print('Мотоцикл движется быстрее машины')
else:
    print('Скорости равны')
print()

car_speed = 100
motorcycle_speed = 120
if car_speed > motorcycle_speed:
    print('Машина движется быстрее мотоцикла км/ч')
    motorcycle_speed += 50
elif car_speed < motorcycle_speed:
    print('Мотоцикл движется быстрее машины')
else:
    print('Скорости равны')
