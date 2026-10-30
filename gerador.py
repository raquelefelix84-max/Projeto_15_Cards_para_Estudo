from groq import Groq
from dotenv import load_dotenv
import os
import json

# Carrega as variáveis do arquivo .env
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

# Cria o client da Groq
client = Groq(api_key=API_KEY)


class Gerador:
    def __init__(self, modelo):
        self.model = modelo
    
    def gerar_perguntas(self, tema: str) -> dict:
        prompt = {
            "role" : f"Você é um especialista no tema: {tema}.",
            "tone" : ["Educado", "Didático"],
            "context" : f"Alunos da universidade precisam de ajuda para estudar o tema: {tema} através de um aplicativo de perguntas e respostas.",
            "task" : f"Você deve gerar 10 perguntas e respostas didáticas para sobre o tema: {tema}.",
            "constraints" : ["O output deve ser uma json string com 10 pares {pergunta : resposta}", 
                            "Não retorne nenhum texto à mais, apenas a json string respeitando o formato explícito em output_format", 
                            "Todas as perguntas devem se parecer com uma pergunta de prova.",
                            "Cada chave da json string deve ser uma pergunta sobre o tema, e cada valor deve ser a resposta correspondente à pergunta",
                            "As chaves não devem ser: Pergunta_1, Pergunta_2 etc... elas devem ser perguntas reais"],
            "example" : "{'Ao que o tema se refere?' : 'O tema se refere à...', 'Onde aplicamos o conceito...? : 'O conceito é aplicado quando...' }",
            "output_format": """{"pergunta_1": "resposta_1", "pergunta_2":"resposta_2"}""",
        }
    
        try:
            resposta = client.chat.completions.create(
                model=self.model,
                messages=[{
                    "role" : "user",
                    "content" : json.dumps(prompt)
                }]
            )
            return json.loads(resposta.choices[0].message.content)
        
        except Exception as e:
            print(f'Erro: {e}')
            return e


if '__main__' == __name__:
    g = Gerador("openai/gpt-oss-120b")

    dados = g.gerar_perguntas('Python Básico')
    print(dados)


import streamlit as st

st.set_page_config(
    page_title="Study Cards",
    page_icon="🧠",
    layout="wide"
)

# SIDEBAR
st.sidebar.title("🧠 Study Cards")
st.sidebar.markdown("---")
st.sidebar.write("Escolha uma página no menu para começar.")

# BODY
st.title("🧠 Study Cards", text_alignment="center")

st.subheader(
    "Estude qualquer assunto com cards de perguntas e respostas.",
    text_alignment="center"
)

st.markdown("---")

st.write(
    """
    Crie cards com inteligência artificial a partir de um tema
    ou carregue cards que você já possui.

    Depois é só estudar, responder e revisar no seu ritmo.
    """
)

st.header("🚀 Por onde começar")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📚 Meus Cards")
    st.write(
        """
        Abra um arquivo JSON com perguntas e respostas
        e comece a estudar.
        """
    )

with col2:
    st.subheader("✨ Gerar Cards com IA")
    st.write(
        """
        Digite um tema como "Revolução Francesa" ou
        "Fundamentos de Python" e a IA cria os cards.
        """
    )

st.markdown("---")

st.header("⚙️ Como funciona")

st.markdown(
    """
    1. **Escolha a origem:** informe um tema ou carregue seus cards.
    2. **Gere ou carregue:** a IA cria as perguntas ou o sistema lê seu arquivo.
    3. **Estude:** tente responder antes de visualizar a resposta.
    4. **Revise:** continue praticando com novas perguntas.
    """
)

st.markdown("---")

st.header("🎯 Por que estudar com cards?")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🧠 Memorização")
    st.write("Ajuda a recuperar informações da memória.")

with col2:
    st.subheader("🔎 Identificação")
    st.write("Mostra quais assuntos ainda precisam de revisão.")

with col3:
    st.subheader("⏱️ Revisão rápida")
    st.write("Permite estudar em sessões curtas e objetivas.")

st.markdown("---")

st.info(
    "Os cards são gerados por IA. Confira as respostas antes "
    "de utilizá-las como referência."
)

st.success("👈 Escolha uma opção no menu lateral para começar!")