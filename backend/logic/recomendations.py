def generate_diagnostic(soba_recommendation: bool) -> str:
    """
    Генерирует рекомендации по шкале Каприни на основе данных из сессии.
    Возвращает текст с рекомендациями.
    """
    base_text = ""
    if soba_recommendation:
        file_path = f"backend/texts/soba.md"
        with open(file_path, "r", encoding="utf-8") as file:
            base_text += file.read()
    if not base_text:
        base_text = "#### 🧾 Стандартное обследование пациента\n\n"
    return base_text


def generate_recommendations(caprini_risk: str, ariscat: int, spo2: int, pulm_risk: bool) -> str:
    # Стартовый текст, если есть показания к CPAP
    start_text = ""
    if pulm_risk or ariscat >= 44 or spo2 < 93:
        start_text = (
            "### 🫁 Рекомендации по послеоперационной респираторной поддержке\n\n"
            "- Рассмотреть применение послеоперационного CPAP\n\n"
        )

    # Словарь соответствий уровням риска и путям к файлам
    dictionary_files = {
        "Очень низкий": "caprini_very_low.md",
        "Низкий": "caprini_low.md",
        "Умеренный": "caprini_middle.md",
        "Высокий": "caprini_high.md"
    }

    # Чтение рекомендаций по ВТЭО из файла
    file_path = f"backend/texts/{dictionary_files[caprini_risk]}"
    with open(file_path, "r", encoding="utf-8") as file:
        vteo_text = file.read()

    # Возвращаем итоговый текст с двойным переносом между блоками
    return f"{start_text}{vteo_text if start_text == '' else f'\n\n{vteo_text}'}"


def generate_monitoring(bmi):
    filepath = ["backend/texts/monitoring_st.md", "backend/texts/monitoring_bmi.md"][bmi >= 35]
    with open(filepath, "r", encoding="utf-8") as file:
        result = file.read()
    return result

