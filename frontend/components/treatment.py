import streamlit as st
import pandas as pd

from backend.logic.medicine import get_parameters_ivl, get_induction_dose, get_infusion_dose, get_end_operation_dose
from backend.logic.recomendations import generate_recommendations


def show_treatment():
    """Отображает диагностические данные пациента с учетом шкалы Caprini."""

    # Отображение в Streamlit
    with st.expander("🧾 Дозировка препаратов"):
        col1, col2 = st.columns(2, border=True)
        with col1:
            st.markdown("**Индукция в анестезию:**")
            result = get_induction_dose(
                st.session_state.scales["idmt"],
                st.session_state.scales["tmt"],
                st.session_state.scales["cmt"]
            )

            df = pd.DataFrame(result)
            df = df.rename(columns={
                "medicine": "Препарат",
                "dose": "Доза",
                "unit": "Ед."
            })
            html_table_scales = df.to_html(index=False)

            st.markdown(html_table_scales, unsafe_allow_html=True)

        with col2:
            st.markdown("**Поддержание в анестезии:**")
            result = get_infusion_dose(
                st.session_state.scales["idmt"],
                st.session_state.scales["tmt"],
                st.session_state.scales["cmt"]
            )

            df = pd.DataFrame(result)
            df = df.rename(columns={
                "medicine": "Препарат",
                "dose": "Доза",
                "unit": "Ед."
            })
            html_table_scales = df.to_html(index=False)

            st.markdown(html_table_scales, unsafe_allow_html=True)

        col3, col4 = st.columns(2, border=True)
        with col3:
            st.markdown("**По окончанию операции:**")
            result = get_end_operation_dose(
                st.session_state.scales["idmt"],
                st.session_state.scales["tmt"],
                st.session_state.scales["cmt"]
            )

            df = pd.DataFrame(result)
            df = df.rename(columns={
                "medicine": "Препарат",
                "dose": "Доза",
                "unit": "Ед."
            })
            html_table_scales = df.to_html(index=False)

            st.markdown(html_table_scales, unsafe_allow_html=True)
        # dictionary = get_medicine_dose_table(st.session_state.scales["tmt"], st.session_state.scales["cmt"])
        # st.table(dictionary)


def show_ivl():
    """Отображает параметры ИВЛ без заголовка 'value'."""
    with st.expander("🧾 Параметры ИВЛ и рекомендации"):
        dictionary = get_parameters_ivl(
            st.session_state.scales["idmt"],
            st.session_state.scales["elganzouri"][1][0]
        )
        df = pd.DataFrame(dictionary.items(), columns=["Параметр", "Значение"])
        df["Значение"] = df["Значение"].astype(str)
        st.dataframe(df, hide_index=True)


def show_recommendations_pp():
    # Словарь соответствий файла уровням риска
    with st.expander("💡 Рекомендации по ведению в послеоперационном периоде"):
        base_text = generate_recommendations(st.session_state["scales"]["caprini"][1])
        st.markdown(base_text, unsafe_allow_html=True)
    return base_text
