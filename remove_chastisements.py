import argparse

from datacenter.models import Schoolkid, Chastisement

def remove_chastisements(schoolkid):
    schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid).first()
    if not schoolkid:
        print('Такой ученик не найден')
    else:
        chastisement = Chastisement.objects.filter(schoolkid=schoolkid).all()
        if not chastisement:
            print('Замечаний не найдено')
        else:
            chastisement.delete()
	
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Удаление записей с замечаниями ученика')
    parser.add_argument('schoolkid', help='Ученик, замечания которого следует удалить (в формате строки)')
    args = parser.parse_args()
    