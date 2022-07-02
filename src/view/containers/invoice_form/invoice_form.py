import streamlit as st
from ...services import fetch
from ...components import form_controller
from .options import years_options, month_options, get_month_index


def create_invoice_form() -> None:
    with st.form("invoice_form"):
        year: int = form_controller(
            "select", title="請選擇年份", options=years_options, index=1
        )
        month: str = form_controller(
            "select", title="請選擇月份", options=month_options, index=get_month_index()
        )
        submitted = st.form_submit_button("Submit")

        if submitted:
            month = month[1] if month[0] == "0" else month[:2]
            result = fetch("get_data", month, year)

            if isinstance(result, str):
                st.error(result)

            return result
