import django
import os

def calculate_closest_deptid(house_id):
    from distance.models import Distance
    distance_set = Distance.objects.raw('SELECT * FROM distance_distance WHERE distance_distance.house_id_id = %s ORDER BY distance_distance.distance ASC',[house_id])
    for item in distance_set:
        return_id = item.department_id.id
        return float(return_id)
    return -1.0

if __name__ == "__main__":
	os.sys.path.append('../..')
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")
	django.setup()
	from housing.models import House
	all_houses = House.objects.all()
	for item in all_houses:
		closest_dept_id = calculate_closest_deptid(house_id=item.id)
		item.closest_department_float = closest_dept_id
		item.save()
		print("finished calcualtion of house_id = %d", item.id)
	print("finished calculation")