import pytest
from bank_limit import calculate_free
@pytest.mark.parametrize(
    "amount, expected_free, description",
    [
        (0, 0.0, "Нижняя граница, бесплатной зоны"),
        (500, 0.0, "В пределах бесплатной зоны"),
        (1000, 0.0, "Верхняя граница бесплатной зоны"),

        (1001, 10.01, "Нижняя граница платной зоны"),
        (50000, 500.0, "Верхняя граница платной зоны"),
        (25000, 250.0, "В пределах платной зоны"),
        (50001, -2.0, "Выход за верхнюю границу платной зоны"),
        (100000, -2.0, "Выход за верхнюю границу платной зоны"),
        (-1, -1.0, "Выход за нижнюю границу бесплатной зоны")
    ],

    ids = lambda amount, expected_free, description: f'Amount_({amount}_description_{description.replace("","_")})'
    
)

def test_free_matrix(amount, expected_free, description):
    assert calculate_free(amount) == expected_free
def test_invalid_type_exception():
    with pytest.raises(TypeError):
        calculate_free("invalid_type")