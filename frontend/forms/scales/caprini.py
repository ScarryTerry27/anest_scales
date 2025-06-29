import time

import streamlit as st

from frontend.components.menu import next_router, show_button_down, check_scales, show_scales


def show_caprini():
    st.subheader("🧮 Шкала Caprini — оценка риска ВТЭО")

    with st.form("CAPRINI_SCALE"):
        st.markdown("### 🩺 Медицинские факторы:")

        checkboxes = {
            "Caprini_Отеки": "Отеки нижних конечностей",
            "Caprini_Варикоз": "Варикозные вены",
            "Caprini_Сепсис": "Сепсис (<1 мес)",
            "Caprini_Заболевание_легких": "Тяжёлое заболевание лёгких (<1 мес)",
            "Caprini_Гормоны": "Оральные контрацептивы / ГЗТ",
            "Caprini_Беременность": "Беременность / послеродовый период (<1 мес)",
            "Caprini_Акушерский_анамнез": "Неблагоприятный акушерский анамнез",
            "Caprini_Инфаркт": "Острый инфаркт миокарда",
            "Caprini_ХСН": "Хроническая сердечная недостаточность",
            "Caprini_Постельный": "Постельный режим (актуальный)",
            "Caprini_Постельный_72ч": "Постельный режим > 72 часов",
            "Caprini_Хирургия_анамнез": "Хирургия в анамнезе (<1 мес)",
            "Caprini_ХОБЛ": "ХОБЛ",
            "Caprini_Онкология": "Онкология (текущая / ранее)",
            "Caprini_Иммобилизация": "Иммобилизация конечности (<1 мес)",
            "Caprini_ВТЭО_анамнез": "Анамнез ВТЭО (ТГВ/ТЭЛА)",
            "Caprini_Лейден": "Мутация фактора V (Лейден)",
            "Caprini_Протромбин": "Мутация протромбина 20210A",
            "Caprini_Волчанка": "Волчаночный антикоагулянт",
            "Caprini_Семейный_ВТЭО": "Семейный анамнез ВТЭО",
            "Caprini_Гомоцистеин": "Гипергомоцистеинемия",
            "Caprini_ГИТ": "Гепарин-индуцированная тромбоцитопения",
            "Caprini_Антикардиолипин": "Антитела к кардиолипину",
            "Caprini_Тромбофилия": "Тромбофилия (др.)",
            "Caprini_Инсульт": "Инсульт (<1 мес)",
            "Caprini_Паралич": "Паралич / повреждение спинного мозга (<1 мес)",
            "Caprini_Прочее": "Прочие факторы риска"
        }

        col1, col2, col3 = st.columns(3)
        items = list(checkboxes.items())

        # Распределение по трём колонкам
        for i, (key, label) in enumerate(items):
            col = [col1, col2, col3][i % 3]
            with col:
                st.session_state.patient_data[key] = st.checkbox(
                    label, value=st.session_state.patient_data.get(key, False)
                )

        st.markdown("### 🏥 Факторы, связанные с вмешательством:")

        interventional_checkboxes = {
            "Caprini_Катетер": "Катетеризация центральных вен",
            "Caprini_Малая_хирургия": "Малое хирургическое вмешательство",
            "Caprini_Артроскопия": "Артроскопическая операция",
            "Caprini_Лапароскопия": "Лапароскопия > 60 мин",
            "Caprini_Большая_операция": "Большая операция > 45 мин",
            "Caprini_Травма": "Множественные травмы (< 1 мес)",
            "Caprini_Эндопротез": "Эндопротезирование крупных суставов",
            "Caprini_Перелом": "Перелом костей конечности или таза"
        }

        col4, col5, col6 = st.columns(3)
        items_int = list(interventional_checkboxes.items())

        for i, (key, label) in enumerate(items_int):
            col = [col4, col5, col6][i % 3]
            with col:
                st.session_state.patient_data[key] = st.checkbox(
                    label, value=st.session_state.patient_data.get(key, False)
                )
        if st.form_submit_button("✅ Сохранить"):
            st.success("Данные сохранены, вы будете перенаправлены на следующую страничку")
            time.sleep(1)
            next_router()

    show_button_down()
