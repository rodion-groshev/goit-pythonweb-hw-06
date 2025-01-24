from faker import Faker
from random import randint
from sqlalchemy import exc

from models import Student, Group, Grade, Teacher, Subject
from db_conn import session

students_number = 40
subjects_number = 7
grades_number = 19
teachers_number = 4


def generate_fake_data(
    students_number, subjects_number, teachers_number, grades_number
):
    group_options = [
        Group(name="Group A"),
        Group(name="Group B"),
        Group(name="Group C"),
    ]
    teachers_data = []
    subjects_data = []
    students_data = []
    grades_data = []

    fake_data = Faker()

    for _ in range(teachers_number):
        teachers_data.append(Teacher(name=fake_data.name()))

    for _ in range(subjects_number):
        subjects_data.append(
            Subject(name=fake_data.country_code(), teacher=teachers_data[randint(0, 3)])
        )

    for _ in range(students_number):
        students_data.append(
            Student(name=fake_data.name(), group=group_options[randint(0, 2)])
        )

    for student in students_data:
        for subject in subjects_data:
            for _ in range(grades_number):
                grades_data.append(
                    Grade(student=student, subject=subject, grade=randint(0, 100))
                )

    try:
        session.add_all(group_options)
        session.commit()
        session.add_all(teachers_data)
        session.commit()
        session.add_all(subjects_data)
        session.commit()
        session.add_all(students_data)
        session.commit()
        session.add_all(grades_data)
        session.commit()
    except exc.SQLAlchemyError as e:
        print(e)


if __name__ == "__main__":
    generate_fake_data(students_number, subjects_number, teachers_number, grades_number)
