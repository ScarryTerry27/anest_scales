import time

import streamlit as st

from frontend.components.menu import show_button_down, next_router


def show_index_lee():
    st.subheader("🧮 Индекс Lee (RCRI) — оценка кардиального риска")

    with st.form("LEE_SCALE"):
        st.markdown("##### Отметьте все пункты, соответствующие анамнезу пациента:")

        high_risk_surgery = st.checkbox(
            "🔧 Операция высокого риска (например, крупная сосудистая, интраперитонеальная, торакальная)",
            value=st.session_state.patient_data.get("LEE_Операция", False)
        )

        ischemic_heart_disease = st.checkbox(
            "❤️ Ишемическая болезнь сердца (инфаркт, стенокардия, Q-зубец, терапия нитратами и т.д.)",
            value=st.session_state.patient_data.get("LEE_ИБС", False)
        )

        heart_failure = st.checkbox(
            "💔 Хроническая сердечная недостаточность (ХСН)",
            value=st.session_state.patient_data.get("LEE_ХСН", False)
        )

        cva_or_tia = st.checkbox(
            "🧠 Перенесённое ОНМК или транзиторная ишемическая атака (ТИА)",
            value=st.session_state.patient_data.get("LEE_ОНМК", False)
        )

        diabetes_on_insulin = st.checkbox(
            "💉 Сахарный диабет, получающий инсулинотерапию",
            value=st.session_state.patient_data.get("LEE_СД", False)
        )

        creatinine_elevated = st.checkbox(
            "🧪 Повышенный уровень креатинина > 180 мкмоль/л",
            value=st.session_state.patient_data.get("LEE_Креатинин", False)
        )
        if st.form_submit_button("✅ Сохранить"):
            # === Сохраняем в session_state ===
            st.session_state.patient_data.update({
                "LEE_Операция": high_risk_surgery,
                "LEE_ИБС": ischemic_heart_disease,
                "LEE_ХСН": heart_failure,
                "LEE_ОНМК": cva_or_tia,
                "LEE_СД": diabetes_on_insulin,
                "LEE_Креатинин": creatinine_elevated
            })
            st.success("Данные сохранены, вы будете перенаправлены на следующую страничку")
            time.sleep(1)
            next_router()

    show_button_down()
