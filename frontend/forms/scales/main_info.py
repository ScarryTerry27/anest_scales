import time

import streamlit as st

from frontend.components.menu import show_button_down, next_router


def show_main_info():
    st.subheader("🧾 Общие сведения о пациенте")

    with st.form("MAIN_PATIENT"):
        name = st.text_input("👤 ФИО", value=st.session_state.patient_data.get("ФИО", ""))
        age = st.number_input(
            "🎂 Возраст", min_value=0,
            max_value=120,
            value=st.session_state.patient_data.get("Возраст", 30)
        )
        gender = st.radio(
            "👫 Пол",
            ["Муж", "Жен"],
            index=0 if st.session_state.patient_data.get("Пол", "Муж") == "Муж" else 1
        )

        height = st.number_input(
            "📏 Рост (в см)",
            min_value=100,
            max_value=250,
            value=st.session_state.patient_data.get("Рост", 170)
        )
        weight = st.number_input(
            "⚖️ Вес (в кг)",
            min_value=30,
            max_value=250,
            value=st.session_state.patient_data.get("Вес", 70)
        )

        ar_spo2 = st.number_input("🫁 Дооперационная сатурация:", value=st.session_state.patient_data.get("spo2", 97))
        if st.form_submit_button("✅ Сохранить"):
            st.session_state.patient_data.update({
                "ФИО": name,
                "Возраст": age,
                "Пол": gender,
                "Рост": height,
                "Вес": weight,
                "spo2": ar_spo2
            })
            st.success("Данные сохранены, вы будете перенаправлены на следующую страничку")
            time.sleep(1)
            next_router()
    show_button_down()
