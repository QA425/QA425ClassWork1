square_list = [i * i for i in range(11) if i % 2 == 0]
print(square_list)

square_list_1 = []
for i in range(11):
    if i % 2 == 0:
        square_list_1.append(i * i)
print(square_list_1)

customers = ['Bob', 'Joe', 'Anna', 'Bob', 'Nick']
customers_filtered = [customer for customer in customers if customer != 'Bob' and customer != 'Joe']
print(customers_filtered)

customers_1 = ['Bob', 'Joe', 'Anna', 'Bob', 'Nick']
customers_filtered_1 = []
for customer in customers_1:
    if customer != 'Bob' and customer != 'Joe':
        customers_filtered_1.append(customer)
print(customers_filtered_1)

product_list = [x * y for x in range(1, 4) for y in range(1, 4)]

product_list_1 = []
for y in range(1, 4):
    for x in range(1, 4):
        product_list_1.append(x * y)
print(product_list_1)

my_matrix = [[x * y for x in range(1, 4)] for y in range(1, 5)]
print(my_matrix)
