from typing import Literal


def get_parameters_ivl(idmt: float, intubation: str, bmi: float, spo2: int) -> dict:
    fio2 = 0.8 if spo2 > 94 else 1.0

    ventilation_settings = {
        "Преоксигенация": f"Через лицевую маску в течении 3 минут с FiO₂ {fio2}" if bmi < 35
        else f"CPAP c ПДКВ 10 см.вд.ст в течении 3 минут с FiO₂ {fio2}",
        "Интубация": intubation,
        "DO": round(6 * idmt, 2),
        "FiO₂": "< 0.8 (как можно ниже).",
        "PEEP": "8-15 мбар, при необ-ти увеличить, но т.о., чтобы движущее давление ΔP ≤ 15 мбар",
        "Pplato": "По возможности ≤ 30 мбар.",
        "ЧДД": "12-16, регулируется по etCO^2 35-50 мм рт. ст.",
    }
    return ventilation_settings


def get_medicine_data_induction(name: Literal[
    "propofol",
    "ketamin",
    "thyopental",
    "succinylcholine",
    "rocuronium",
    "atracurium",
    "veropipecuronium",
]) -> dict:
    """
    Retrieve the medicine data from the session state.
    """

    dictionary = {
        "propofol": {"parameters": "tmt", "doza": 2.5, "unit": "мг"},
        "ketamin": {"parameters": "cmt", "doza": 2.0, "unit": "мг"},
        "thyopental": {"parameters": "tmt", "doza": 4.0, "unit": "мг"},
        "succinylcholine": {"parameters": "weight", "doza": 1.5, "unit": "мг"},
        "rocuronium": {"parameters": "tmt", "doza": 0.8, "unit": "мг"},
        "atracurium": {"parameters": "tmt", "doza": 0.6, "unit": "мг"},
        "veropipecuronium": {"parameters": "tmt", "doza": 0.06, "unit": "мг"},
    }
    return dictionary[name]


def get_medicine_data_infusion(name: Literal[
    "propofol",
    "morphin",
    "rocuronium",
    "atracurium",
    "veropipecuronium"]) -> dict:
    """
    Retrieve the medicine data from the session state.
    """

    dictionary = {
        "propofol": {"parameters": "сmt", "doza": 9, "unit": "мг/ч"},
        "rocuronium": {"parameters": "tmt", "doza": 0.4, "unit": "мг/ч"},
        "atracurium": {"parameters": "tmt", "doza": 0.6, "unit": "мг/ч"},
        "veropipecuronium": {"parameters": "tmt", "doza": 0.02, "unit": "мг/ч"},

    }
    return dictionary[name]


def get_medicine_end_operation(name: Literal["propofol"]) -> dict:
    """
    Retrieve the medicine data from the session state.
    """

    dictionary = {
        "neostigmine": {"parameters": "cmt", "doza": 0.07, "unit": "мг"},
        "paracetamol": {"parameters": "tmt", "doza": 15.0, "unit": "мг"},
    }
    return dictionary[name]


def get_induction_dose(idmt: float, tmt: float, cmt: float, weight: float) -> list[dict]:
    """
    Return the induction dose for propofol.
    - пропофол: 2 мг/кг для индукции, 1 мг/кг/ч для поддержания
    Рокуроний: 0.6 мг/кг
    Сукцинилхлорид: 1.0 мг/кг
    Кетамин: 1.0 мг/кг
    """

    medicines = [
        "propofol",
        "ketamin",
        "thyopental",
        "succinylcholine",
        "rocuronium",
        "atracurium",
        "veropipecuronium"
    ]
    result = []
    for med in medicines:
        med_data = get_medicine_data_induction(med)
        if med == "succinylcholine":
            weight = weight
        else:
            weight = idmt if med_data["parameters"] == "idmt" else tmt if med_data["parameters"] == "tmt" else cmt
        dose = f"{med_data['doza'] * weight:.2f}"
        result.append({"medicine": med, "dose": dose, "unit": med_data["unit"]})

    ap_l = [{"medicine": "phenthanyl", "dose": 0.2, "unit": "мг"}, {"medicine": "morphin", "dose": 20, "unit": "мг"}]
    result = result[:1] + ap_l + result[1:]
    return result


