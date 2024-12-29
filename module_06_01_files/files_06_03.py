def get_guests_count(filename):
    guest_count = 0
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line.rstrip())
                guest_count += 1
    except FileNotFoundError:
        return 'Файл не найден'
    return guest_count


guests_filename = r'files\guests.txt'
print(get_guests_count(guests_filename))
print()


def get_guests_count_readlines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            guest_list = file.readlines()
    except FileNotFoundError:
        return 'Файл не найден'
    return guest_list


guests_filename = r'files\guests.txt'
guests_list = get_guests_count_readlines(guests_filename)
for guest in guests_list:
    print(guest.rstrip())
print()

print(''.join(guests_list))
print(len(guests_list))
