import streamlit as st

st.subheader("Roterio para Calçadas")

# --- 1º BLOCO: LARGURA DA CALÇADA ---
largura = st.radio(
    "Escolha a largura da calçada:",
    ["Menos de 1,2m", "Entre 1,2m e 2m", "Maior que 2m"]
)

# --- 2º BLOCO: INTERFERÊNCIAS ---
st.subheader("Existem interferências?")

q1 = st.radio(
    "2.1 Lixeiras ou construções similares que não permitem a passagem de 0,9m de largura com 2,1m de altura?",
    ["Não", "Sim"], index=0
)

q2 = st.radio(
    "2.2 Árvores que não permitem a passagem de 0,9m de largura com 2,1m de altura?",
    ["Não", "Sim"], index=0
)

q3 = st.radio(
    "2.3 O piso possui superfície derrapante?",
    ["Não", "Sim"], index=0
)

q4 = st.radio(
    "2.4 O piso possui pavimento, mas em alguns trechos possui área permeável (piso + grama geralmente)?",
    ["Não", "Sim"], index=0
)

# --- RESULTADOS ---
resultado = []

if largura == "Menos de 1,2m":
    resultado.append("O piso apenas precisa ser pavimentado, não importando existências de lixeiras (ou afins) e árvores.")

elif largura == "Entre 1,2m e 2m":
    if q2 == "Sim":
        resultado.append("O piso deverá ser concretado não importando a existência de árvores.")
    if q1 == "Sim":
        resultado.append("A calçada deverá possuir 1,2m de largura e as lixeiras (ou similares) deverão ser deslocadas.")
    if q4 == "Sim":
        resultado.append("O piso deverá ter 1,2m de largura e ser 100% pavimentado.")
    if q1 == "Não" and q2 == "Não" and q4 == "Não":
        resultado.append("Não se exige acessibilidade, mas o passeio deverá ser pavimentado.")

elif largura == "Maior que 2m":
    resultado.append("Exige-se passeio completo com todos os itens da acessibilidade.")

# Regra independente
if q3 == "Sim":
    resultado.append("O piso deverá possuir superfície antiderrapante.")

# --- EXIBIÇÃO FINAL ---
st.subheader("Resultado")
if resultado:
    for r in resultado:
        st.write("- " + r)
else:
    st.write("Selecione as opções acima para ver o resultado.")
