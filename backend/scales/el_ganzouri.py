def check_elganzouri(elganzouri_flag: dict):
    thyromental_distance = {"Более 6.5 см (0 баллов)": 0, "6–6.5 см (+1 балл)": 1, "Менее 6 см (+2 балла)": 2}
    mallampati = {"I (0 баллов)": 0, "II (+1 балл)": 1, "III (+2 балла)": 2, "IV (+2 балла)": 2}
    intubation_history = {"Нет (0 баллов)": 0, "Недостоверно (+1 балл)": 1, "Определённо (+2 балла)": 2}
    head_angle = {"Более 90° (0 баллов)": 0, "80–90° (+1 балл)": 1, "Менее 80° (+2 балла)": 2}
    jaw_movement = {"Да (0 баллов)": 0, "Нет (+1 балл)": 1}
    mouth_opening = {"Более 4 см (0 баллов)": 0, "Менее 4 см (+1 балл)": 1}
    score = sum([
        intubation_history[elganzouri_flag["ElGanzouri_Интубация"]],
        thyromental_distance[elganzouri_flag["ElGanzouri_Thyromental"]],
        mallampati[elganzouri_flag["ElGanzouri_Mallampati"]],
        head_angle[elganzouri_flag["ElGanzouri_Голова"]],
        jaw_movement[elganzouri_flag["ElGanzouri_Челюсть"]],
        mouth_opening[elganzouri_flag["ElGanzouri_Рот"]],
    ]
    )

    result_dict = {
        8: "Интубация трахеи в сознании при бронхоскопии",
        4: "Интубация трахеи при видеоларингоскопии",
    }
    result = "Интубация трахеи при обычной ларингоскопии"

    for k, v in result_dict.items():
        if score >= k:
            result = v
            break
    return score, result
