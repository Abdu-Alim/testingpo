from student_service import add_student

def test_add_student():
    student = add_student(
        "Alim",
        "Shirakhunov",
        20,
        85
    )

    assert student['name'] == "Alim"
    assert student['surname'] == "Shirakhunov"
    assert student['age'] == 20
    assert student['score'] == 85