import streamlit as st

from frontend.components.menu import show_scales
from frontend.forms.scales.ariscat import show_arescat
from frontend.forms.scales.caprini import show_caprini
from frontend.forms.scales.el_ganzouri import show_el_ganzuri
from frontend.forms.scales.index_lee import show_index_lee
from frontend.forms.scales.main_info import show_main_info
from frontend.forms.scales.soba_recomendation import show_soba


def show_sidebar():
    with st.sidebar:
        if st.button("➗ AnestObesity", use_container_width=True):
            st.session_state["stage"] = 0


if __name__ == "__main__":
    stages = {
        0: show_main_info,
        1: show_el_ganzuri,
        2: show_arescat,
        3: show_soba,
        4: show_index_lee,
        5: show_caprini,
        6: show_scales
    }

    if "stage" not in st.session_state:
        st.session_state["stage"] = 0
    if "scales" not in st.session_state:
        st.session_state["scales"] = {}
    if "patient_data" not in st.session_state:
        st.session_state["patient_data"] = {}
    st.set_page_config(page_title="Осмотр пациента", layout="wide")
    show_sidebar()
    stages[st.session_state["stage"]]()


