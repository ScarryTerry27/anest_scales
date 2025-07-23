import streamlit as st

from backend.logic.recomendations import generate_diagnostic


def show_diagnostic():
    """Отображает диагностические данные пациента с учетом шкалы Caprini."""

    base_text = generate_diagnostic(soba_recommendation=st.session_state.scales["soba"])

    # Отображение в Streamlit
    with st.expander("🧾 Рекомендованная диагностика пациента"):
        st.markdown(base_text, unsafe_allow_html=True)
