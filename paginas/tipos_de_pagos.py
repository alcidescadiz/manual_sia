import streamlit as st

def page_tipos_de_pagos():
    st.title("💳 Módulo de Tipos de Pagos")
    st.write("""
    Este módulo ofrece control sobre las distintas formas de pago admitidas, como:

    ✅ Efectivo, transferencias, pagos móviles, Zelle, divisas, entre otros.

    ✅ Asignación de tasas de cambio en tiempo real si aplica.

    ✅ Combinación de múltiples métodos en una misma transacción.
    """)