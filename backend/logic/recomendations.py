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
        base_text = "### 🧾 Стандартное обследование пациента\n\n"
    return base_text


def generate_recommendations(caprini_risk: str) -> str:
    # Словарь соответствий файла уровням риска
    base_text = ""

    # Словарь соответствий файла уровням риска
    dictionary_files = {
        "Очень низкий": "caprini_very_low.md",
        "Низкий": "caprini_low.md",
        "Умеренный": "caprini_middle.md",
        "Высокий": "caprini_high.md"
    }

    # Чтение рекомендаций из файла по уровню риска
    file_path = f"backend/texts/{dictionary_files[caprini_risk]}"
    with open(file_path, "r", encoding="utf-8") as file:
        base_text += file.read()

    return base_text
