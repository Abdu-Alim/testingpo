from student_service import (
    add_student, get_student, update_student, delete_student
)

def clear_students():
    students.clear()

def test_add_student():
    clear_students()
    add_student("Abdu-Alim", "Shirakhunov", 20, 85)

    assert students['name'] == "Abdu-Alim"
    assert students['surname'] == "Shirakhunov"
    assert students['age'] == 20
    assert students['score'] == 85

    assert len(students) == 1

def test_invalid_age():
    clear_students()

    try:
        add_student("Abdu-Alim", "Shirakhunov", 10, 85)
        assert False, "Expected ValueError for invalid age"
    except ValueError:
        assert True

def test_invalid_score():
    clear_students()

    try:
        add_student("Abdu-Alim", "Shirakhunov", 20, 250)
        assert False, "Expected ValueError for invalid score"
    except ValueError:
        assert True

def test_update_student():
    clear_students()

    student = add_student("Petr", "Petrov", 20, 85)
    updated = update_student(student['id'], "Petr", "Petrov", 25, 95)

    assert updated['name'] == "Petr"
    assert updated['surname'] == "Petrov"
    assert updated['age'] == 25
    assert updated['score'] == 95

def test_delete_student():
    clear_students()

    student = add_student("Ivan", "Ivanov", 20, 85)

    result = delete_student(student['id'])
    assert result is True
    assert len(students) == 0