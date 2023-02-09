# hack_tool

Набор скриптов для изменения данных в электронном журнале

## create_commendation.py

Создает похвалу по указанному предмету у указанного ученика.

Требуемые аргументы:

- `name` - ФИО ученика, которому следует создать рекомендацию (в формате строки)
- `subject` - предмет, по которому следует создать рекомендацию (в формате строки)

## remove_chastisements.py

Удаляет все замечания у указанного ученика.

Требуемые аргументы:

- `schoolkid` - Ученик, замечания которого следует удалить (в формате экземпляра модели Schoolkid)

## fix_marks.py

Исправляет оценки меньше 4 на 5 у указанного ученика.

Требуемые аргументы:

- `schoolkid` - Ученик, оценки которого следует исправить (в формате экземпляра модели Schoolkid)