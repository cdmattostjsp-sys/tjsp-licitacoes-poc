import streamlit as st
import os
import time
import openai

from docx import Document  # para arquivos .docx
import PyPDF2  # para arquivos .pdf

# Configuração da página
st.set_page_config(
    page_title="Synapse.IA – Agente IA para Licitações",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Synapse.IA TJSP")
st.markdown("---")

openai.api_key = st.secrets["openai_api_key"]

# Biblioteca integrada
st.subheader("📂 Biblioteca Integrada")
biblioteca_path = "biblioteca"

# Verifica se a pasta existe
if not os.path.exists(biblioteca_path):
    st.error("❌ A pasta `biblioteca` não foi encontrada.")
    arquivos = []
else:
    arquivos = os.listdir(biblioteca_path)
    if not arquivos:
        st.warning("⚠️ Nenhum arquivo encontrado na biblioteca.")
    else:
        st.success(f"✅ {len(arquivos)} arquivo(s) carregado(s):")
        for arquivo in arquivos:
            st.markdown(f"- `{arquivo}`")

# Execução simulada
if arquivos:
    st.markdown("---")
    st.subheader("⚙️ Execução Simulada do Agente")

    opcao = st.selectbox("Selecione um arquivo para processar:", arquivos)

    if st.button("🤖 Processar com agente IA"):
        with st.spinner("Executando agente..."):

            caminho_arquivo = os.path.join(biblioteca_path, opcao)

            # Função para extrair o conteúdo com base no tipo do arquivo
            def extrair_texto(caminho):
                if caminho.endswith(".txt"):
                    with open(caminho, "r", encoding="utf-8") as f:
                        return f.read()
                elif caminho.endswith(".docx"):
                    doc = Document(caminho)
                    return "\n".join([p.text for p in doc.paragraphs])
                elif caminho.endswith(".pdf"):
                    with open(caminho, "rb") as f:
                        leitor = PyPDF2.PdfReader(f)
                        texto = ""
                        for pagina in leitor.pages:
                            texto += pagina.extract_text()
                        return texto
                else:
                    return "❌ Tipo de arquivo não suportado."

            conteudo = extrair_texto(caminho_arquivo)

            if "Tipo de arquivo não suportado" in conteudo:
                st.error(conteudo)
            else:
                resposta = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "Você é um especialista em licitações públicas do TJSP."},
                        {"role": "user", "content": f"Com base neste conteúdo, gere um resumo técnico:\n\n{conteudo}"}
                    ],
                    temperature=0.3,
                    max_tokens=800
                )

                resultado = resposta["choices"][0]["message"]["content"]

                st.success("✅ Agente executado com sucesso!")
                st.markdown("### 🧠 Resultado do agente IA:")
                st.write(resultado)
 com sucesso!")
            st.markdown("### 🧠 Resultado do agente IA:")
            st.write(resultado)
