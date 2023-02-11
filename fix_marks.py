import argparse

from datacenter.models import Schoolkid, Mark

def fix_marks(schoolkid):
    schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid).first()
    if not schoolkid:
        print('Такой ученик не найден')
    else:
        Mark.objects.filter(schoolkid=schoolkid, points__lt=4).update(points=5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Исправление оценок ученика меньше 4 на 5')
    parser.add_argument('schoolkid', help='Ученик, оценки которого следует исправить (в формате экземпляра модели Schoolkid)')
    args = parser.parse_args()
    