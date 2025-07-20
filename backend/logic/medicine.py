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
        "intubation": intubation,
        "DO": round(6 * idmt, 2),
        "FiO2": "< 0.8 (как можно ниже).",
        "PEEP": "8-15 мбар, при необходимости увеличить, но т.о., чтобы движущее давление (ДР) не превышало 15 мбар",
        "Pplato": "По возможности, ≤ 30 мбар.",
        "Recruitment": "Периодические маневры рекрутирования. У больных с ожирением - 50 мбар.",
        "PaCO2": "Нормокапния за счет регулирования частоты."
    }
    return ventilation_settings