def get_infusion_dose(idmt: float, tmt: float, cmt: float) -> list[dict]:
    medicines = ["propofol", "rocuronium", "atracurium", "veropipecuronium"]
    result = []
    for med in medicines:
        med_data = get_medicine_data_infusion(med)
        weight = idmt if med_data["parameters"] == "idmt" else tmt if med_data["parameters"] == "tmt" else cmt
        dose = f"{med_data['doza'] * weight:.2f}"
        result.append({"medicine": med, "dose": dose, "unit": med_data["unit"]})

    ap_l = [{"medicine": "phenthanyl", "dose": 0.4, "unit": "мг/ч"}]
    result = result[:1] + ap_l + result[1:]
    return result


def get_end_operation_dose(idmt: float, tmt: float, cmt: float) -> list[dict]:
    """Максимальная доза: 0,07 мг/кг внутривенно или до 5 мг внутривенно, в зависимости от того, какая доза меньше
"""
    medicines = [("neostigmine", 5), ("paracetamol", 1000)]
    result = []
    for med in medicines:
        med_data = get_medicine_end_operation(med[0])
        weight = idmt if med_data["parameters"] == "idmt" else tmt if med_data["parameters"] == "tmt" else cmt
        dose = f"{med_data['doza'] * weight:.2f}"
        result.append({"medicine": med[0], "dose": min((float(dose), med[1])), "unit": med_data["unit"]})
    return result


def get_add_medicine_induction(name: Literal["ketamin", "mgso4", "dexmedetomedin", "lidocaine"]) -> dict:
    """
    Retrieve the additional medicine data for induction.
    """

    dictionary = {
        "ketamin": {"parameters": "idmt", "doza": 0.3, "unit": "мг"},
        "mgso4": {"parameters": "idmt", "doza": 30.0, "unit": "мг"},
        "dexmedetomedin": {"parameters": "tmt", "doza": 0.001, "unit": "мг в течении 10 мин"},
        "lidocaine": {"parameters": "tmt", "doza": 1.5, "unit": "мг"},
    }
    return dictionary[name]


def get_add_medicine_infusion(name: Literal["ketamin", "mgso4", "dexmedetomedin", "lidocaine"]) -> dict:
    """
    Retrieve the additional medicine data for induction.
    """

    dictionary = {
        "ketamin": {"parameters": "idmt", "doza": 0.15, "unit": "мг"},
        "mgso4": {"parameters": "idmt", "doza": 10.0, "unit": "мг"},
        "dexmedetomedin": {"parameters": "tmt", "doza": 0.0007, "unit": "мг"},
        "lidocaine": {"parameters": "tmt", "doza": 2.0, "unit": "мг"},
    }
    return dictionary[name]


def get_ad_induction_dose(idmt: float, tmt: float, cmt: float):
    medicines = ["ketamin", "mgso4", "dexmedetomedin", "lidocaine"]
    result = []
    for med in medicines:
        med_data = get_add_medicine_induction(med)
        weight = idmt if med_data["parameters"] == "idmt" else tmt if med_data["parameters"] == "tmt" else cmt
        dose = f"{med_data['doza'] * weight:.2f}"
        result.append({"medicine": med, "dose": dose, "unit": med_data["unit"]})

    result.append({"medicine": "dexamethasone", "dose": 8, "unit": "мг"})
    return result


def get_ad_infusion_dose(idmt: float, tmt: float, cmt: float):
    medicines = ["ketamin", "mgso4", "dexmedetomedin", "lidocaine"]
    result = []
    for med in medicines:
        med_data = get_add_medicine_infusion(med)
        weight = idmt if med_data["parameters"] == "idmt" else tmt if med_data["parameters"] == "tmt" else cmt
        dose = f"{med_data['doza'] * weight:.2f}"
        result.append({"medicine": med, "dose": dose, "unit": med_data["unit"]})

    return result
