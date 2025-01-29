import re

# Округление часов до указанных в таблице-памятке
min_to_hour = {
    0:0, 5: 0.08, 10: 0.17, 15: 0.25, 20: 0.33, 25: 0.42,
    30: 0.5, 35: 0.58, 40: 0.67, 45: 0.75, 50: 0.83, 55: 0.92
    }

def format_time(hour: int, minute: int) -> dict:
    last_digit = 10 if (minute % 10 > 7) else 0 if (minute % 10 < 3) else 5 #Если минуты оканчиваются на 0-2 округляем до 0, 3-7 до 5, 8-9 округляет до следующего десятка, т.е. 18 минут округлит до 20
    minute = (minute // 10)*10 + last_digit
    if minute > 59: # 60 минут сбрасываем до нуля и добавляем час
        minute -= 60
        hour += 1
    return [hour, minute]


input_data = "Start" # Создание строки ввода
while input_data != "выход": # Пока не введено это слово повторяем цикл
    input_data = input("Вставьте строку с промежутками времени:")
    total, count = 0, 0
    timestamps = re.findall("\d*:\d* - \d*:\d*", input_data) # Ищет все промежутки и собирает в массив
    for ts in timestamps:
        tStart, tEnd = ts.split(" - ")
        tStart = tStart.split(':')
        tStart = format_time(int(tStart[0]), int(tStart[1]))
        tEnd = tEnd.split(':')
        tEnd = format_time(int(tEnd[0]), int(tEnd[1]))
        if not(0 <= tStart[0] < 24) or not (0 <= tEnd[0] < 24) or not (0 <= tStart[1] < 60) or not (0<=tEnd[1]<60):
            print("Неверный ввод.")
            continue
        tDelta = (tEnd[0]*60+tEnd[1]) - (tStart[0]*60+tStart[1])
        total += tDelta
        tStart[1] = f'0{tStart[1]}' if tStart[1] < 10 else tStart[1]
        tEnd[1] = f'0{tEnd[1]}' if tEnd[1] < 10 else tEnd[1]
        count += 1
        print(f"{count}) {tStart[0]}:{tStart[1]} - {tEnd[0]}:{tEnd[1]}, длительность {round(tDelta/60, 2)} ч.") # Выводит каждый найденный промежуток и его продолжительность в часах
    if total > 0:
        total = (total // 60) + min_to_hour[total%60]
        print(f'В полученной строке считано {count} отрезков времени.'
              f'\nОбщая продолжительность всех указанных промежутков составила {total} ч.'
              '\nДля выхода из цикла введите "выход" без кавычек.')
    elif input_data != "выход": # Чтобы при выходе не писало о пустом вводе.
        print("Пустой ввод.")
input("Нажмите Enter для закрытия окна.")
