def caprini_score_and_risk(caprini_flags: dict) -> tuple[int, str]:
    """
    Расчёт суммы баллов по шкале Caprini и определение уровня риска ВТЭО.

    :param caprini_flags: Словарь вида {ключ: bool}, где ключ — название фактора.
    :return: (сумма баллов, уровень риска как строка)
    """

    # Словарь баллов по факторам (ключ должен совпадать с названием флага)
    caprini_weights = {
        # 1 балл
        "Caprini_Отеки": 1,
        "Caprini_Варикоз": 1,
        "Caprini_Сепсис": 1,
        "Caprini_Заболевание_легких": 1,
        "Caprini_Гормоны": 1,
        "Caprini_Беременность": 1,
        "Caprini_Акушерский_анамнез": 1,
        "Caprini_Инфаркт": 1,
        "Caprini_ХСН": 1,
        "Caprini_Постельный": 1,
        "Caprini_ХОБЛ": 1,
        "Caprini_Онкология": 1,
        "Caprini_Прочее": 1,

        # 2 балла
        "Caprini_Постельный_72ч": 2,
        "Caprini_Хирургия_анамнез": 2,
        "Caprini_Иммобилизация": 2,
        "Caprini_Катетер": 2,
        "Caprini_Артроскопия": 2,
        "Caprini_Лапароскопия": 2,
        "Caprini_Большая_операция": 2,
        "Caprini_Онкология": 2,  # может быть 1 или 2, если нужно, обработать отдельно

        # 3 балла
        "Caprini_ВТЭО_анамнез": 3,
        "Caprini_Лейден": 3,
        "Caprini_Протромбин": 3,
        "Caprini_Волчанка": 3,
        "Caprini_Семейный_ВТЭО": 3,
        "Caprini_Гомоцистеин": 3,
        "Caprini_ГИТ": 3,
        "Caprini_Антикардиолипин": 3,
        "Caprini_Тромбофилия": 3,

        # 5 баллов
        "Caprini_Инсульт": 5,
        "Caprini_Паралич": 5,
        "Caprini_Травма": 5,
        "Caprini_Эндопротез": 5,
        "Caprini_Перелом": 5,
    }

    score = 0
    for key, value in caprini_flags.items():
        if value and key in caprini_weights:
            score += caprini_weights[key]

    # Определение уровня риска
    if score <= 1:
        risk = "Очень низкий"
    elif score == 2:
        risk = "Низкий"
    elif 3 <= score <= 4:
        risk = "Умеренный"
    else:
        risk = "Высокий"

    return score, risk
