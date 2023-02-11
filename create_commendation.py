import argparse
from django.core.exceptions import 

def create_commendation(name, subject):
    schoolkid = Schoolkid.objects.filter(full_name__contains=name).first()
    if not schoolkid:
        print('Такой ученик не найден')
    else:
        last_lesson = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=subject
        ).order_by('-date').first()
        if not last_lesson:
            print('Такой предмет не найден')
        else:
            Commendation.objects.create(
                text='Хвалю!',
                created=last_lesson.date,
                schoolkid=schoolkid,
                subject=last_lesson.subject,
                teacher=last_lesson.teacher
            )
	
	
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Создает положительный комментарий от учителя по последнему указанному предмету')
    parser.add_argument('name', help='ФИО ученика, которому следует создать рекомендацию (в формате строки)')
    parser.add_argument('subject', help='Предмет, по которому следует создать рекомендацию (в формате строки)')
    args = parser.parse_args()	
    