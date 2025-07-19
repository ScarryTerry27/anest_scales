from typing import Literal


def stopbang_score(
        snoring: bool = False,
        daytime_sleepiness: bool = False,
        apnea_observed: bool = False,
        hypertension: bool = False,
        bmi: float = 35.0,
        age: int = 50,
        neck_circumference_cm: int = 40,
        gender: Literal["man", "woman"] = "man"
) -> int:
    """
    Оценка риска обструктивного апноэ сна по шкале STOP-BANG.

    S — Храп
    T — Дневная сонливость
    O — Остановка дыхания во сне (наблюдаемая)
    P — Артериальная гипертензия
    B — BMI > 35
    A — Возраст > 50 лет
    N — Обхват шеи > 40 см
    G — Мужской пол

    :return: Количество положительных признаков (0–8)
    """
    score = sum([
        snoring,
        daytime_sleepiness,
        apnea_observed,
        hypertension,
        bmi > 35,
        age > 50,
        neck_circumference_cm > 40,
        gender == "man"
    ])
    return score


def is_high_soba_risk(
        poor_functional_data: bool = False,
        ecg_changes: bool = True,
        uncontrolled_hypertension_or_ischemia: bool = False,
        spo2: int = 94,
        co2: int = 28,
        thromboembolic_history: bool = False,
        stopbang_score_val: int = 5
) -> bool:
    """
    Определение высокого риска по шкале SOBA.

    Учитываются:
    - Нарушения функциональных показателей
    - Изменения ЭКГ
    - Неконтролируемое АГ или ишемическая болезнь сердца
    - SpO2 < 94% на атмосферном воздухе
    - CO2 > 28 мм рт. ст.
    - Тромбоэмболический анамнез
    - STOPBANG > 5

    :return: True, если риск повышен
    """

    return any([
        poor_functional_data,
        ecg_changes,
        spo2 < 94,
        uncontrolled_hypertension_or_ischemia,
        co2 > 28,
        thromboembolic_history,
        stopbang_score_val > 5
    ])
