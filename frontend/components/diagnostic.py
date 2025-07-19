import streamlit as st


def show_diagnostic():
    """Отображает диагностические данные пациента с учетом шкалы Caprini."""

    soba_recommendation = (
        "\n\n---\n\n"
        "**📌 Дополнительные диагностические мероприятия при синдроме обструктивного апноэ сна (СОАС):**\n\n"
        "- Анализ газового состава крови\n"
        "- Исследование сна\n"
        "- Предоперационный CPAP\n"
        "- Эхокардиография\n"
        "- Кардио-респираторное обследование\n\n"
        "> 🛑 **Необходима опытная анестезиологическая бригада, если операция считается необходимой.**"
    )

    # Получение данных из сессии
    caprini_score = st.session_state.scales['caprini'][0]
    caprini_risk = st.session_state.scales['caprini'][1]

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
    try:
        file_path = f"frontend/texts/{dictionary_files[caprini_risk]}"
        with open(file_path, "r", encoding="utf-8") as file:
            base_text += file.read()
    except Exception as e:
        base_text += "_⚠️ Не удалось загрузить рекомендации по уровню риска._"

    # Добавление блока СОАС
    base_text += soba_recommendation

    # Отображение в Streamlit
    with st.expander("🧾 Рекомендованная диагностика пациента"):
        st.markdown(base_text, unsafe_allow_html=True)
