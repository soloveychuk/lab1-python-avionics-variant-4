"""
Лабораторна робота: Варіант 4
Студент: Бучак Олег
Група: EIP30
"""

# Задача 1: Кут входження в атмосферу (if/elif/else)
def check_entry_angle(gamma: float) -> str:
    if gamma > -5.5:
        return "Рикошет від атмосфери"
    elif gamma < -7.5:
        return "Перегрів та руйнування"
    else:
        return "Вхід успішний"


# Задача 2: Статус сопел орієнтації (match-case)
def check_nozzle_status(data: dict) -> str:
    match data:
        case {"nozzle_id": nozzle_id, "temp": temp} if temp > 400:
            return f"Перегрів сопла {nozzle_id}"
        case {"nozzle_id": nozzle_id, "pressure": pressure} if pressure < 1.2:
            return f"Витік палива в соплі {nozzle_id}"
        case {"nozzle_id": nozzle_id, "temp": temp, "pressure": pressure}:
            return f"Сопло {nozzle_id} працює штатно"
        case _:
            return "Некоректні дані"
    

# Задача 3: Перевірка цілісності пакета (for / else)
def verify_telemetry_packet(packet: list) -> str:
    for byte in packet:
        if byte == 0xFF:
            break
    else:
        return "Пакет валідний"
    return "Помилка пакета: виявлено 0xFF"


# Задача 4: Пошук втрати GPS (zip / enumerate)
def find_gps_loss_moments(time_list: list, sats_list: list) -> list:
    loss_moments = []
    for index, (time, sats) in enumerate(zip(time_list, sats_list)):
        if sats < 4:
            loss_moments.append(time)

            if len(loss_moments) == 3:
                break
    return loss_moments


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


