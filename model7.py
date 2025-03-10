# Форматирование строк

team1_num = 5
team2_num = 6

score_1 = 40
score_2 = 42

team1_time = 1552.512
team2_time = 2153.31451


# Используя %:
# Количество участников первой команды
print("В команде Мастера кода участников: %s !" % team1_num)

# Количество участников в обеих командах
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

# Используя format():
# Количество задач, решённых командой 2
print("Команда Волшебники данных решила задач: {} !".format(score_2))

# Время, за которое команда 2 решила задачи
print("Волшебники данных решили задачи за {} с !".format(team2_time))

# Используя f-строки:
# Количество решённых задач по командам
print(f"Команды решили {score_1} и {score_2} задач.")

# Исход соревнования
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
print(f"Результат битвы: {challenge_result}")

# Количество задач и среднее время решения
tasks_total = score_1 + score_2  # Общее количество задач
time_avg = (team1_time + team2_time) / 2  # Среднее время решения
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!.")