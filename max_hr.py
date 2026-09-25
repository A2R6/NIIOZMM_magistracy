def calculate_max_hr (age):
    """
        Функция для расчета максимальной частоты сердечных сокращений
    
        :param age: Возраст
        :return: максимальная частота сердечных сокращений
        """
    return 220 - age

if __name__ == "__main__":
    print("Программа для расчета максимальной частоты сердечных сокращений (ЧСС)")
    age = int(input("Введите возраст: "))

    max_hr = calculate_max_hr(age)

    # Расчёт границ зон
    zone_1_low = int(max_hr * 0.50)
    zone_1_high = int(max_hr * 0.60)

    zone_2_low = int(max_hr * 0.60)
    zone_2_high = int(max_hr * 0.70)

    zone_3_low = int(max_hr * 0.70)
    zone_3_high = int(max_hr * 0.80)

    zone_4_low = int(max_hr * 0.80)
    zone_4_high = int(max_hr * 0.90)

    print(f"Ваша максимальная частота сердечных колебаний (ЧСС): {max_hr} уд/мин")

    print(f"Зона 1 (50–60%): {zone_1_low}–{zone_1_high} уд/мин — низкая интенсивность, восстановление")
    print(f"Зона 2 (60–70%): {zone_2_low}–{zone_2_high} уд/мин — умеренная, развитие выносливости")
    print(f"Зона 3 (70–80%): {zone_3_low}–{zone_3_high} уд/мин — высокая, аэробная нагрузка")
    print(f"Зона 4 (80–90%): {zone_4_low}–{zone_4_high} уд/мин — очень высокая, анаэробная зона")
    