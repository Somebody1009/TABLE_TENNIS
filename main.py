from turtle import Screen, Turtle  # Імпортуємо класи Screen і Turtle з модуля turtle
from paddle import Paddle  # Імпортуємо клас Paddle з модуля paddle
from ball import Ball  # Імпортуємо клас Ball з модуля ball
from scoreboard import Scoreboard  # Імпортуємо клас Scoreboard з модуля scoreboard
from interface import setup_menu, is_running, is_paused, register_bounce, update_timer_display, update_speed_display, draw_status, update_bounce_display  # Імпортуємо функції для графічного інтерфейсу
import time  # Імпортуємо модуль для роботи з часом
import random  # Імпортуємо модуль для генерації випадкових чисел

LEVEL = 0  # Початковий рівень гри
NUM_BALLS = 0  # Кількість м'ячів на полі
balls = []  # Список об'єктів Ball
recent_bounces = []  # Список для відстеження нещодавніх відбивань м'ячів

screen = Screen()  # Створюємо вікно для гри
screen.bgcolor("black")  # Встановлюємо чорний фон
screen.setup(width=800, height=600)  # Встановлюємо розміри вікна
screen.title("Pong")  # Встановлюємо заголовок вікна
screen.tracer(0)  # Вимикаємо автоматичне оновлення екрана

selector = Turtle()  # Створюємо черепашку для відображення меню вибору
selector.hideturtle()  # Ховаємо її вигляд
selector.color("white")  # Встановлюємо білий колір пера
selector.penup()  # Піднімаємо перо, щоб не залишати ліній при русі
selector.goto(0, 0)  # Переміщуємося в центр екрана
selector.write("Вибери рівень: [1], [2], або [3]", align="center", font=("Courier", 20, "normal"))  # Виводимо текст меню

r_paddle = Paddle((350, 0))  # Створюємо праву ракетку
l_paddle = Paddle((-350, 0))  # Створюємо ліву ракетку
scoreboard = Scoreboard()  # Створюємо табло для рахунку

def start_level(level):  # Функція для запуску гри на заданому рівні
    global LEVEL, NUM_BALLS, balls, recent_bounces  # Використовуємо глобальні змінні
    LEVEL = level  # Зберігаємо обраний рівень
    NUM_BALLS = LEVEL  # Кількість м'ячів відповідає рівню
    selector.clear()  # Очищаємо текст меню

    balls = [Ball() for _ in range(NUM_BALLS)]  # Створюємо список м'ячів
    start_x, start_y = 0, 0  # Початкова позиція м'ячів
    balls[0].goto(start_x, start_y)  # Ставимо перший м'яч у центр
    for i in range(1, NUM_BALLS):  # Для решти м'ячів
        balls[i].goto(start_x, start_y)  # Теж у центр
        balls[i].x_move = random.choice([-1, 1]) * (2 + random.random() * 2)  # Випадковий рух по x
        balls[i].y_move = random.choice([-1, 1]) * (2 + random.random() * 2)  # Випадковий рух по y

    recent_bounces = [False] * NUM_BALLS  # Ініціалізуємо список бульовими значеннями

    screen.listen()  # Активуємо прослуховування клавіш
    screen.onkey(r_paddle.go_up, "Up")  # Призначаємо стрілку вгору для правої ракетки
    screen.onkey(r_paddle.go_down, "Down")  # Стрілку вниз — для неї ж
    screen.onkey(l_paddle.go_up, "w")  # W — для лівої ракетки вгору
    screen.onkey(l_paddle.go_down, "s")  # S — для неї ж вниз

    setup_menu(screen, balls, scoreboard)  # Ініціалізуємо меню інтерфейсу
    run_game()  # Запускаємо гру

