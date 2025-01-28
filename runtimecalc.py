import re

# Округление часов до указанных в таблице-памятке
min_to_hour = {
    0:0, 5: 0.08, 10: 0.17, 15: 0.25, 20: 0.33, 25: 0.42,
    30: 0.5, 35: 0.58, 40: 0.67, 45: 0.75, 50: 0.83, 55: 0.92
    }
input_data = "Start" # Создание строки ввода
while input_data != "выход": # Пока не введено это слово повторяем цикл
    input_data = input("Вставьте строку с промежутками времени:")
    total, count = 0, 0
    timestamps = re.findall("\d*:\d* - \d*:\d*", input_data) # Ищет все промежутки и собирает в массив
    for ts in timestamps:
        tStart, tEnd = ts.split(" - ")
        tStart = tStart.split(':')
        tStart[0],tStart[1] = int(tStart[0]), int(tStart[1])
        tEnd = tEnd.split(':')
        tEnd[0],tEnd[1] = int(tEnd[0]), int(tEnd[1])
        if not(0 <= tStart[0] < 24) or not (0 <= tEnd[0] < 24) or not (0 <= tStart[1] < 60) or not (0<=tEnd[1]<60):
            print("Неверный ввод.")
            continue
        tDelta = (tEnd[0]*60+tEnd[1]) - (tStart[0]*60+tStart[1])
        total += tDelta
        print(ts, round(tDelta/60, 2)) # Выводит каждый найденный промежуток и его продолжительность в часах
        count += 1
    if total > 0:
        total = (total // 60) + min_to_hour[total%60]
        print(f'В полученной строке считано {count} отрезков времени.'
              f'\nОбщая продолжительность всех указанных промежутков составила {total} ч.'
              '\nДля выхода из цикла введите "выход" без кавычек.')
    elif input_data != "выход": # Чтобы при выходе не писало о пустом вводе.
        print("Пустой ввод.")
input("Нажмите Enter для закрытия окна.")
