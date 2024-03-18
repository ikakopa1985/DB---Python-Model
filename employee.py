from db import c


class Employee(object):
    def __init__(self, name, surname, age, pk=None):
        self.id = pk
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    def get(cls, pk):
        result = c.execute("SELECT * FROM employee WHERE id = ?", (pk,))
        values = result.fetchone()
        if values is None:
            return None
        employee = Employee(values["name"], values["surname"], values["age"], values["id"])
        return employee

    @classmethod
    def get_list(cls, **args):
        res_all = []
        if len(args.items()) == 0:
            result = c.execute('SELECT * FROM employee')
        else:
            result = c.execute(f'SELECT * FROM employee WHERE {list(args.items())[0][0]} = "{list(args.items())[0][1]}"'
                               f' AND {list(args.items())[1][0]} = "{list(args.items())[1][1]}"')
        values = result.fetchall()
        for item in values:
            res_all.append(Employee(item["name"], item["surname"], item["age"], item["id"]))
        return res_all

    def __repr__(self):
        return f"<Employee {self.id}, {self.name}, {self.surname}, {self.age}>"

    def update(self):
        c.execute("UPDATE employee SET name = ?, surname = ?, age = ? WHERE id = ?",
                  (self.name, self.surname, self.age, self.id))

    def create(self):
        c.execute("INSERT INTO employee (name, surname, age) VALUES (?, ?, ?)", (self.name, self.surname, self.age))
        self.id = c.lastrowid

    @classmethod
    def delete(cls, pk):
        result = c.execute("SELECT * FROM employee WHERE id = ?", (pk,))
        values = result.fetchone()
        if values is None:
            return None
        else:
            c.execute(f'DELETE FROM employee WHERE id = {pk}')

    def save(self):
        if self.id is not None:
            self.update()
        else:
            self.create()
        return self

    def __gt__(self, other):
        this_age = c.execute(f'SELECT * FROM employee WHERE id = {self.id}').fetchone()['age']
        other_age = c.execute(f'SELECT * FROM employee WHERE id = {other.id}').fetchone()['age']
        if this_age > other_age:
            return True
        else:
            return False

    def __eq__(self, other):
        this_age = c.execute(f'SELECT * FROM employee WHERE id = {self.id}').fetchone()['age']
        other_age = c.execute(f'SELECT * FROM employee WHERE id = {other.id}').fetchone()['age']
        if this_age == other_age:
            return True
        else:
            return False

    def __lt__(self, other):
        this_age = c.execute(f'SELECT * FROM employee WHERE id = {self.id}').fetchone()['age']
        other_age = c.execute(f'SELECT * FROM employee WHERE id = {other.id}').fetchone()['age']
        if this_age < other_age:
            return True
        else:
            return False
