import streamlit as st

st.set_page_config(
    page_title='Stock Agent',
    page_icon='/home/vitor/Documentos/PyCodeBR/ia_master/streamlit/stock_agent/assets/stock.png'
)

st.header('Stock Assistant')

selection_options = [
    'gpt-3.5-turbo',
    'gpt-4',
    'gpt-4o-mini',
    'gpt-4o',
    'gpt-4-turbo'
]
model = st.sidebar.selectbox(
    label='Model',
    options = selection_options
)
st.sidebar.markdown('### About')
st.sidebar.markdown('This applicattion is a stock assistant!')