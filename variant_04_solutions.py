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
    """
    За допомогою zip та enumerate знаходить перші 3 моменти часу (time),
    коли кількість супутників sats < 4.
    """
    ...
