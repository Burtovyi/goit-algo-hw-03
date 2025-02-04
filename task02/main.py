import turtle

def koch_curve(t, length, level):
    """
    Функція малює одну сторону кривої Коха.
    :param t: об'єкт Turtle
    :param length: довжина відрізка
    :param level: рівень рекурсії
    """
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        # Малюємо перший сегмент
        koch_curve(t, length, level - 1)
        t.left(60)
        # Малюємо сегмент, що утворює «хвильку»
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        # Малюємо останній сегмент
        koch_curve(t, length, level - 1)

def draw_koch_snowflake(t, length, level):
    """
    Функція малює сніжинку Коха, що складається з трьох кривих Коха.
    :param t: об'єкт Turtle
    :param length: довжина кожної сторони сніжинки
    :param level: рівень рекурсії
    """
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

def main():
    # Запит рівня рекурсії від користувача
    try:
        level = int(input("Введіть рівень рекурсії для сніжинки Коха (наприклад, 0, 1, 2, 3, ...): "))
    except ValueError:
        print("Введіть ціле число для рівня рекурсії.")
        return

    # Ініціалізація Turtle
    t = turtle.Turtle()
    t.speed(0)  # Найвища швидкість малювання
    t.hideturtle()  # Приховуємо стрілку для більш чистого вигляду

    # Налаштування екрану
    screen = turtle.Screen()
    screen.title("Сніжинка Коха")

    # Розташування для початку малювання (можна налаштувати за бажанням)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    length = 400  # Довжина сторони сніжинки

    # Малювання сніжинки
    draw_koch_snowflake(t, length, level)

    # Очікування кліку для закриття вікна
    screen.exitonclick()

if __name__ == '__main__':
    main()
