import pytest

def get_result(score, attendance):
    if not isinstance(score, (int, float)):
        raise TypeError("Баллы должны быть числом")

    if not isinstance(attendance, (int, float)):
        raise TypeError("Посещаемость должна быть числом")

    if score < 0 or score > 100:
        return "Некорректный балл"

    if attendance < 0 or attendance > 100:
        return "Некорректная посещаемость"

    if score >= 90 and attendance >= 80:
        return "Отлично"

    if score >= 70 and attendance >= 70:
        return "Хорошо"

    if score >= 50 and attendance >= 60:
        return "Зачёт"

    return "Незачёт"



@pytest.mark.parametrize(
    "score, attendance, expected",
    [
        
        (90, 80, "Отлично"),
        (100, 100, "Отлично"),
        
        (70, 70, "Хорошо"),
        (89, 79, "Хорошо"),
        
        (50, 60, "Зачёт"),
        (69, 69, "Зачёт"),
        # Незачёт
        (49, 59, "Незачёт"),
        (0, 0, "Незачёт"),
        
        (-1, 80, "Некорректный балл"),
        (101, 80, "Некорректный балл"),
        
        (80, -1, "Некорректная посещаемость"),
        (80, 101, "Некорректная посещаемость"),
    ],
)
def test_get_result_parametrized(score, attendance, expected):
    assert get_result(score, attendance) == expected

@pytest.mark.parametrize(
    "score, attendance, match_msg",
    [
        ("90", 80, "Баллы должны быть числом"),
        (90, "80", "Посещаемость должна быть числом"),
        (None, 50, "Баллы должны быть числом"),
        (50, None, "Посещаемость должна быть числом"),
    ],
)
def test_get_result_type_errors(score, attendance, match_msg):
    with pytest.raises(TypeError, match=match_msg):
        get_result(score, attendance)