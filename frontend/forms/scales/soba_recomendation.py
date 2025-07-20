import time

import streamlit as st

from frontend.components.menu import next_router, show_button_down


def show_soba():
    st.markdown("### 🧮 Рекомендации SOBA и шкала STOP-BANG")

    with st.form("SOBA_SCALE"):
        st.markdown("#### 📋 Критерии SOBA:")
        func_data = st.checkbox(
            "🔬 Плохие функциональные данные",
            value=st.session_state.patient_data.get("SOBA_Функция", False)
        )
        ecg_changes = st.checkbox("📉 Изменения на ЭКГ", value=st.session_state.patient_data.get("SOBA_ЭКГ", False))
        uncontrolled_ag = st.checkbox(
            "💊 Неконтролируемая гипертензия или ИБС",
            value=st.session_state.patient_data.get("SOBA_АГ", False)
        )
        thrombo_history = st.checkbox(
            "🧨 ТГВ / ТЭЛА в анамнезе",
            value=st.session_state.patient_data.get("SOBA_ТГВ", False)
        )

        co2 = st.checkbox(
            "🧪 Уровень HCO₃⁻ (мм рт. ст.) > 28",
            value=st.session_state.patient_data.get("SOBA_CO2", False)
        )

        st.markdown("#### 📋 Компоненты шкалы STOP-BANG:")

        snoring = st.checkbox(
            "😴 Громкий храп (слышен через дверь или громче речи)",
            value=st.session_state.patient_data.get("STOPBANG_Храп", False)
        )
        tired = st.checkbox(
            "😵 Частая дневная сонливость/утомляемость",
            value=st.session_state.patient_data.get("STOPBANG_Сонливость", False)
        )
        observed_apnea = st.checkbox(
            "🛌 Замеченные остановки дыхания во сне",
            value=st.session_state.patient_data.get("STOPBANG_Апноэ", False)
        )
        hypertension = st.checkbox(
            "💊 Артериальная гипертензия (диагностирована)",
            value=st.session_state.patient_data.get("STOPBANG_Давление", False)
        )
        neck = st.checkbox(
            "📏 Обхват шеи (в см) > 40",
            value=st.session_state.patient_data.get("STOPBANG_Шея", False)
        )

        if st.form_submit_button("✅ Сохранить"):
            # Сохраняем всё в session_state
            st.session_state.patient_data.update({
                # SOBA
                "SOBA_Функция": func_data,
                "SOBA_ЭКГ": ecg_changes,
                "SOBA_АГ": uncontrolled_ag,
                "SOBA_ТГВ": thrombo_history,
                "SOBA_CO2": co2,
                # STOP-BANG
                "STOPBANG_Храп": snoring,
                "STOPBANG_Сонливость": tired,
                "STOPBANG_Апноэ": observed_apnea,
                "STOPBANG_Давление": hypertension,
                "STOPBANG_Шея": neck,
            })

            st.success("Данные сохранены, вы будете перенаправлены на следующую страничку")
            time.sleep(1)
            next_router()

    show_button_down()


