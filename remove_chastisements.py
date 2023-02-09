import argparse

def remove_chastisements(schoolkid):
    chastisement = Chastisement.objects.filter(schoolkid=schoolkid).get()
    chastisement.delete()
	
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Удаление записей с замечаниями ученика')
    parser.add_argument('schoolkid', help='Ученик, замечания которого следует удалить (в формате экземпляра модели Schoolkid)')
    args = parser.parse_args()
    