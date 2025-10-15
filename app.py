
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_openai import ChatOpenAI
import streamlit as st

load_dotenv()

st.set_page_config(
    page_icon='assets/stock.png',
    page_title='Stock Assistant'
)
st.header('📦 I am a Stock Assistant')

options = [
    'gpt-3.5-turbo',
    'gpt-4',
    'gpt-4o',
    'gpt-4o-mini'
]
selected_model = st.sidebar.selectbox(
    label='Select the LLM:', 
    options=options
)

question = st.text_input('Ask a question about the stock:')

model = ChatOpenAI(model= selected_model)

db = SQLDatabase.from_uri('sqlite:///estoque.db')


agent = create_sql_agent(
    db=db,
    llm=model,
    agent_type='tool-calling'
)

prompt = '''
Use as ferramentas necessárias para responder perguntas relacionadas ao
estoque de produtos. Você fornecerá insights sobre produtos, preços, 
reposição de estoque e relatórios conforme solicitado pelo usuário.
A resposta final deve ter uma formatação amigável de visualização para o usuário.
Sempre responda em português brasileiro.
Pergunta: {q}
'''
prompt_template = PromptTemplate.from_template(prompt)

if st.button('Send'):
    if question:
        with st.spinner('Generating the answer'):
            response = agent.invoke(
                {
                    'input': prompt.format(q=question)
                }
            )

            st.markdown(response.get('output'))
    
    else:
        st.warning('You need to ask somethink to the agent!')