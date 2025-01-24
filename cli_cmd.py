from argparse import ArgumentParser
import logging
from db_conn import session
from models import Student, Group, Teacher, Subject, Grade


logger = logging.getLogger()
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)

logger.addHandler(ch)

parser = ArgumentParser()
parser.add_argument("-a", "--action")
parser.add_argument("-m", "--model")
parser.add_argument("-n", "--name")
parser.add_argument("--id")
parser.add_argument("--group_id")
parser.add_argument("--teacher_id")
parser.add_argument("--subject_id")
parser.add_argument("--student_id")
parser.add_argument("--grade")
args = parser.parse_args()
print(args)


def create(data):
    session.add(data)
    session.commit()
    if hasattr(data, "name"):
        logger.info(f"{data.name} added")
    else:
        logger.info(f"{data.grade} added to {data.student_id}")


def read(data):
    result = session.query(data).all()
    if hasattr(data, "name"):
        for res in result:
            logger.info(f"Name: {res.name} | ID: {res.id}")
    else:
        for res in result:
            logger.info(f"Name: {res.grade} | ID: {res.id}")


def update(data, get_id, new_data):
    get_record = session.query(data).get(get_id)
    if hasattr(data, "name"):
        get_record.name = new_data
        session.commit()
        logger.info(f"Record ID: {get_id} updated to name '{new_data}'.")
    else:
        get_record.grade = new_data
        session.commit()
        logger.info(f"Record ID: {get_id} updated to name '{new_data}'.")


def delete_record(data, get_id):
    get_record = session.query(data).get(get_id)
    session.delete(get_record)
    session.commit()
    logger.info(f"Record ID: {get_id} deleted.")


if args.action == "create":
    if args.model == "Student":
        create(Student(name=args.name, group_id=int(args.group_id)))
    elif args.model == "Teacher":
        create(Teacher(name=args.name))
    elif args.model == "Group":
        create(Group(name=args.name))
    elif args.model == "Subject":
        create(Subject(name=args.name, teacher_id=args.teacher_id))
    elif args.model == "Grade":
        create(
            Grade(
                grade=args.grade, student_id=args.student_id, subject_id=args.subject_id
            )
        )
elif args.action == "list":
    if args.model == "Student":
        read(Student)
    elif args.model == "Teacher":
        read(Teacher)
    elif args.model == "Group":
        read(Group)
    elif args.model == "Subject":
        read(Subject)
    elif args.model == "Grade":
        read(Grade)

elif args.action == "update":
    if args.model == "Student":
        update(Student, args.id, args.name)
    elif args.model == "Teacher":
        update(Teacher, args.id, args.name)
    elif args.model == "Group":
        update(Group, args.id, args.name)
    elif args.model == "Subject":
        update(Subject, args.id, args.name)
    elif args.model == "Grade":
        update(Grade, args.id, args.grade)

elif args.action == "delete":
    if args.model == "Student":
        delete_record(Student, args.id)
    elif args.model == "Teacher":
        delete_record(
            Teacher,
            args.id,
        )
    elif args.model == "Group":
        delete_record(Group, args.id)
    elif args.model == "Subject":
        delete_record(Subject, args.id)
    elif args.model == "Grade":
        delete_record(Grade, args.id)
