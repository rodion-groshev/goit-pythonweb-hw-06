from db_conn import session
from models import Student, Teacher, Subject, Grade, Group
from sqlalchemy.sql import func

student_id = Student.id
student_name = Student.name
grade = Grade.grade
subject_name = Subject.name
group_name = Group.name
teacher_name = Teacher.name


def select_1():
    return (
        session.query(student_name, func.avg(grade))
        .join(Grade)
        .group_by(student_id)
        .order_by(func.avg(grade).desc())
        .limit(5)
    )


def select_2():
    return (
        session.query(Student.name, func.avg(grade))
        .join(Grade)
        .join(Subject)
        .filter(subject_name == "TV")
        .group_by(student_id)
        .order_by(func.avg(grade).desc())
        .first()
    )


def select_3():
    return (
        session.query(group_name, func.avg(grade))
        .select_from(Group)
        .join(Student)
        .join(Grade)
        .join(Subject)
        .filter(subject_name == "TV")
        .group_by(Group.id)
    )


def select_4():
    return session.query(func.avg(grade))


def select_5():
    return (
        session.query(subject_name).join(Teacher).filter(teacher_name == "Shaun Reese")
    )


def select_6():
    return session.query(student_name).join(Group).filter(group_name == "Group A")


def select_7():
    return (
        session.query(student_name, grade, group_name)
        .join(Grade)
        .join(Group)
        .filter(group_name == "Group A")
    )


def select_8():
    return (
        session.query(func.avg(grade))
        .select_from(Grade)
        .join(Subject)
        .join(Teacher)
        .filter(teacher_name == "Shaun Reese")
        .scalar()
    )


def select_9():
    return (
        session.query(subject_name)
        .join(Grade)
        .join(Student)
        .filter(student_name == "Frank Taylor")
        .group_by(subject_name)
    )


def select_10():
    return (
        session.query(subject_name)
        .join(Grade)
        .join(Student)
        .join(Teacher)
        .filter(student_name == "Frank Taylor", teacher_name == "Shaun Reese")
        .group_by(subject_name)
    )


if __name__ == "__main__":
    result = select_10()
    for stud in result:
        print(stud)

    result_8 = select_8()
    print(result_8)
    session.close()
