import streamlit as st

# ============================================================
# CONFIGURAÇÕES INICIAIS
# ============================================================

st.set_page_config(
    page_title="Study Cards",
    page_icon="🧠",
    layout="wide"
    
)


# ========================= SIDEBAR

st.sidebar.title('Study Cards')


# ========================= BODY
st.title('Study Cards', text_alignment="center")
st.subheader('🧠Estude qualquer assunto com cards de perguntas e respostas.', text_alignment="center")
st.markdown('---')
st.write('Crie cards com inteligência artificial a partir de um tema ou de um texto seu, ou carregue cards que você já tem. Depois é só virar, responder e revisar no seu ritmo.')

st.markdown("""

## Por onde começar

Escolha uma opção no menu à esquerda:

### 📚 Cards
Abra um arquivo de cards que você já tem e comece a estudar.

### ✨ Gerar Cards com IA
Digite um tema, como "Revolução Francesa" ou "Fundamentos de Python", e a IA cria os cards para você.

---

## Como funciona

1. **Escolha a origem:** um tema, um texto ou cards que você já tem.
2. **Gere ou carregue:** a IA cria os cards em poucos instantes.
3. **Estude:** vire os cards, teste sua memória e repita quantas vezes quiser.

---

## Por que estudar com cards?

Reler o conteúdo dá a sensação de que você sabe, mas responder perguntas mostra o que você realmente sabe. Os cards ajudam a lembrar melhor, encontrar lacunas e revisar em sessões curtas.

---

> ℹ️ Os cards são gerados por IA. Vale conferir as respostas, principalmente em assuntos importantes.

**Pronto para começar? Escolha uma opção no menu ao lado.** 👈
""")



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