import streamlit as st
import urllib.parse

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Registro Aliados CLS", page_icon="📝", layout="centered")

# --- ESTILO PARA CELULARES (DISEÑO DEDUCTIVO) ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 70px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 12px;
        background-color: #01579b;
        color: white;
    }
    .main-title {
        text-align: center;
        color: #01579b;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .custom-btn {
        display: block;
        width: 100%;
        padding: 20px;
        background-color: #25d366;
        color: white !important;
        text-align: center;
        font-weight: bold;
        font-size: 22px;
        text-decoration: none;
        border-radius: 12px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>📝 REGISTRO DE FLETEROS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>CONEXIÓN LOGÍSTICA SUR</p>", unsafe_allow_html=True)

# --- FORMULARIO ---
with st.form("form_registro"):
    st.subheader("1. Datos del Fletero")
    nombre = st.text_input("Nombre y Apellido completo:")
    celular_fletero = st.text_input("Tu número de celular:")
    ciudad = st.text_input("Ciudad y Departamento:")

    st.markdown("---")
    st.subheader("2. Documentación (Sacar Fotos)")
    st.info("Al tocar los botones se abrirá tu cámara. Saca la foto y dale a 'Aceptar'.")
    
    foto_ci = st.camera_input("FOTO DE CÉDULA")
    foto_seguro = st.camera_input("FOTO DE SEGURO")
    foto_vehiculo = st.camera_input("FOTO DEL VEHÍCULO")

    st.markdown("---")
    st.subheader("3. Acuerdo Legal")
    st.warning("Declaro que la documentación es verídica, que soy responsable de la carga y acepto la comisión del 15% para CLS.")
    acepto = st.checkbox("ACEPTO LOS TÉRMINOS Y CONDICIONES")

    enviar = st.form_submit_button("✅ GUARDAR DATOS")

# --- LÓGICA DE ENVÍO ---
if enviar:
    if nombre and foto_ci and acepto:
        st.balloons()
        
        # Armamos el mensaje para tu WhatsApp
        resumen = (
            f"🚀 *NUEVO REGISTRO DE ALIADO*\n\n"
            f"👤 *Nombre:* {nombre}\n"
            f"📱 *Celular:* {celular_fletero}\n"
            f"📍 *Ciudad:* {ciudad}\n\n"
            f"✅ *Estado:* Documentación cargada y términos aceptados."
        )
        msg_codificado = urllib.parse.quote(resumen)
        
        # Tu número configurado
        tu_wa = "59899417716"
        wa_url = f"https://wa.me/{tu_wa}?text={msg_codificado}"

        st.markdown("---")
        st.markdown(f"""
            <div style="background-color: #f1f8e9; padding: 25px; border-radius: 15px; border: 2px solid #2e7d32; text-align: center;">
                <h2 style="color: #2e7d32; margin-top:0;">¡DATOS LISTOS!</h2>
                <p style="font-size: 18px;">Para terminar el registro, tocá el botón verde de abajo para enviarnos tu ficha por WhatsApp.</p>
                <a href="{wa_url}" target="_blank" class="custom-btn">
                    📲 ENVIAR REGISTRO A LEONARDO
                </a>
            </div>
        """, unsafe_allow_html=True)
        
    else:
        st.error("⚠️ Falta completar datos, sacar la foto de la CI o aceptar los términos.")

st.sidebar.caption("CLS - Conexión Logística Sur 2026")
