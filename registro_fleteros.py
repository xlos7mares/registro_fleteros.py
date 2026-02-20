import streamlit as st
import pandas as pd

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Registro de Aliados CLS", page_icon="📝", layout="centered")

# --- ESTILO PARA BOTONES GRANDES Y VISIBLES ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        background-color: #01579b;
        color: white;
    }
    .stHeader {
        text-align: center;
        color: #01579b;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📝 Registro de Aliados")
st.markdown("### Conexión Logística Sur")
st.info("Complete los datos y saque las fotos solicitadas. Es rápido y seguro.")

# --- FORMULARIO PASO A PASO ---
with st.form("registro_form"):
    st.subheader("1. Datos Personales")
    nombre = st.text_input("Nombre y Apellido completo:")
    celular = st.text_input("Tu número de WhatsApp:")
    ciudad = st.text_input("¿En qué ciudad vivís?")

    st.markdown("---")
    st.subheader("2. Documentación (Sacar Fotos)")
    
    # Estos botones abren la cámara automáticamente en el celular
    foto_ci = st.camera_input("Sacar foto de tu Cédula (Frente)")
    foto_seguro = st.camera_input("Sacar foto de la Póliza del Seguro")
    foto_vehiculo = st.camera_input("Sacar foto de tu Camión/Camioneta")

    st.markdown("---")
    st.subheader("3. Acuerdo Legal")
    st.write("Al enviar, aceptás trabajar como fletero aliado, siendo responsable de la carga y abonando el 15% de comisión por viaje a CLS.")
    acepto = st.checkbox("ACEPTO LOS TÉRMINOS Y CONDICIONES")

    st.markdown("---")
    # Botón de envío
    enviar = st.form_submit_button("✅ FINALIZAR Y ENVIAR REGISTRO")

# --- LÓGICA DE ENVÍO ---
if enviar:
    if nombre and celular and foto_ci and acepto:
        st.balloons()
        st.success("¡Excelente! Tus datos han sido procesados.")
        
        # Preparamos el resumen para el email
        resumen = f"Nuevo Aliado: {nombre}\nCelular: {celular}\nCiudad: {ciudad}"
        
        # Link para que el fletero te avise por WhatsApp que ya terminó
        msg_wa = f"Hola Leonardo, ya completé mi registro. Mi nombre es {nombre}."
        wa_url = f"https://wa.me/598[TU_NUMERO]?text={resumen}" # Cambia por tu número real
        
        st.markdown(f"""
            <div style="background-color:#e1f5fe; padding:20px; border-radius:10px; text-align:center;">
                <h4>Último Paso</h4>
                <p>Hacé clic en el botón de abajo para enviarnos los documentos por WhatsApp y finalizar.</p>
                <a href="{wa_url}" target="_blank" style="text-decoration:none;">
                    <button style="background-color:#25d366; color:white; border:none; padding:15px; border-radius:5px; width:100%; font-weight:bold;">
                        📱 AVISAR POR WHATSAPP AHORA
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)
        
        # Nota técnica: Streamlit no envía archivos adjuntos a emails directamente sin un servidor SMTP.
        # Por eso, lo más "deductivo" y seguro es que las fotos te lleguen por WhatsApp o queden en tu base de datos.
    else:
        st.warning("Por favor, saca las fotos obligatorias y marca que aceptas los términos.")

st.sidebar.caption("Desarrollado por Leonardo Olivera | CLS Tech 2026")
