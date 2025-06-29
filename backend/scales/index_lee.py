def lee_score_and_risk(
        high_risk_surgery: bool = False,
        ischemic_heart_disease: bool = False,
        heart_failure: bool = False,
        cva_or_tia: bool = False,
        diabetes_on_insulin: bool = False,
        creatinine_elevated: bool = False
) -> tuple[int, float]:
    """
    Расчёт индекса Ли (Revised Cardiac Risk Index, RCRI) и оценка вероятности осложнений.

    :param high_risk_surgery: Операция высокого риска
    :param ischemic_heart_disease: ИБС (инфаркт, стенокардия и т.д.)
    :param heart_failure: Хроническая сердечная недостаточность
    :param cva_or_tia: Перенесённые ОНМК / ТИА
    :param diabetes_on_insulin: Сахарный диабет на инсулине
    :param creatinine_elevated: Креатинин > 180 мкмоль/л

    :return: (баллы, риск осложнений в процентах)
    """
    score = sum([
        high_risk_surgery,
        ischemic_heart_disease,
        heart_failure,
        cva_or_tia,
        diabetes_on_insulin,
        creatinine_elevated
    ])

    if score == 0:
        risk_percent = 0.4
    elif score == 1:
        risk_percent = 0.9
    elif score == 2:
        risk_percent = 7.0
    else:  # score >= 3
        risk_percent = 11.0

    return score, risk_percent
