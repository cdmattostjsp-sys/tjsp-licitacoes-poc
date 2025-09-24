import streamlit as st
from dataclasses import dataclass

@dataclass
class ProcessoLicitatorio:
    etapa: str
    insumos: str
    saida: dict

def executar_agente(etapa, insumos):
    resposta = f"[✔] Documento da etapa '{etapa}' gerado com base em:\\n→ {insumos}"
    return {etapa: resposta}

st.set_page_config(page_title="Agente IA – Licitações TJSP", page_icon="🤖")
st.title("🤖 Agente IA – Licitações e Contratos TJSP")

etapas = [
    "DFD", "ETP", "ITF", "TR",
    "Pesquisa de Preços", "Matriz de Riscos",
    "Minutas/Editais", "Contrato",
    "Fiscalização", "Checklist"
]

etapa = st.selectbox("Selecione a etapa:", etapas)
insumos = st.text_area("Descreva os insumos ou contexto:")

if st.button("Executar Agente"):
    if not insumos.strip():
        st.warning("⚠️ Por favor, preencha os insumos.")
    else:
        processo = ProcessoLicitatorio(etapa=etapa, insumos=insumos, saida={})
        processo.saida = executar_agente(processo.etapa, processo.insumos)
        st.success("✅ Agente executado com sucesso!")
        st.subheader("📄 Resultado")
        st.code(processo.saida[etapa], language="markdown")

st.markdown("---")
st.caption("PoC desenvolvida para a Secretaria de Administração e Abastecimento – TJSP")
