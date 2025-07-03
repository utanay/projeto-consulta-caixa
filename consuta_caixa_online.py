import streamlit as st

st.title("Consulta Meu Caixa")

st.write("Preencha os valores abaixo (use ponto ou vírgula):")

def converter(valor):
    try:
        return float(str(valor).replace(",", ".").strip())
    except:
        return 0.0

valor_abastecimentos = st.text_input("Valor total dos abastecimentos", "0")
valor_relatorio = st.text_input("Dinheiro no relatório", "0")
valor_sangrias = st.text_input("Valor das sangrias", "0")
valor_dinheiro = st.text_input("Dinheiro em caixa", "0")

if st.button("Consultar"):
    try:
        v1 = converter(valor_abastecimentos)
        v2 = converter(valor_relatorio)
        v3 = converter(valor_sangrias)
        v4 = converter(valor_dinheiro)

        total_caixa = v1 + v2
        total_din_sang = v3 + v4
        resultado = total_caixa - total_din_sang

        if resultado > 0:
            st.error(f"❌ Seu caixa está FALTANDO R$ {abs(resultado):.2f}")
        elif resultado < 0:
            st.success(f"✅ Seu caixa está SOBRANDO R$ {abs(resultado):.2f}")
        else:
            st.info("✔️ Seu caixa está CERTINHO!")
    except:
        st.warning("Erro: Verifique os valores digitados.")
