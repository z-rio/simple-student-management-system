from .models import Student

def get_all_students():
    return Student.objects.all()    

def count_students():
    return Student.objects.count()

def get_student_by_id(student_id):
    try:
        return Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return None

def create_student(name, email, age):
    return Student.objects.create(name=name, email=email, age=age)

def delete_student(student_id):
    student = get_student_by_id(student_id)
    if student:
        student.delete()
        return True
    return False

def search_student_by_name(name):
    return Student.objects.filter(name__icontains=name)


def update_student(student_id, name=None, email=None, age=None):
    student = get_student_by_id(student_id)
    if student:
        if name is not None:
            student.name = name
        if email is not None:
            student.email = email
        if age is not None:
            student.age = age
        student.save()
        return student
    return None