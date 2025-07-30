from typing import Tuple, Literal


def calculate_bmi(height_cm: int, weight_kg: int) -> Tuple[float, str]:
    """
    Расчёт индекса массы тела (Body Mass Index).

    :param height_cm: Рост в сантиметрах
    :param weight_kg: Вес в килограммах
    :return: BMI = вес (кг) / (рост (м))²
    """
    height_m = height_cm / 100
    dictionary_info = {
        18.5: "Недостаточная масса тела",
        24.9: "Нормальная масса тела",
        29.9: "Избыточная масса тела",
        34.9: "Ожирение I степени",
        39.9: "Ожирение II степени",
        49.9: "Ожирение III степени",
        59.9: "супер ожирение",
        60.0: "супер-супер ожирение"
    }
    bmi = round(weight_kg / (height_m ** 2), 2)
    filtered_info = {k: v for k, v in dictionary_info.items() if k <= bmi}
    max_info = max(filtered_info.keys()) if filtered_info else 18.5
    return bmi, dictionary_info[max_info]


def calculate_idmt(height_cm, gender: Literal["man", "woman"] = "man") -> int:
    """
    Расчёт идеальной массы тела (Ideal Body Mass).

    :param gender Literal["man", "woman"] Пол пациента
    :param height_cm: Рост в сантиметрах"""
    delta = [100, 105][gender == "man"]
    return height_cm - delta


def calculate_tmt(weight, bmi, gender: Literal["man", "woman"] = "man") -> int:
    if gender == "man":
        tmt = 9270 * weight / (6680 + 216 * bmi)
    else:
        tmt = 9270 * weight / (8780 + 244 * bmi)
    return round(tmt, 2)


def calculate_cmt(weight, idmt) -> int:
    cmt = idmt + 0.4 * (weight - idmt)
    return round(cmt, 2)


def calculate_asa(bmi, lee_res, flag) -> tuple:
    asa = "Не определён"
    extr = "E" if flag else ""

    if bmi >= 35:
        asa = f"III{extr} класс", "Высокий"
        if lee_res >= 1:
            asa = f"IV{extr} класс", "Крайне-высокий"
    elif bmi >= 30:
        asa = f"II{extr} класс", "Умеренный"
        if lee_res == 1:
            asa = f"III{extr} класс", "Высокий"
        elif lee_res >= 2:
            asa = f"IV{extr} класс", "Крайне-высокий"
    else:
        asa = f"I{extr} класс", "Низкий" if not extr else "Умеренный"
        if lee_res >= 2:
            asa = f"III{extr} класс", "Высокий"
        elif lee_res == 1:
            asa = f"II{extr} класс", "Умеренный"
    return asa
