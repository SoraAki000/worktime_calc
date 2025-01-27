import re

# Округление часов до указанных в таблице-памятке
min_to_hour = {
    5: 0.08, 10: 0.17, 15: 0.25, 20: 0.33, 25: 0.42, 30: 0.5,
    35: 0.58, 40: 0.67, 45: 0.75, 50: 0.83, 55: 0.92
    }
input_data = "Start"
while input_data != "выход":
    input_data = input("Вставьте строку с промежутками времени:")
    total = 0
    timestamps = re.findall("\d*:\d* - \d*:\d*", input_data) # Ищет все проомежутки и собирает в массив
    for ts in timestamps:
        tStart, tEnd = ts.split(" - ")
        tStart = tStart.split(':')
        tEnd = tEnd.split(':')
        if not tStart or not tEnd:
            print("Неверный ввод.")
            exit()
        tDelta = (int(tEnd[0])*60+int(tEnd[1])) - (int(tStart[0])*60+int(tStart[1]))
        total += tDelta
        print(ts, round(tDelta/60, 2)) # Выводит каждый найденный промежуток и его продолжительность в часах
    if total > 0:
        total = (total // 60) + min_to_hour[total%60]
        print(f'В полученной строке считано {len(timestamps)} отрезков времени.\nОбщая продолжительность всех указанных промежутков составила {total} ч.\nДля выхода из цикла введите "выход" без кавычек.')
    elif input_data != "выход":
        print("Пустой ввод.")
input("Нажмите Enter для закрытия окна.")
