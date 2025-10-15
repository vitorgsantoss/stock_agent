# Stock Agent

Com o Agente de Estoque, é possível acessar registros do banco de dados de maneira amigável, fazendo com que muito tempo seja poupado na busca por informações.
Este é um agente criado com Langchain utilizando ferramentas SQL para buscar dados atravéz de linguagem natural, Streamlit para a interface do usuário e a API da OpenAI para processar as requisições.

## Configuração do Ambiente

### 1. Crie um Ambiente Virtual

Para manter as dependências do projeto isoladas, crie um ambiente virtual:

```bash
python -m venv venv
```

E ative-o:

**No Windows:**
```bash
venv\Scripts\activate
```

**No macOS e Linux:**
```bash
source venv/bin/activate
```

### 2. Instale as Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias a partir do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Configure a Chave da API

Este projeto utiliza a API da OpenAI. Você precisará de uma chave de API para que ele funcione.

1.  Crie um arquivo chamado `.env` na raiz do projeto.
2.  Copie o conteúdo do arquivo `.env.example` para o novo arquivo `.env`.
3.  Adicione sua chave da API da OpenAI ao arquivo `.env`:

```
OPENAI_API_KEY='sua-chave-de-api-aqui'
```

## Como Executar a Aplicação

Depois de configurar o ambiente e a chave da API, você pode iniciar a aplicação Streamlit com o seguinte comando:

```bash
streamlit run app.py
```

A aplicação estará disponível no seu navegador no endereço `http://localhost:8501`.
