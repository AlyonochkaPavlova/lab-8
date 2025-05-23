capitals = {
    'Россия': 'Москва',
    'Великобритания': 'Лондон',
    'Франция': 'Париж',
    'Германия': 'Берлин',
    'Италия': 'Рим',
    'Испания': 'Мадрид',
    'Китай': 'Пекин',
    'Япония': 'Токио',
    'Индия': 'Нью-Дели',
    'Канада': 'Оттава'
}
print("Все пары страна-столица:")
for country, city in capitals.items():
    print(f'{country} : {city}')
search_country = input("Введите название страны, чтобы узнать её столицу: ")
capital = capitals.get(search_country, "Такую страну не нашли")
print(f'Столица {search_country}: {capital}')
print("\nОтсортированные пары страна-столица:")
for country, city in sorted(capitals.items()):
    print(f'{country} : {city}')
