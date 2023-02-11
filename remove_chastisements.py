import argparse

from datacenter.models import Schoolkid, Chastisement

def remove_chastisements(schoolkid):
    schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid).first()
    if not schoolkid:
        return print('Такой ученик не найден')
    chastisement = Chastisement.objects.filter(schoolkid=schoolkid).all()
    if not chastisement:
        return print('Замечаний не найдено')
    chastisement.delete()
	
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Удаление записей с замечаниями ученика')
    parser.add_argument('schoolkid', help='Ученик, замечания которого следует удалить (в формате строки)')
    args = parser.parse_args()
    