import argparse

def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
    for mark in bad_marks:
        mark.points = 5
        mark.save()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Исправление оценок ученика меньше 4 на 5')
    parser.add_argument('schoolkid', help='Ученик, оценки которого следует исправить (в формате экземпляра модели Schoolkid)')
    args = parser.parse_args()
    