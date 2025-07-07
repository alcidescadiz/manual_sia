import streamlit as st
from streamlit_option_menu import option_menu
from paginas.bienvenido import page_bienvenido
from paginas.productos import page_productos
from paginas.clientes import page_clientes
from paginas.tipos_de_ventas import page_tipos_de_ventas
from paginas.tipos_de_pagos import page_tipos_de_pagos
from paginas.gastos import page_gastos
from paginas.ventas import page_ventas
from paginas.cuentas_por_cobrar import page_cuentas_por_cobrar
from paginas.configuraciones import page_configuraciones

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
        page_bienvenido()
    elif selected == "Productos":
        page_productos()
    elif selected == "Clientes":
        page_clientes()
    elif selected == "Tipos de Ventas":
        page_tipos_de_ventas()
    elif selected == "Tipos de Pagos":
        page_tipos_de_pagos()
    elif selected == "Gastos":
        page_gastos()
    elif selected == "Ventas":
        page_ventas()
    elif selected == "Cuentas por Cobrar":
        page_cuentas_por_cobrar()
    elif selected == "Configuraciones":
        page_configuraciones()


main()