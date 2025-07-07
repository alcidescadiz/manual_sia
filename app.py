import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="S.I.A",
    page_icon="🏠",
    initial_sidebar_state="expanded",
    layout="centered", )

st.markdown(
    """
    <style>
        .st-key-add_action button{
            background-color: green;
            color: white;
        }
        footer {visibility: hidden;}
    </style>
    """, 
    unsafe_allow_html=True
)


def main():
    with st.sidebar: 
        selected = option_menu( 
            menu_title="Manual S.I.A", 
            options=["Bienvenido","Productos", "Clientes", "Tipos de Ventas", "Tipos de Pagos", "Gastos", "Ventas", "Cuentas por Cobrar", "Configuraciones"], 
            menu_icon="cast", 
            default_index=0, 
        )

    if selected == "Bienvenido":
        st.title("Bienvenido")
    elif selected == "Productos":
        st.title("Productos")
    elif selected == "Clientes":
        st.title("Clientes")
    elif selected == "Tipos de Ventas":
        st.title("Tipos de Ventas")
    elif selected == "Tipos de Pagos":
        st.title("Tipos de Pagos")
    elif selected == "Gastos":
        st.title("Gastos")
    elif selected == "Ventas":
        st.title("Ventas")
    elif selected == "Cuentas por Cobrar":
        st.title("Cuentas por Cobrar")
    elif selected == "Configuraciones":
        st.title("Configuraciones")


main()