import streamlit as st
import urllib.parse

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Registro Aliados CLS", page_icon="📝", layout="centered")

# --- ESTILO PARA CELULARES ---
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
    .instruccion-camara {
        background-color: #fff3e0;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #ff9800;
        font-size: 14px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #01579b;'>📝 REGISTRO DE FLETEROS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>CONEXIÓN LOGÍSTICA SUR</p>", unsafe_allow_html=True)

# --- FORMULARIO ---
with st.form("form_registro"):
    st.subheader("1. Datos del Fletero")
    nombre = st.text_input("Nombre y Apellido completo:")
    celular_fletero = st.text_input("Tu número de celular:")
    ciudad = st.text_input("Ciudad y Departamento:")

    st.markdown("---")
    st.subheader("2. Documentación (Cámara Trasera)")
    
    st.markdown("""
        <div class="instruccion-camara">
            📸 <b>NOTA:</b> Si se abre la cámara frontal, busca el icono 🔄 en la pantalla para cambiar a la cámara trasera.
        </div>
    """, unsafe_allow_html=True)
    
    # Intentamos forzar la cámara trasera con 'label_visibility' y la posición del widget
    foto_ci = st.camera_input("FOTO DE CÉDULA (Usa la cámara de atrás)")
    foto_seguro = st.camera_input("FOTO DE SEGURO (Usa la cámara de atrás)")
    
    st.markdown("---")
    st.subheader("3. Foto del Vehículo")
    st.write("Subí una foto de tu unidad (puede ser actual o de tu galería):")
    foto_vehiculo = st.file_uploader("Seleccionar imagen del vehículo", type=['png', 'jpg', 'jpeg'])

    st.markdown("---")
    st.subheader("4. Acuerdo Legal")
    st.warning("Acepto la responsabilidad de la carga y la comisión del 15% para CLS.")
    acepto = st.checkbox("ACEPTO TÉRMINOS Y CONDICIONES")

    enviar = st.form_submit_button("✅ GUARDAR DATOS")

# --- LÓGICA DE ENVÍO ---
if enviar:
    if nombre and foto_ci and acepto:
        st.balloons()
        
        resumen = (
            f"🚀 *NUEVO REGISTRO DE ALIADO*\n\n"
            f"👤 *Nombre:* {nombre}\n"
            f"📱 *Celular:* {celular_fletero}\n"
            f"📍 *Ciudad:* {ciudad}\n\n"
            f"✅ *Estado:* Datos listos. Enviame las fotos por acá abajo 👇"
        )
        msg_codificado = urllib.parse.quote(resumen)
        
        tu_wa = "59899417716"
        wa_url = f"https://wa.me/{tu_wa}?text={msg_codificado}"

        st.markdown("---")
        st.markdown(f"""
            <div style="background-color: #f1f8e9; padding: 25px; border-radius: 15px; border: 2px solid #2e7d32; text-align: center;">
                <h2 style="color: #2e7d32; margin-top:0;">¡LISTO!</h2>
                <p style="font-size: 18px;">Tocá el botón verde para enviarme los datos. <b>Luego adjuntame las fotos de la Cédula y el Seguro en el chat.</b></p>
                <a href="{wa_url}" target="_blank" class="custom-btn">
                    📲 ENVIAR DATOS A LEONARDO
                </a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("⚠️ Falta completar datos, sacar la foto de la CI o aceptar términos.")

st.sidebar.caption("CLS - Conexión Logística Sur 2026")
