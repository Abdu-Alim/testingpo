import random
from game_logic import check_guess

def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = 7
    
    print("Угадай число от 1 до 100! У тебя есть 7 попыток.")
    
    for attempt in range(1, max_attempts + 1):
        print(f"\nПопытка № {attempt} из {max_attempts}")
        
        try:
            user_guess = int(input("Введите число: "))
        except ValueError:
            print("Число должно быть целым!")
            continue
            
        result = check_guess(secret_number, user_guess)
        
        if result == "win":
            print(f"Ты угадал число с {attempt}-й попытки!")
            break
        elif result == "less":
            print("Меньше!")
        elif result == "bigger":
            print("Больше!")
            
    else:
        print(f"\Ты исчерпал все попытки. Загаданное число было: {secret_number}")

if __name__ == "__main__":
    play_game()


    # 50
    #_____________________________________________________________________________________________________________________________
    # 25
    # 75
    #_____________________________________________________________________________________________________________________________
    # 12.5
    # 37.5
    #_____________________________________________________________________________________________________________________________
    # 62.5
    # 87.5
