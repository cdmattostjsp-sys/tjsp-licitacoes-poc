import streamlit as st
import os
import time
import openai

# Configuração da página
st.set_page_config(
    page_title="Synapse.IA – Agente IA para Licitações",
    page_icon="🤖",
    layout="wide"
)

# Título principal
st.title("🤖 Synapse.IA TJSP")
st.markdown("---")

# Inicializa a API da OpenAI com chave vinda do secrets.toml (ou painel do Streamlit)
openai.api_key = st.secrets["openai_api_key"]

# 📁 Biblioteca Integrada
st.subheader("📂 Biblioteca Integrada")
biblioteca_path = "biblioteca"

# Verifica se a pasta existe
if not os.path.exists(biblioteca_path):
    st.error("❌ A pasta `biblioteca` não foi encontrada no repositório.")
    arquivos = []
else:
    arquivos = os.listdir(biblioteca_path)
    if not arquivos:
        st.warning("⚠️ Nenhum arquivo encontrado na pasta `biblioteca`.")
    else:
        st.success(f"✅ {len(arquivos)} arquivo(s) carregado(s) com sucesso:")
        for arquivo in arquivos:
            st.markdown(f"- `{arquivo}`")

# --- Execução Simulada do Agente ---
if arquivos:
    st.markdown("---")
    st.subheader("⚙️ Execução Simulada do Agente")

    opcao = st.selectbox("Selecione um arquivo para processar:", arquivos)

    if st.button("🤖 Processar com agente IA"):
        with st.spinner("Executando agente..."):

            # 1. Lê o conteúdo do arquivo selecionado
            caminho_arquivo = os.path.join(biblioteca_path, opcao)
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                conteudo = f.read()

            # 2. Envia para o GPT-4 (ou GPT-3.5)
            resposta = openai.ChatCompletion.create(
                model="gpt-4",  # ou "gpt-3.5-turbo"
                messages=[
                    {"role": "system", "content": "Você é um especialista em licitações públicas do TJSP."},
                    {"role": "user", "content": f"Com base neste conteúdo, gere um resumo técnico: \n\n{conteudo}"}
                ],
                temperature=0.3,
                max_tokens=800
            )

            resultado = resposta["choices"][0]["message"]["content"]

            # 3. Exibe a resposta no app
            st.success("✅ Agente executado com sucesso!")
            st.markdown("### 🧠 Resultado do agente IA:")
            st.write(resultado)
