from v7.school.people.people import People


class Student(People):

    def __init__(self, name, student_id):
        People.__init__(self, name)
        self.student_id = student_id

    def introduction(self):
        return f"Student: {self.name}\tStudent id:{self.student_id}"
