import random

number = random.randint(1, 100)
attempts = 0
print("Угадайте число от 1 до 100! - lolik.py:5")

while True:
    guess = int(input("Ваша попытка: "))
    attempts += 1
    
    if guess == number:
        print(f"Поздравляем! Угадали за {attempts} попыток! - lolik.py:12")
        break
    elif guess < number:
        print("Больше! - lolik.py:15")
    else:
        print("Меньше! - lolik.py:17")