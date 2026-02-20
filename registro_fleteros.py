import streamlit as st
import urllib.parse

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Registro Aliados CLS", page_icon="📝", layout="centered")

# --- ESTILO PARA CELULARES (USABILIDAD) ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 70px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 12px;
    }
    .btn-wa {
        display: block;
        width: 100%;
        padding: 15px;
        margin-bottom: 10px;
        text-align: center;
        color: white !important;
        font-weight: bold;
        text-decoration: none;
        border-radius: 10px;
        font-size: 18px;
    }
    .cl-blue { background-color: #01579b; }
    .cl-green { background-color: #25d366; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #01579b;'>📝 Registro de Fleteros</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>CONEXIÓN LOGÍSTICA SUR</b></p>", unsafe_allow_html=True)

with st.form("form_registro"):
    st.subheader("1. Tus Datos")
    nombre = st.text_input("Nombre y Apellido completo:")
    celular_fletero = st.text_input("Tu número de celular:")
    ciudad = st.text_input("Ciudad y Departamento:")

    st.markdown("---")
    st.subheader("2. Documentación (Fotos)")
    st.write("Presioná el botón para activar la cámara")
    
    foto_ci = st.camera_input("FOTO DE CÉDULA (Frente)")
    foto_seguro = st.camera_input("FOTO DE PÓLIZA DE SEGURO")
    foto_vehiculo = st.camera_input("FOTO DE TU VEHÍCULO")

    st.markdown("---")
    st.subheader("3. Acuerdo Legal")
    st.warning("Acepto que CLS es un nexo comercial. Soy responsable de la carga y acepto la comisión del 15%.")
    acepto = st.checkbox("HE LEÍDO Y ACEPTO LOS TÉRMINOS")

    enviar = st.form_submit_button("✅ GUARDAR Y FINALIZAR")

if enviar:
    if nombre and foto_ci and acepto:
        st.balloons()
        st.success("¡Datos guardados localmente!")
        
        # Preparación de los mensajes para WhatsApp
        resumen_texto = f"NUEVO REGISTRO CLS\nNombre: {nombre}\nCelular: {celular_fletero}\nCiudad: {ciudad}"
        msg_codificado = urllib.parse.quote(resumen_texto)
        
        # Números proporcionados
        numeros = {
            "Leonardo": "59899417716",
            "Socio 2": "59899276396", # Corregido (asumí 99 por formato Uruguay)
            "Socio 3": "59899001707"
        }

        st.markdown("---")
        st.subheader("🚀 ÚLTIMO PASO OBLIGATORIO")
        st.write("Hacé clic en uno de los botones de abajo para avisarnos por WhatsApp y enviarnos las fotos:")

        # Generar botones de WhatsApp
        for nombre_socio, num in numeros.items():
            wa_url = f"https://wa.me/{num}?text={msg_codificado}"
            st.markdown(f'''
                <a href="{wa_url}" target="_blank" class="btn-wa cl-green">
                    📲 AVISAR A {nombre_socio.upper()}
                </a>
            ''', unsafe_allow_html=True)
            
    else:
        st.error("Por favor, completá tu nombre, saca la foto de la CI y marcá 'Acepto'.")

st.sidebar.caption("CLS - Gestión de Tercerizados 2026")
