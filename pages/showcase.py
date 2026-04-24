import streamlit as st
import pandas as pd
from ecomplexity import ecomplexity

pd.set_option('display.max_columns', None)

@st.cache_data
def get_data(uploaded_file ):
    ## Cargamos datos
    data = pd.read_csv(uploaded_file)
    
    # Calculate complexity
    trade_cols = {'time': data.columns[0], 'loc':data.columns[1], 'prod':data.columns[2], 'val':data.columns[3]}

    with st.spinner("Wait for it...", show_time=True):
        cdata = ecomplexity(data, trade_cols)
    st.success("Done!")

    return cdata


@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")


st.title(":material/bar_chart: App para el Cálculo de Medidas de Complejidad")
st.markdown(
    "La aplicación calcula las medidas de Complejidad Económica con el paquete [py-ecomplexity](https://github.com/cid-harvard/py-ecomplexity/tree/master)."
)

if "upload_key" not in st.session_state:
    st.session_state["upload_key"] = 0

uploaded_file = st.file_uploader("**Sube los datos**", key=st.session_state["upload_key"], type=["csv"])

if uploaded_file !=None:

    

    cdata = get_data(uploaded_file)


    st.dataframe(cdata, column_order= tuple(cdata.columns))

    csv = convert_for_download(cdata)

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="data.csv",
        mime="text/csv",
        icon=":material/download:",
    )
