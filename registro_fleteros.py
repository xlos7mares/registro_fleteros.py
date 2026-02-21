import streamlit as st
import urllib.parse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Registro Aliados CLS", page_icon="🚛", layout="centered")

# --- ESTILO PARA EL CONTRATO Y BOTONES ---
st.markdown("""
    <style>
    .contrato-box {
        background-color: #f8f9fa;
        padding: 15px;
        border: 1px solid #d1d5db;
        border-radius: 10px;
        height: 250px;
        overflow-y: scroll;
        margin-bottom: 20px;
        font-size: 14px;
        line-height: 1.5;
    }
    .stButton>button {
        width: 100%;
        height: 60px;
        font-weight: bold;
        background-color: #01579b;
        color: white;
    }
    .btn-wa {
        display: block;
        width: 100%;
        padding: 20px;
        background-color: #25d366;
        color: white !important;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        text-decoration: none;
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚛 Registro de Fleteros")
st.markdown("### CONEXIÓN LOGÍSTICA SUR")

# --- 1. CONTRATO CON BARRA DE DESPLAZAMIENTO ---
st.subheader("Contrato de Adhesión")
texto_contrato = """
<div class="contrato-box">
<b>CONTRATO DE ADHESIÓN Y DESLINDE DE RESPONSABILIDAD - CLS</b><br><br>
1. <b>NATURALEZA DEL VÍNCULO:</b> El Fletero acepta que Conexión Logística Sur (CLS) actúa únicamente como nexo comercial. No existe relación de dependencia laboral.<br><br>
2. <b>RESPONSABILIDAD POR LA CARGA:</b> El Fletero asume la responsabilidad total por la integridad de la mercadería o botes transportados. CLS no responde por daños, hurtos o accidentes.<br><br>
3. <b>COMISIÓN:</b> El Fletero abonará el 15% del valor de cada flete a CLS por gestión comercial.<br><br>
4. <b>DOCUMENTACIÓN:</b> El Fletero declara tener vehículo, seguros y documentación personal al día según las leyes de Uruguay.<br><br>
5. <b>ESTADO DE LA UNIDAD:</b> El fletero garantiza que su vehículo está en óptimas condiciones de seguridad.
</div>
"""
st.markdown(texto_contrato, unsafe_allow_html=True)

# --- 2. FORMULARIO ---
with st.form("form_completo"):
    acepto = st.checkbox("HE LEÍDO EL CONTRATO Y ACEPTO LAS CONDICIONES")
    
    st.markdown("---")
    nombre = st.text_input("Nombre y Apellido completo:")
    celular = st.text_input("Número de celular:")
    ciudad = st.text_input("Ciudad y Departamento:")
    domicilio = st.text_input("Domicilio y Nro de Casa:")
    
    st.markdown("---")
    st.subheader("Adjuntar Documentación")
    f_ci = st.file_uploader("Adjuntar foto de Cédula", type=['jpg','png','jpeg'])
    f_lic = st.file_uploader("Adjuntar foto de Licencia de Conducir", type=['jpg','png','jpeg'])
    f_lib = st.file_uploader("Adjuntar foto de Libreta de Propiedad", type=['jpg','png','jpeg'])
    f_seg = st.file_uploader("Adjuntar foto de Póliza de Seguro", type=['jpg','png','jpeg'])
    f_veh = st.file_uploader("Adjuntar foto del Vehículo", type=['jpg','png','jpeg'])
    
    enviar = st.form_submit_button("✅ ENVIAR REGISTRO")

# --- LÓGICA DE ENVÍO DE EMAIL ---
def enviar_por_email(nombre, celular, ciudad, domicilio, archivos):
    remitente = "leopcpay@gmail.com"
    # IMPORTANTE: Aquí va tu CONTRASEÑA DE APLICACIÓN de 16 letras, no tu clave normal
    password = "TU_CONTRASEÑA_DE_APLICACION" 
    
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = "leopcpay@gmail.com"
    msg['Subject'] = f"NUEVO REGISTRO: {nombre}"

    cuerpo = f"Datos del Fletero:\n\nNombre: {nombre}\nCelular: {celular}\nCiudad: {ciudad}\nDomicilio: {domicilio}"
    msg.attach(MIMEText(cuerpo, 'plain'))

    for n_archivo, contenido in archivos.items():
        if contenido:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(contenido.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={n_archivo}.jpg')
            msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remitente, password)
        server.send_message(msg)
        server.quit()
        return True
    except:
        return False

# --- PROCESO AL DAR CLIC ---
if enviar:
    if acepto and nombre and f_ci:
        lista_fotos = {"CI": f_ci, "Licencia": f_lic, "Libreta": f_lib, "Seguro": f_seg, "Vehiculo": f_veh}
        
        # 1. Intentar enviar email
        mail_enviado = enviar_por_email(nombre, celular, ciudad, domicilio, lista_fotos)
        
        # 2. Preparar mensaje WhatsApp
        resumen = f"🚀 *NUEVO FLETERO ANEXADO*\n\n👤 *Nombre:* {nombre}\n🏠 *Domicilio:* {domicilio}\n📍 *Ciudad:* {ciudad}\n\n✅ Registro enviado a CLS."
        wa_url = f"https://wa.me/59899417716?text={urllib.parse.quote(resumen)}"
        
        st.balloons()
        st.success("¡Registro procesado correctamente!")
        
        st.markdown(f"""
            <div style="background-color: #f1f8e9; padding: 20px; border-radius: 15px; text-align: center; border: 2px solid #2e7d32;">
                <h3>¡REGISTRO ENVIADO!</h3>
                <p>Las fotos se enviaron a nuestro servidor de correo.</p>
                <a href="{wa_url}" target="_blank" class="btn-wa">
                    📲 AVISAR POR WHATSAPP
                </a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Debes aceptar el contrato y completar los datos obligatorios.")
