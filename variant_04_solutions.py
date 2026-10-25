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
    """
    Зіставляє словник {'nozzle_id': int, 'temp': float, 'pressure': float}:
    - temp > 400 -> "Перегрів сопла {id}"
    - pressure < 1.2 -> "Витік палива в соплі {id}"
    - штатно -> "Сопло {id} працює штатно"
    """
    ...

# Задача 3: Перевірка цілісності пакета (for / else)
def verify_telemetry_packet(packet: list) -> str:
    """
    Перевіряє байти пакета. Якщо знайдено 0xFF -> негайно перериває (break)
    і повертає "Помилка пакета: виявлено 0xFF".
    Якщо цикл завершився без break -> повертає через else: "Пакет валідний".
    """
    ...

# Задача 4: Пошук втрати GPS (zip / enumerate)
def find_gps_loss_moments(time_list: list, sats_list: list) -> list:
    """
    За допомогою zip та enumerate знаходить перші 3 моменти часу (time),
    коли кількість супутників sats < 4.
    """
    ...
