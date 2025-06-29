import time

import streamlit as st

from frontend.components.menu import next_router, show_button_down


def show_arescat():
    st.subheader("🫁 Шкала ARISCAT — риск послеоперационных легочных осложнений")

    with st.form("SCALE_ARISCAT"):
        ar_infection = st.radio(
            "Была ли респираторная инфекция в последние 30 дней?",
            options=["Нет (0 баллов)", "Да (+17 баллов)"],
            index=0
        )

        ar_anemia = st.radio(
            "Присутствует ли анемия? (Hb ≤ 100 г/л)",
            options=["Нет (0 баллов)", "Да (+11 баллов)"],
            index=0
        )

        ar_incision = st.selectbox(
            "Локализация хирургического доступа:",
            options=["Периферический (0 баллов)", "Верхний абдоминальный (+15 баллов)", "Внутригрудной (+24 балла)"],
            index=0
        )

        ar_duration = st.selectbox(
            "Сколько длилась (или планируется) операция:",
            options=["< 2 часов (0 баллов)", "2–3 часа (+16 баллов)", "> 3 часов (+23 балла)"],
            index=0
        )

        ar_emergency = st.radio(
            "Операция экстренная?",
            options=["Нет (0 баллов)", "Да (+8 баллов)"],
            index=0
        )
        if st.form_submit_button("✅ Сохранить"):
            # Сохраняем всё в session_state
            st.session_state.patient_data.update({
                "ARISCAT_Инфекция": ar_infection,
                "ARISCAT_Анемия": ar_anemia,
                "ARISCAT_Разрез": ar_incision,
                "ARISCAT_Длительность": ar_duration,
                "ARISCAT_Экстренная": ar_emergency
            })

            st.success("Данные сохранены, вы будете перенаправлены на следующую страничку")
            time.sleep(1)
            next_router()

    show_button_down()
