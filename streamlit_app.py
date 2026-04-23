import streamlit as st

st.set_page_config(
    page_title="Streamlit ECharts Demo",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)

pg = st.navigation(
    [
        st.Page(
            "pages/showcase.py",
            title="Showcase",
            icon=":material/dashboard:",
            default=True,
        ),
        #st.Page("pages/covariables.py", title="Covariables", icon=":material/code:"),
    ]
)
pg.run()

with st.sidebar:
    st.markdown(
        ":material/code: [streamlit-echarts](https://github.com/andfanilo/streamlit-echarts)"
    )
    st.caption("Made in :streamlit: by [@milocortes](https://github.com/milocortes)")