import streamlit as st
import pandas as pd
from ecomplexity import ecomplexity

st.title(":material/bar_chart: App para el Cálculo de Medidas de Complejidad")
st.markdown(
    "La aplicación calcula las medidas de Complejidad Económica con el paquete [py-ecomplexity](https://github.com/cid-harvard/py-ecomplexity/tree/master)."
)

if "upload_key" not in st.session_state:
    st.session_state["upload_key"] = 0

uploaded_file = st.file_uploader("**Sube los datos**", key=st.session_state["upload_key"], type=["csv"])

if uploaded_file !=None:
    ## Cargamos datos
    data = pd.read_csv(uploaded_file, skiprows = 3)
    
    
    # Calculate complexity
    trade_cols = {'time': data.columns[0], 'loc':data.columns[1], 'prod':data.columns[2], 'val':data.columns[3]}

    with st.spinner("Wait for it...", show_time=True):
        cdata = ecomplexity(data, trade_cols)
    st.success("Done!")

    

    st.dataframe(cdata)

    #st.button("Reset", on_click=reset_uploader)
    #st.session_state["upload_key"] += 1
    #st.success('Se limpio caché', icon="✅")
    ### Booteamos la aplicación para cargar los datos recientemente actualizados
    #st.rerun()
    