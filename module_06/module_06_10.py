def get_total_check(prices, tip=0):
    temp_total = sum(prices)
    total = temp_total * (100 + tip) / 100
    return total


total_0 = get_total_check([1000, 3000, 5000])
print(total_0)

total_10 = get_total_check([1000, 3000, 5000], 10)
print(total_10)

total_10 = get_total_check([1000, 3000, 5000], tip=10)
print(total_10)
