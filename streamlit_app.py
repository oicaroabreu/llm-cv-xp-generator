import os
import streamlit as st
import litellm
import time

litellm.set_verbose = True

st.set_page_config(page_title="🤖 llm-cv-xp-generator 📃")

with st.sidebar:
    st.title("🤖 llm-cv-xp-generator 📃")
    st.subheader("Crie seu currículo de desenvolvedor com facilidade!")
    st.write(
        "Desenvolva seu currículo com poderosos modelos de linguagem. Destaque suas habilidades e experiências de forma única e conquiste os recrutadores."
    )

    if "GEMINI_API_KEY" in st.secrets:
        st.success("Token da API Gemini já fornecida!", icon="✅")
        gemini_key = st.secrets["GEMINI_API_KEY"]
    else:
        gemini_key = st.text_input("Inserir Gemini API token:", type="password")

        if not (gemini_key and len(gemini_key) > 0):
            st.warning("Por favor, insira suas credenciais!", icon="⚠️")
            with st.container(border=True):
                st.write("Você ainda não possui um token de API Gemini? Clique no botão abaixo para obter um!")
                col1, col2 = st.columns(2, gap="small")
                col2.link_button("Obter token", "https://ai.google.dev/")
        else:
            st.empty()
            st.success("Agora desfrute!!", icon="👉")
            if "messages" in st.session_state:
                del st.session_state["messages"]


    os.environ["GEMINI_API_KEY"] = gemini_key

    st.markdown(
        "📖 Acesse nosso [Github](https://github.com/oicaroabreu/llm-cv-xp-generator/)"
    )


def get_assistant_response():
    response = litellm.completion(
        model="gemini/gemini-pro",
        messages=st.session_state.messages,
        api_base="http://localhost:11434",
        max_tokens=200,
    )
    print(response)
    return response.choices[0].message.content


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """
                Objetivo: gerar descrição de experiência para colocar no currículo

                - Haja como um assistente de currículo.
                - Elabore as opções e gere uma descrição de experiência profissional curta e objetiva
                - Efetiva para chamar atenção de recrutadores
                - Um parágrafo, usar palavras chaves dentro deste único parágrafo dando contexto.
                """,
        },
        {
            "role": "assistant",
            "content": """
                Contexto: Experiência em contrução de aplicação web

                Docker, Django, Git, Scrum, Pair-Programming, Python, AWS, Microservices, FastAPI, AWS Lambda, CI/CD, Github Actions, REST API
                """,
        }
    ]

generate_command = st.button("Gerar", disabled=False if os.environ["GEMINI_API_KEY"] else True)

with st.container(border=True):
    placeholder = st.empty()
    placeholder.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    if generate_command:
        with st.spinner("Pensando..."):
                time.sleep(0.5)
                placeholder.markdown("<div style='height: 0px;'></div>", unsafe_allow_html=True)
                assistant_response = get_assistant_response()
                placeholder.write(assistant_response)