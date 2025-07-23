def check_ariscat(old: int, spo2: int, resp_inf: bool, anemia: bool, hir_razrez: str, long_oper: str, extr_oper: bool):
    old_score = 0 if old <= 50 else [3, 16][old > 80]
    spo2_score = 0 if spo2 >= 96 else [8, 24][spo2 <= 90]
    resp_inf_score = [0, 17][resp_inf]
    anem_score = [0, 11][anemia]
    hir_razrez_dict = {
        "Периферический (0 баллов)": 0,
        "Верхний абдоминальный (+15 баллов)": 15,
        "Внутригрудной (+24 балла)": 24
    }
    hir_razrez_score = hir_razrez_dict[hir_razrez]

    long_oper_dict = {
        "< 2 часов (0 баллов)": 0,
        "2–3 часа (+16 баллов)": 16,
        "> 3 часов (+23 балла)": 23
    }
    long_oper_score = long_oper_dict[long_oper]
    extr_oper = [0, 8][extr_oper]

    score = old_score + spo2_score + resp_inf_score + anem_score + hir_razrez_score + long_oper_score + extr_oper
    risk_dicti = {
        "Высокий": (44, 42.1),
        "Средний": (26, 13.3),
        "Низкий": (0, 1.6),

    }
    result = ("Низкий", 0)
    for k, v in risk_dicti.items():
        if score > v[0]:
            result = (k, v[1])
            break
    return score, result
