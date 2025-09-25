import streamlit as st
import os

# ---------------------
# 🎯 CONFIGURAÇÕES INICIAIS
# ---------------------
st.set_page_config(page_title="SYNAPSE.IA - PoC TJSP", layout="wide")

# ---------------------
# 🧠 TÍTULO DO APLICATIVO
# ---------------------
st.title("🤖 SYNAPSE.IA – Prova de Conceito • Licitações e Contratos TJSP")

st.markdown("""
> Este é um protótipo funcional para demonstração de um **ecossistema de agentes especializados em contratações públicas**, integrados ao fluxo da Nova Lei de Licitações (Lei 14.133/2021), em ambiente simulado.
""")

st.divider()

# ---------------------
# 📂 ACESSO À BIBLIOTECA DE DOCUMENTOS
# ---------------------
st.subheader("📁 Biblioteca de Documentos de Apoio")

# Caminho para a pasta de documentos
biblioteca_path = "biblioteca"

# Verifica se a pasta existe
if not os.path.exists(biblioteca_path):
    st.warning("⚠️ A pasta 'biblioteca/' ainda não foi criada no repositório.")
else:
    arquivos = os.listdir(biblioteca_path)

    if not arquivos:
        st.info("📂 Nenhum documento foi encontrado na biblioteca. Faça o upload pelo GitHub.")
    else:
        arquivo_escolhido = st.selectbox("Selecione um documento para visualizar:", arquivos)

        if st.button("🔍 Carregar Documento"):
            caminho_arquivo = os.path.join(biblioteca_path, arquivo_escolhido)
            try:
                with open(caminho_arquivo, "rb") as f:
                    conteudo = f.read()

                st.success(f"📄 Documento carregado: `{arquivo_escolhido}`")

                # Exibir conteúdo se for texto ou PDF
                if arquivo_escolhido.endswith(".txt"):
                    st.text(conteudo.decode("utf-8"))
                elif arquivo_escolhido.endswith(".pdf"):
                    st.info("Visualização de PDF não implementada nesta versão.")
                else:
                    st.info("Visualização de arquivos deste tipo ainda não está disponível nesta versão.")
            except Exception as e:
                st.error(f"Erro ao abrir o arquivo: {e}")

# ---------------------
# 📌 DEMONSTRAÇÃO BÁSICA DE AGENTES
# ---------------------
st.divider()
st.subheader("🔧 Simulação de Execução de Agente Especializado")

agente = st.selectbox("Escolha um agente para executar:", [
    "Agente DFD (Formalização da Demanda)",
    "Agente ETP (Estudo Técnico Preliminar)",
    "Agente Matriz de Riscos",
    "Agente Minutas e Editais",
    "Agente Contrato Administrativo"
])

if st.button("🚀 Executar Agente"):
    st.success(f"✅ {agente} executado com sucesso.")
    st.write("📄 *Aqui seria exibido o resultado da execução automática, com base em modelos e documentos internos.*")

# ---------------------
# ℹ️ Rodapé
# ---------------------
st.divider()
st.caption("🔒 Este é um ambiente de protótipo desenvolvido para uso institucional no TJSP.")

