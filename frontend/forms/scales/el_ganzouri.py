import time

import streamlit as st

from frontend.components.menu import show_button_down, next_router


def show_el_ganzuri():
    st.subheader("🧮 Шкала El-Ganzouri — прогноз трудной интубации")

    with st.form("el_ganzuri_form"):
        intubation_history = st.selectbox(
            "Была ли трудная интубация ранее?",
            options=["Нет (0 баллов)", "Недостоверно (+1 балл)", "Определённо (+2 балла)"],
            index=0
        )

        thyromental_distance = st.selectbox(
            "Щитоподбородочное расстояние (см):",
            options=["Более 6.5 см (0 баллов)", "6–6.5 см (+1 балл)", "Менее 6 см (+2 балла)"],
            index=0
        )

        mallampati = st.selectbox(
            "Класс по шкале Mallampati (I–IV):",
            options=["I (0 баллов)", "II (+1 балл)", "III (+2 балла)", "IV (+2 балла)"],
            index=0
        )

        head_angle = st.selectbox(
            "Угол запрокидывания головы:",
            options=["Более 90° (0 баллов)", "80–90° (+1 балл)", "Менее 80° (+2 балла)"],
            index=0
        )

        jaw_movement = st.radio(
            "Пациент может выдвинуть нижнюю челюсть вперёд?",
            options=["Да (0 баллов)", "Нет (+1 балл)"],
            index=0
        )

        mouth_opening = st.radio(
            "Расстояние между резцами:",
            options=["Более 4 см (0 баллов)", "Менее 4 см (+1 балл)"],
            index=0
        )
        if st.form_submit_button("✅ Сохранить"):
            # === Сохраняем в session_state ===
            st.session_state.patient_data.update({
                "ElGanzouri_Интубация": intubation_history,
                "ElGanzouri_Thyromental": thyromental_distance,
                "ElGanzouri_Mallampati": mallampati,
                "ElGanzouri_Голова": head_angle,
                "ElGanzouri_Челюсть": jaw_movement,
                "ElGanzouri_Рот": mouth_opening
            })
            st.success("Данные сохранены, вы будете перенаправлены на следующую страничку")
            time.sleep(1)
            next_router()
    show_button_down()
