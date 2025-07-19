import streamlit as st


def show_characteristics_of_body_weight():
    with st.expander("🧾 Характеристики ожирения пациента"):
        col1, col2 = st.columns(2, border=True)
        with col1:
            bmi_value = round(st.session_state.scales['bmi'][0], 2)
            bmi_text = st.session_state.scales['bmi'][1]
            color = "red" if bmi_value >= 30 else "green"
            st.markdown(
                f"**Индекс массы тела (BMI)</span>",
                unsafe_allow_html=True
            )
            st.markdown(
                f"<span style='color:{color}; font-weight:bold;'>{bmi_value} кг/м^2</span>",
                unsafe_allow_html=True
            )
            st.markdown(
                f"<span style='color:{color}; font-weight:bold;'>{bmi_text}</span>",
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(f"**Идеальная масса тела (ИдМТ):**")
            st.markdown(
                f"<span style='color:blue; font-weight:bold;'>"
                f"{st.session_state.scales['idmt']} кг</span>",
                unsafe_allow_html=True
            )
        col3, col4 = st.columns(2, border=True)
        with col3:
            st.markdown(f"**Тощая масса тела (ТМТ):**")
            st.markdown(
                f"<span style='color:blue; font-weight:bold;'>"
                f"{st.session_state.scales['tmt']} кг</span>",
                unsafe_allow_html=True
            )
        with col4:
            st.markdown(f"**Скорректированная масса тела:**")
            st.markdown(
                f"<span style='color:blue; font-weight:bold;'>"
                f"{st.session_state.scales['cmt']} кг</span>",
                unsafe_allow_html=True
            )
