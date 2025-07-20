def generate_diagnostic(caprini_score: float, caprini_risk: str, soba_recommendation: bool) -> str:
    """
    Генерирует рекомендации по шкале Каприни на основе данных из сессии.
    Возвращает текст с рекомендациями.
    """

    # Начальный текст
    base_text = (
        f"### 💡 Уровень риска ВТЭО: **{caprini_risk}**  \n"
        f"**Сумма баллов:** {caprini_score}\n\n"
    )

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

    if soba_recommendation:
        file_path = f"backend/texts/items.txt"
        with open(file_path, "r", encoding="utf-8") as file:
            base_text += file.read()
    return base_text
