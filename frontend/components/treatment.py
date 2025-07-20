import streamlit as st

from backend.logic.medicine import get_medicine_dose_table, get_parameters_ivl


def show_treatment():
    """Отображает диагностические данные пациента с учетом шкалы Caprini."""

    # Отображение в Streamlit
    with st.expander("🧾 Дозировка препаратов"):
        dictionary = get_medicine_dose_table(st.session_state.scales["tmt"], st.session_state.scales["cmt"])
        st.table(dictionary)


def show_ivl():
    """Отображает диагностические данные пациента с учетом шкалы Caprini."""

    # Отображение в Streamlit
    with st.expander("🧾 Параметры ИВЛ"):
        dictionary = get_parameters_ivl(st.session_state.scales["idmt"], st.session_state.scales["elganzouri"][1])
        st.table(dictionary)
