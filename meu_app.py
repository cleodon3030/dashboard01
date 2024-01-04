import streamlit as st 
import pandas as pd
from pathlib import Path 
caminho_projeto = Path()
caminho_arquivo = Path(__file__)
diretorio_arquivo = caminho_arquivo.parent
arquivo = diretorio_arquivo / 'resultados.csv'

#arquivo = str(Path())+'resultados.csv'

#----------Configurando a página  
st.set_page_config(page_title='Dashboard01')

#arquivo = 'c:/treinamento/streamlit/proj01/venv/resultados.csv'
#arquivo = '.\resultados.csv'
with st.container():
    st.write('Meu primeiro site com stremlit 0.0.6.')
    st.title('Título')
    st.subheader('Subheader')
    st.write('Informações sobre os contratos fechados pela empresa Cleo S/A')
    st.write('Quer aprender Pyton? [Clique Aqui](https://www.hashtagtreinamentos.com/curso-python)')
    st.write(f'caminho_projeto :  {caminho_projeto}')
    st.write(f'caminho_arquivo :  {caminho_arquivo}')
    st.write(f'diretorio_arquivo :  {diretorio_arquivo}')
    st.write(f'arquivo :  {arquivo}')


with st.container():
   st.write('---')
#--decorator está associado a uma função logo abaixo dele   
@st.cache_data  
def obter_dados():
    dados = pd.read_csv(arquivo)
    return dados
resultado = obter_dados()
st.write(resultado)
qtde_dias=st.selectbox('Selecione o período',['7d','15d','21d','30d'])
numdias = int(qtde_dias.replace('d',''))
filtro = resultado[-numdias:]
st.area_chart(filtro,x='Data',y='Contratos')