def run_game():
    game_is_on = True  # Запуск гри
    try:
        while game_is_on:  # Поки гра активна
            screen.update()  # Оновлюємо вікно

            if not is_running() or is_paused():  # Якщо гра не запущена або призупинена
                continue  # Пропускаємо ітерацію

            time.sleep(balls[0].move_speed)  # Чекаємо відповідно до швидкості м'яча
            for i, ball in enumerate(balls):  # Для кожного м'яча
                ball.move()  # Рухаємось
                update_timer_display()  # Оновлюємо таймер
                update_speed_display(ball.move_speed)  # Оновлюємо швидкість м'яча

                if -320 < ball.xcor() < 320:  # Якщо м'яч не біля країв
                    recent_bounces[i] = False  # Скидаємо стан відбиття

                if not recent_bounces[i] and (  # Якщо нещодавно не було відбиття і...
                        (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or  # праворуч близько до ракетки
                        (ball.distance(l_paddle) < 50 and ball.xcor() < -320)  # або ліворуч
                ):
                    ball.bounce_x()  # Відбиваємо по x
                    register_bounce()  # Реєструємо відбиття
                    recent_bounces[i] = True  # Відзначаємо, що вже відбивали

                if ball.ycor() > 280 or ball.ycor() < -280:  # Якщо вдарився об верх або низ
                    ball.bounce_y()  # Відбиваємо по y
                    register_bounce()  # Реєструємо

                if abs(ball.xcor()) > 380:  # Якщо м'яч вилетів за межі
                    if ball.xcor() > 0:  # Якщо праворуч — очко лівому
                        scoreboard.l_point()
                    else:  # Якщо ліворуч — правому
                        scoreboard.r_point()
                    ball.reset_position()  # Скидаємо позицію
                    ball.goto(0, 0)  # У центр
                    ball.x_move = random.choice([-1, 1]) * (2 + random.random() * 2)  # Випадковий рух
                    ball.y_move = random.choice([-1, 1]) * (2 + random.random() * 2)

    except:  # Якщо вручну зупинили
        print("Гру завершено вручну.")  # Повідомлення в консоль

def restart_game(ball, scoreboard):  # Функція перезапуску гри
    global game_running, game_paused, bounce_count, start_time  # Глобальні змінні
    game_running = False  # Зупиняємо гру
    game_paused = False  # Вимикаємо паузу
    bounce_count = 0  # Скидаємо лічильник відбиттів
    start_time = time.time()  # Оновлюємо час старту

    if isinstance(ball, list):  # Якщо ball — список
        for b in ball:  # Для кожного м'яча
            b.goto(0, 0)  # Центруємо
            b.x_move = random.choice([-1, 1]) * (2 + random.random() * 2)  # Випадковий рух
            b.y_move = random.choice([-1, 1]) * (2 + random.random() * 2)
            b.move_speed = 0.05  # Скидаємо швидкість
            b.update_color()  # Оновлюємо колір
        update_speed_display(ball[0].move_speed)  # Оновлюємо швидкість на екрані
    else:  # Якщо один м'яч
        ball.goto(0, 0)
        ball.x_move = random.choice([-1, 1]) * (2 + random.random() * 2)
        ball.y_move = random.choice([-1, 1]) * (2 + random.random() * 2)
        ball.move_speed = 0.05
        ball.update_color()
        update_speed_display(ball.move_speed)

    scoreboard.l_score = 0  # Обнуляємо рахунок лівого
    scoreboard.r_score = 0  # І правого
    scoreboard.update_scoreboard()  # Оновлюємо табло
    draw_status("Натисни [Space], щоб почати | Зупинити: [p] | Почати спочатку: [r]")  # Інструкція
    update_bounce_display()  # Оновлюємо лічильник відбиттів
    update_timer_display()  # Оновлюємо таймер

screen.listen()
screen.onkey(lambda: start_level(1), "1")  # Рівень 1 — клавіша 1
screen.onkey(lambda: start_level(2), "2")  # Рівень 2 — клавіша 2
screen.onkey(lambda: start_level(3), "3")  # Рівень 3 — клавіша 3

screen.mainloop()  # Запускаємо головний цикл
