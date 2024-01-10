import os
import streamlit as st
import litellm
import time
from streamlit_tags import st_tags

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
                st.write(
                    "Você ainda não possui um token de API Gemini? Clique no botão abaixo para obter um!"
                )
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


st.markdown("# Gerador de Experiência")
with st.container(border=True):
    col1, col2 = st.columns(2)
    context_input = col1.text_input(
        "Contexto",
        placeholder="Desenvolvimento de ...",
    )

    position_input = col2.text_input(
        "Cargo",
        placeholder="Qual a cargo ocupado?",
    )

    st.markdown("## Stack de Technologias")
    tech_stack_keywords = st_tags(
        label="Palavra chaves:",
        text="Pressione enter para adicionar mais",
        value=["Python", "Streamlit", "Git"],
        suggestions=[
            "React",
            "Node.js",
            "Angular",
            "Vue.js",
            "JavaScript",
            "TypeScript",
            "Python",
            "Java",
            "C#",
            "Ruby",
            "PHP",
            "HTML5",
            "CSS3",
            "SASS/LESS",
            "Bootstrap",
            "Tailwind CSS",
            "SQL",
            "MongoDB",
            "PostgreSQL",
            "GraphQL",
            "Express.js",
            "Django",
            "Flask",
            "Spring Boot",
            "Ruby on Rails",
            "Laravel",
            "ASP.NET",
            "RESTful Web Services",
            "GraphQL APIs",
            "Microservices Architecture",
            "Docker",
            "Kubernetes",
            "Jenkins",
            "Travis CI",
            "Git",
            "GitHub",
            "GitLab",
            "Bitbucket",
            "Jira",
            "Confluence",
            "Agile Methodologies",
            "Scrum",
            "Kanban",
            "Pair Programming",
            "Test-Driven Development (TDD)",
            "Behavior-Driven Development (BDD)",
            "AWS (Amazon Web Services)",
            "Azure",
            "Google Cloud Platform (GCP)",
            "Serverless Architecture",
            "CI/CD Pipelines",
            "GitHub Actions",
            "GitLab CI/CD",
            "Heroku",
            "Netlify",
            "Firebase",
            "JAMstack",
            "Webpack",
            "Babel",
            "Nginx",
            "Apache",
            "Jest",
            "Mocha",
            "Selenium",
            "Cypress",
            "Agile",
            "DevOps",
            "Container Orchestration",
            "Infrastructure as Code (IaC)",
            "Domain-Driven Design (DDD)",
            "Progressive Web Apps (PWA)",
            "Responsive Web Design",
            "Web Accessibility (a11y)",
            "Cross-Browser Compatibility",
            "Elasticsearch",
            "Log Management",
            "Monitoring Tools",
            "Machine Learning",
            "Data Science",
            "Blockchain",
            "Internet of Things (IoT)",
            "Cybersecurity",
            "Websockets",
            "WebAssembly",
            "AR/VR Development",
            "Rust",
            "Go (Golang)",
            "Swift",
            "Kotlin",
            "Unity",
            "Flutter",
            "TensorFlow",
            "PyTorch",
            "Natural Language Processing (NLP)",
            "Computer Vision",
            "Quantum Computing",
        ],
        key="1",
    )

    st.markdown("## Habilidades Interpessoais")
    soft_skills_keywords = st_tags(
        label="Palavra chaves:",
        text="Pressione enter para adicionar mais",
        value=["Trabalho em Equipe", "Comunicação Efetiva", "Flexibilidade"],
        suggestions=[
            "Comunicação Efetiva",
            "Colaboração",
            "Trabalho em Equipe",
            "Resolução de Problemas",
            "Adaptabilidade",
            "Flexibilidade",
            "Pensamento Crítico",
            "Criatividade",
            "Inovação",
            "Empatia",
            "Gestão de Tempo",
            "Resiliência",
            "Liderança",
            "Tomada de Decisão",
            "Auto-Motivação",
            "Aprendizado Contínuo",
            "Negociação",
            "Gerenciamento de Conflitos",
            "Inteligência Emocional",
            "Orientação para Resultados",
            "Proatividade",
            "Habilidades Interpessoais",
            "Respeito à Diversidade",
            "Assertividade",
            "Autoconhecimento",
            "Gestão de Relacionamentos",
            "Compreensão Intercultural",
            "Habilidade de Delegar",
            "Tolerância ao Estresse",
            "Pensamento Analítico",
            "Planejamento Estratégico",
            "Orientação para o Cliente",
            "Habilidade de Influenciar",
            "Compartilhamento de Conhecimento",
            "Feedback Construtivo",
            "Habilidade de Motivar",
            "Ética Profissional",
            "Responsabilidade",
            "Adaptação à Mudança",
            "Auto-Organização",
            "Foco no Cliente",
            "Habilidade de Lidar com a Pressão",
            "Facilidade de Aprendizado",
            "Ética de Trabalho",
            "Confiabilidade",
            "Autenticidade",
        ],
        key="2",
    )

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """
                Objetivo: gerar descrição de uma única experiência para colocar na seção de experiência profissional do currículo

                - Haja como um assistente de currículo.
                - Elabore as opções e gere uma descrição de experiência profissional curta e objetiva
                - Efetiva para chamar atenção de recrutadores
                - Um parágrafo, usar palavras chaves dentro deste único parágrafo dando contexto.
                - Descreva, em formato de lista, as realizações e habilidades desenvolvidas.
                - Destaque cada ponto como um tópico, evidenciando conquistas específicas e habilidades adquiridas. 
                - Certifique-se de que cada ponto inicie com um verbo no passado, indicando ação concluída ou habilidade adquirida. 
                - Estruture o texto para enfatizar as realizações e aquisições de habilidades.
                - Forneça detalhes específicos sobre as áreas de conhecimento adquiridas, destacando habilidades técnicas e interpessoais. 
                - Mantenha a clareza e coesão na estrutura do texto, destacando habilidades técnicas, interpessoais e profissionais. Utilize uma enumeração específica para listar as habilidades técnicas e outra para as habilidades interpessoais.

                Template:
                Concluiu o [contexto], onde [breve descrição do contexto].

                Desenvolveu habilidades fundamentais de [lista de tech skills relevantes], incluindo [exemplos específicos de realizações].

                Demonstrou fortes habilidades de [lista de soft skills relevantes], evidenciando [exemplos específicos de demonstração dessas habilidades].

                Como resultado dessas experiências, obteve benefícios significativos, tais como [enumerar benefícios específicos ou aprendizados], contribuindo para [impacto positivo no contexto].

                [Adicione qualquer informação adicional ou detalhes específicos conforme necessário].
                """,
        },
        {
            "role": "assistant",
            "content": f"""
                Contexto: {context_input}
                Cargo Ocupado: {position_input}

                Tech Skills trabalhadas: {tech_stack_keywords}
                Soft Skills trabalhadas: {soft_skills_keywords}
                """,
        },
    ]


generate_command = st.button(
    "Gerar", disabled=False if os.environ["GEMINI_API_KEY"] else True
)

with st.container(border=True):
    placeholder = st.empty()
    placeholder.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    if generate_command:
        with st.spinner("Pensando..."):
            time.sleep(0.5)
            placeholder.markdown(
                "<div style='height: 0px;'></div>", unsafe_allow_html=True
            )
            assistant_response = get_assistant_response()
            placeholder.write(assistant_response)
