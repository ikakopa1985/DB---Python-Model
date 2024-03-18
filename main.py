from employee import Employee
from db import conn


first_user = Employee("zaza", "ksdaokoze", "34")
first_user.save()

print(Employee.get_list(name='gio', surname='kokoze'))
print(Employee.get_list())

nana = Employee("nana", "kilopa", "30")
nana.save()
eka = Employee("eka", "kankava", "29")
eka.save()
print(nana < eka)

Employee.delete(14)

first_user = Employee.get(1)
if first_user is None:
    first_user = Employee("name", "surname", "age")
    first_user.save()

# first_user.name = "Tornike"
# first_user.save()

conn.commit()
conn.close()
