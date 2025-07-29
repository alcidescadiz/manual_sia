import streamlit as st

def page_configuraciones():
    st.title("⚙️ Configuraciones")
    # insertar una imagen img/configuraciones.jpg
    st.image("img/configuraciones.jpg")
    st.write("""
    Este módulo centraliza los parámetros generales del sistema, permitiendo personalizar su funcionamiento:

    ✅ Nombre de la empresa.

    ✅ Datos para el pago movil, el cual se envia a los clientes con cuentas por cobrar pendientes.
    """)