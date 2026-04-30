import streamlit as st
from database import fetch_material_type
from services import validar_fluxo_material

# Configurações Iniciais
st.set_page_config(page_title="Portal Sparetech", layout="centered")

def apply_custom_css():
    st.markdown("""
        <style>
        .stButton>button { width: 100%; border-radius: 5px; background-color: #004a80; color: white; }
        </style>
    """, unsafe_allow_html=True)

def main():
    apply_custom_css()
    st.title("Portal de Acesso Sparetech")
    
    operacao = st.selectbox("O que você deseja realizar?", ["Selecione...", "Criação", "Extensão / Alteração"])

    if operacao == "Criação":
        st.success("Operação de Criação identificada.")
        if st.button("Acessar Sparetech"):
            st.info("Redirecionando para Sparetech...")

    elif operacao == "Extensão / Alteração":
        codigo = st.text_input("Digite o código do material existente:").upper().strip()

        if codigo:
            with st.spinner('Validando base global...'):
                tipo_mat = fetch_material_type(codigo)

            if tipo_mat:
                fluxo = validar_fluxo_material(tipo_mat)
                
                if fluxo:
                    if fluxo["status"] == "warning": st.warning(fluxo["msg"])
                    else: st.success(fluxo["msg"])
                    
                    if st.button(fluxo["label"]):
                        st.write(f"Link: {fluxo['url']}")
                else:
                    st.error("Tipo de material não suportado pelo fluxo automático.")
            else:
                st.error("Código não encontrado na base de dados.")

if __name__ == "__main__":
    main()
