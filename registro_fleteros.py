import streamlit as st
import urllib.parse

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Registro Aliados CLS", page_icon="🚛", layout="centered")

# --- ESTILO PARA CELULARES ---
st.markdown("""
    <style>
    .contrato-box {
        background-color: #f1f3f5;
        padding: 15px;
        border-radius: 10px;
        height: 200px;
        overflow-y: scroll;
        font-size: 13px;
        border: 1px solid #ced4da;
    }
    .stButton>button {
        width: 100%;
        height: 70px;
        font-size: 20px;
        font-weight: bold;
        background-color: #01579b;
        color: white;
        border-radius: 12px;
    }
    .btn-final {
        display: block;
        width: 100%;
        padding: 20px;
        background-color: #25d366;
        color: white !important;
        text-align: center;
        font-weight: bold;
        font-size: 22px;
        text-decoration: none;
        border-radius: 15px;
        border: 3px solid #128c7e;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚛 Registro de Fleteros")
st.markdown("### CONEXIÓN LOGÍSTICA SUR")

# --- 1. CONTRATO ---
st.subheader("Contrato de Adhesión y Deslinde")
st.markdown("""
<div class="contrato-box">
<b>ACUERDO DE TRABAJO - CLS</b><br><br>
1. <b>Intermediación:</b> CLS es solo nexo comercial. No hay dependencia.<br>
2. <b>Responsabilidad:</b> El fletero es el único responsable por la carga y daños.<br>
3. <b>Comisión:</b> Se acepta el 15% de comisión por viaje.<br>
4. <b>Documentación:</b> Declaro que los documentos adjuntos son reales y vigentes.
</div>
""", unsafe_allow_html=True)

# --- 2. FORMULARIO ---
with st.form("registro_cls"):
    acepto = st.checkbox("HE LEÍDO Y ACEPTO LOS TÉRMINOS")
    
    st.markdown("---")
    nombre = st.text_input("Nombre y Apellido:")
    celular = st.text_input("Tu número de celular:")
    ciudad = st.text_input("Ciudad / Departamento:")
    domicilio = st.text_input("Domicilio y Nro de Casa:")
    
    st.markdown("---")
    st.subheader("Fotos de Documentación")
    st.info("Prepará las fotos de tu Cédula, Licencia, Libreta, Seguro y Vehículo.")
    
    # Usamos file_uploader para que puedan elegir de la galería o sacar foto
    fotos = st.file_uploader("Subir fotos (Podés seleccionar varias a la vez)", accept_multiple_files=True)

    enviar = st.form_submit_button("✅ GENERAR FICHA DE REGISTRO")

# --- 3. LÓGICA DE SALIDA ---
if enviar:
    if acepto and nombre and celular:
        st.balloons()
        
        # Armamos el texto para WhatsApp
        texto_wa = (
            f"🟢 *NUEVO REGISTRO DE FLETERO - CLS*\n\n"
            f"👤 *Nombre:* {nombre}\n"
            f"📱 *Celular:* {celular}\n"
            f"📍 *Ciudad:* {ciudad}\n"
            f"🏠 *Domicilio:* {domicilio}\n\n"
            f"📝 *Contrato:* Aceptado\n"
            f"---------------------------\n"
            f"¡Hola Leonardo! Acabo de completar mi registro. Ahora te adjunto las fotos de la documentación aquí debajo. 👇"
        )
        
        wa_url = f"https://wa.me/59899417716?text={urllib.parse.quote(texto_wa)}"
        
        st.success("¡Ficha generada con éxito!")
        
        st.markdown(f"""
            <div style="background-color: #f1f8e9; padding: 25px; border-radius: 15px; text-align: center;">
                <h2 style="color: #2e7d32;">¡ÚLTIMO PASO!</h2>
                <p style="font-size: 18px;">Tocá el botón verde para enviarme la ficha a mi WhatsApp y <b>luego adjuntame las fotos en el chat.</b></p>
                <a href="{wa_url}" target="_blank" class="btn-final">
                    📲 ENVIAR REGISTRO POR WHATSAPP
                </a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Por favor, aceptá el contrato y completá tus datos.")

st.sidebar.caption("CLS - Gestión Logística 2026")
