"""
Лабораторна робота: Варіант 4
Студент: Бучак Олег
Група: EIP30
"""

# Задача 1: Кут входження в атмосферу (if/elif/else)
def check_entry_angle(gamma: float) -> str:
    if gamma > -5.5: #перевіряємо, чи не є кут входження занадто пологим
        return "Рикошет від атмосфери"
    elif gamma < -7.5: #перевіряємо, чи не є входження занадто крутим
        return "Перегрів та руйнування"
    else: #якщо кут у допустимих межах, вхід успішний
        return "Вхід успішний"


# Задача 2: Статус сопел орієнтації (match-case)
def check_nozzle_status(data: dict) -> str:
    match data: #перевіряємо стан сопла за даними словника
        case {"nozzle_id": nozzle_id, "temp": temp} if temp > 400: #якщо температура більша за 400, сопло перегріте
            return f"Перегрів сопла {nozzle_id}"
        case {"nozzle_id": nozzle_id, "pressure": pressure} if pressure < 1.2: #якщо тиск менший за 1.2, виявлено витік палива
            return f"Витік палива в соплі {nozzle_id}"
        case {"nozzle_id": nozzle_id, "temp": temp, "pressure": pressure}: #якщо попередні умови не виконалися, сопло працює штатно
            return f"Сопло {nozzle_id} працює штатно"
        case _: #якщо у словнику неправильні дані
            return "Некоректні дані"
    

# Задача 3: Перевірка цілісності пакета (for / else)
def verify_telemetry_packet(packet: list) -> str:
    for byte in packet: #послідовно перевіряємо кожен байт пакета
        if byte == 0xFF: #якщо знайдено байт помилки, перериваємо цикл
            break 
    else: #якщо цикл завершився без break, то виконується ця частина коду
        return "Пакет валідний"
    return "Помилка пакета: виявлено 0xFF" #повертаємо повідомлення про помилку якщо відбувся break


# Задача 4: Пошук втрати GPS (zip / enumerate)
def find_gps_loss_moments(time_list: list, sats_list: list) -> list:  
    loss_moments = [] #створюємо пустйи список для збереження моментів втрати GPS
    #об'єднуємо час і кількість супутників, додаючи індекс
    for index, (time, sats) in enumerate(zip(time_list, sats_list)):
        if sats < 4: #якщо супутників менше 4, то додаємо відповідний час до списку
            loss_moments.append(time)

            if len(loss_moments) == 3: #після того як знайшли три моменти припиняємо пошук
                break
    return loss_moments

#перевірки роботи коду
print("--------------------1--------------------")
print(check_entry_angle(-6.5))
print(check_entry_angle(-5.0))
print(check_entry_angle(-8.0))

print("--------------------2--------------------")
print(check_nozzle_status({"nozzle_id": 1, "temp": 450, "pressure": 2.0}))
print(check_nozzle_status({"nozzle_id": 2, "temp": 300, "pressure": 0.8}))
print(check_nozzle_status({"nozzle_id": 3, "temp": 300, "pressure": 2.0}))

print("--------------------3--------------------")
print(verify_telemetry_packet([0x12, 0x34, 0x56]))
print(verify_telemetry_packet([0x12, 0xFF, 0x56]))

print("--------------------4--------------------")
print(find_gps_loss_moments(
    [10, 20, 30, 40, 50, 60],
    [7, 3, 5, 2, 1, 6]
))


