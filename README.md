# Как установить.

1. Поместить файл main.py в корневую папку сайта.
2. Ввести в консоль команду `python manage.py shell`.
3. Открыть в текстовом редакторе файл main.py, скопировать содержимое.
4. Вставить содержимое файла main.py в консоль.

# Как пользоваться

Что-бы исправить отрицательные оценки введите команду :
```python
fix_marks("kid_name")
# Например
fix_marks("Леха пропусков")
```
Что-бы удалить все замечания введите в консоль команду :
```python
remove_chastisements("kid_name")
# Например
remove_chastisements("Кейт Лик")
```
Что-бы добавить похвалу от учителя введите в консоль команду :
```python
append_commendation("subject", "kid_name")
# Например
append_commendation("Математика", "Ке́плер Лавера́н")
```