def check_guess(secret_number, user_guess):
    """
    Проверяет число.
    Возвращает:
    - 'win', если число угадано
    - 'less', если загаданное число МЕНЬШЕ попытки пользователя
    - 'bigger', если загаданное число БОЛЬШЕ попытки пользователя
    """
    if user_guess == secret_number:
        return 'win'
    elif user_guess > secret_number:
        return 'less'
    else:
        return 'bigger'