def new_sum(*args):
    print(args)
    sum_ = 0
    for num in args:
        sum_ += num
    return sum_


print(new_sum(2, 4, 5, 5, 7))
