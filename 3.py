students = [
    {'name': 'Иван', 'languages': {'английский', 'испанский'}},
    {'name': 'Анна', 'languages': {'русский', 'китайский', 'английский'}},
    {'name': 'Сергей', 'languages': {'английский', 'немецкий'}},
    {'name': 'Ольга', 'languages': {'китайский', 'французский'}},
    {'name': 'Дмитрий', 'languages': {'английский', 'китайский', 'португальский'}}
]
all_languages = set()
for student in students:
    all_languages.update(student['languages'])
print("Различные языки, известные студентам:")
for lang in sorted(all_languages):
    print(lang)
chinese_knowers = [student['name'] for student in students if 'китайский' in student['languages']]
print("\nСтуденты, знающие китайский язык:")
for student in chinese_knowers:
    print(student)
