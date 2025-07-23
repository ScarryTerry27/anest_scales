from typing import Literal


def get_medicine_data(
        name: Literal[
            "propofol",
            "thiopental",
            "fentanyl",
            "rocuronium",
            "atracurium",
            "vecuronium",
            "morphine",
            "paracetamol",
            "bupivacaine",
            "lidocaine",
            "alfentanil",
            "neostigmine",
            "sugammadex",
            "antibiotics"]
) -> dict:
    """
    Retrieve the medicine data from the session state.
    """

    dictionary = {
        "propofol": {
            "induction": {"parameters": "tmt", "doza": 2.0, "unit": "мг/кг"},
            "infusion": {"parameters": "cmt", "doza": 1.0, "unit": "мг/кг/ч"}
        },
        "thiopental": {"parameters": "tmt", "doza": 5.0, "unit": "мг/кг"},
        "fentanyl": {"parameters": "tmt", "doza": 2.0, "unit": "мкг/кг"},
        "rocuronium": {"parameters": "tmt", "doza": 0.6, "unit": "мг/кг", },
        "atracurium": {"parameters": "tmt", "doza": 0.5, "unit": "мг/кг"},
        "vecuronium": {"parameters": "tmt", "doza": 0.1, "unit": "мг/кг"},
        "morphine": {"parameters": "tmt", "doza": 0.1, "unit": "мг/кг"},
        "paracetamol": {"parameters": "tmt", "doza": 15.0, "unit": "мг/кг"},
        "bupivacaine": {"parameters": "tmt", "doza": 2.0, "unit": "мг/кг"},
        "lidocaine": {"parameters": "tmt", "doza": 5.0, "unit": "мг/кг"},
        "alfentanil": {"parameters": "cmt", "doza": 10.0, "unit": "мкг/кг"},
        "neostigmine": {"parameters": "cmt", "doza": 0.05, "unit": "мг/кг"},
        "sugammadex": {"parameters": "cmt", "doza": 2.0, "unit": "мг/кг"},
    }
    return dictionary[name]


def get_medicine_dose_table(tmt: float, cmt: float) -> list[dict]:
    """
    Return a list of dictionaries with medicine, dose, unit, and type
    for tabular representation.
    """
    medicines = [
        "propofol", "thiopental", "fentanyl", "rocuronium", "atracurium",
        "vecuronium", "morphine", "paracetamol", "bupivacaine", "lidocaine",
        "alfentanil", "neostigmine", "sugammadex"
    ]

    table = []
    for med in medicines:
        if med != "propofol":
            med_data = get_medicine_data(med)
            weight = cmt if med_data["parameters"] == "cmt" else tmt
            dose = f"{med_data['doza'] * weight:.2f}"  # строка с 2 знаками после запятой
            table.append({
                "medicine": med,
                "type": "standard",
                "dose": dose,
                "unit": med_data["unit"]
            })
        else:
            # Handle propofol separately with induction and infusion
            item_ind = get_medicine_data(med)["induction"]
            item_inf = get_medicine_data(med)["infusion"]

            weight_ind = cmt if item_ind["parameters"] == "cmt" else tmt
            weight_inf = cmt if item_inf["parameters"] == "cmt" else tmt

            dose_ind = f"{item_ind["doza"] * weight_ind:.2f}"
            dose_inf = f"{item_inf["doza"] * weight_inf:.2f}"

            table.append({
                "medicine": "propofol",
                "type": "induction",
                "dose": dose_ind,
                "unit": item_ind["unit"]
            })
            table.append({
                "medicine": "propofol",
                "type": "infusion",
                "dose": dose_inf,
                "unit": item_inf["unit"]
            })

    return table


def get_parameters_ivl(idmt: float, intubation: str):
    ventilation_settings = {
        "Интубация": intubation,
        "DO": round(6 * idmt, 2),
        "FiO2": "< 0.8 (как можно ниже).",
        "PEEP": "8-15 мбар, при необ-ти увеличить, но т.о., чтобы движущее давление ΔP ≤ 15 мбар",
        "Pplato": "По возможности ≤ 30 мбар.",
        "ЧДД": "12-16, регулируется по etCO^2 35-50 мм рт. ст.",
    }
    return ventilation_settings


def get_medicine_data_induction(name: Literal["propofol", "rocuronium", "succinylcholine", "ketamine"]) -> dict:
    """
    Retrieve the medicine data from the session state.
    """

    dictionary = {
        "propofol": {"parameters": "tmt", "doza": 2.0, "unit": "мг"},
        "rocuronium": {"parameters": "tmt", "doza": 0.6, "unit": "мг"},
        "succinylcholine": {"parameters": "idmt", "doza": 1.5, "unit": "мг"},
        "ketamine": {"parameters": "cmt", "doza": 2.0, "unit": "мг"},
    }
    return dictionary[name]


def get_medicine_data_infusion(name: Literal["propofol"]) -> dict:
    """
    Retrieve the medicine data from the session state.
    """

    dictionary = {
        "propofol": {"parameters": "tmt", "doza": 9, "unit": "мг/ч"},
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


def get_induction_dose(idmt: float, tmt: float, cmt: float) -> list[dict]:
    """
    Return the induction dose for propofol.
    - пропофол: 2 мг/кг для индукции, 1 мг/кг/ч для поддержания
    Рокуроний: 0.6 мг/кг
    Сукцинилхлорид: 1.0 мг/кг
    Кетамин: 1.0 мг/кг
    """

    medicines = ["propofol", "rocuronium", "succinylcholine", "ketamine"]
    result = []
    for med in medicines:
        med_data = get_medicine_data_induction(med)
        weight = idmt if med_data["parameters"] == "idmt" else tmt if med_data["parameters"] == "tmt" else cmt
        dose = f"{med_data['doza'] * weight:.2f}"
        result.append({"medicine": med, "dose": dose, "unit": med_data["unit"]})
    return result


def get_infusion_dose(idmt: float, tmt: float, cmt: float) -> list[dict]:
    medicines = ["propofol"]
    result = []
    for med in medicines:
        med_data = get_medicine_data_infusion(med)
        weight = idmt if med_data["parameters"] == "idmt" else tmt if med_data["parameters"] == "tmt" else cmt
        dose = f"{med_data['doza'] * weight:.2f}"
        result.append({"medicine": med, "dose": dose, "unit": med_data["unit"]})
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
