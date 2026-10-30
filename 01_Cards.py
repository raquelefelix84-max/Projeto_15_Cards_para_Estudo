import streamlit as st
import json
import random

st.set_page_config(
    page_title="Meus Cards",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Meus Cards")

st.write(
    "Carregue um arquivo JSON com perguntas e respostas "
    "para começar a estudar."
)

st.markdown("---")

arquivo = st.file_uploader(
    "Selecione seu arquivo de cards",
    type=["json"]
)

if arquivo is not None:

    try:
        cards = json.load(arquivo)

        if not isinstance(cards, dict):
            st.error(
                "O arquivo precisa possuir perguntas e respostas."
            )
            st.stop()

        if len(cards) == 0:
            st.warning("O arquivo não possui cards.")
            st.stop()

        st.success(
            f"✅ {len(cards)} cards carregados!"
        )

        # Guarda cards na sessão
        st.session_state["cards"] = cards

        if "pergunta_atual" not in st.session_state:
            st.session_state["pergunta_atual"] = random.choice(
                list(cards.keys())
            )

        pergunta = st.session_state["pergunta_atual"]

        st.markdown("---")

        st.subheader("❓ Pergunta")

        st.info(pergunta)

        if st.button(
            "👀 Mostrar resposta",
            use_container_width=True
        ):
            st.session_state["mostrar_resposta"] = True

        if st.session_state.get("mostrar_resposta", False):

            st.subheader("💡 Resposta")

            st.success(cards[pergunta])

        st.markdown("---")

        if st.button(
            "🔄 Outra pergunta",
            use_container_width=True
        ):

            st.session_state["pergunta_atual"] = random.choice(
                list(cards.keys())
            )

            st.session_state["mostrar_resposta"] = False

            st.rerun()

    except json.JSONDecodeError:
        st.error(
            "❌ O arquivo selecionado não contém um JSON válido."
        )

    except Exception as erro:
        st.error(f"Erro ao carregar os cards: {erro}")

else:

    st.info(
        "👆 Selecione um arquivo JSON para começar."
    )