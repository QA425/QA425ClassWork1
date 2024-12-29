import random


def get_random_genre(category: str, categories_matrix: list):
    if category.lower() == "кино":
        return random.choice(categories_matrix[0])
    elif category.lower() == "книги":
        return random.choice(categories_matrix[1])
    elif category == "игры":
        return random.choice(categories_matrix[2])
    else:
        return f"Не знаю такой категории: {category}"


if __name__ == '__main__':
    cinema_genres = ["Драма", "Комедия", "Фэнтези", "Ужасы"]
    book_genres = ["Поэма", "Водевиль", "Роман", "Проза"]
    game_genres = ["Симулятор", "Аркада", "RPG", "Инди"]
    my_categories_matrix = [cinema_genres, book_genres, game_genres]

    user_choice = input("Введите категорию жанра: ")
    while user_choice.lower() not in ['stop', 'стоп']:
        my_genre = get_random_genre(user_choice, my_categories_matrix)
        print(my_genre)
        user_choice = input("Введите категорию жанра: ")
