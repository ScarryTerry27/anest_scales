import streamlit as st
import pandas as pd


def show_an_ream_risk():
    """Отображает оценку анестезиолого-операционного риска."""

    with st.expander("🧮 Оценка анестезиолого-операционного риска"):
        data = {
            "Показатель": [
                "Риск ВТЭО",
                "Риск сердечно сосудистых осложнений",
                "Риск послеоперационных легочных осложнений",
                "Риск трудных дыхательных путей",
                "Риск синдрома обструктивного апноэ сна",
                "Риск SOBA"
            ],
            "Интерпретация": [
                st.session_state.scales["caprini"][1],
                st.session_state.scales["lee"][1][1],
                f"{st.session_state.scales["ariscat"][1][0]}",
                st.session_state.scales["elganzouri"][1][1],
                ["Высокий", "Низкий"][st.session_state.scales["stopbang"] <= 5],
                ["Низкий", "Высокий"][st.session_state.scales["soba"]]
            ],
            "Баллы": [
                st.session_state.scales["caprini"][0],
                st.session_state.scales["lee"][0],
                st.session_state.scales["ariscat"][0],
                st.session_state.scales["elganzouri"][0],
                st.session_state.scales["stopbang"],
                "-"
            ],
            "Шкала": ["Caprini", "Lee", "ARISCAT", "El Ganzouri", "STOP-BANG", "SOBA"]
        }

        # Преобразуем в таблицу
        df_scales = pd.DataFrame(data)
        html_table_scales = df_scales.to_html(index=False)

        st.markdown(html_table_scales, unsafe_allow_html=True)
