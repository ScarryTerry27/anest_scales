import streamlit as st

from backend.logic.recomendations import generate_monitoring


def show_monitoring():

    bmi = st.session_state.scales["bmi"][0]
    base_text = generate_monitoring(bmi)
    # Отображение в Streamlit
    with st.expander("🧾 Интраоперационный мониторинг"):
        st.markdown(base_text, unsafe_allow_html=True)
