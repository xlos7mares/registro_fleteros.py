import streamlit as st
import urllib.parse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Registro Aliados CLS", page_icon="🚛", layout="centered")

# --- ESTILO PERSONALIZADO ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; height: 60px; font-weight: bold; background-color: #01579b; color: white; border-radius: 10px; }
    .contrato { background-color: #f0f2f6; padding: 20px; border-radius: 10px; border: 1px solid #d1d5db; font-size: 14px; height: 300px; overflow-y: scroll; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚛 Registro de Fletero Aliado")
st.write("Conexión Logística Sur")

# --- 1. EL CONTRATO (VISIBILIDAD PRIMERO) ---
st.subheader("Términos y Condiciones del Servicio")
contrato_texto = """
**CONTRATO DE ADHESIÓN Y DESLINDE DE RESPONSABILIDAD - CLS**

1. **NATURALEZA DEL VÍNCULO:** El Fletero acepta que Conexión Logística Sur (en adelante CLS) actúa únicamente como un nexo comercial y tecnológico entre el cliente y el transportista. No existe relación de dependencia laboral.
2. **RESPONSABILIDAD POR LA CARGA:** El Fletero asume la responsabilidad total y absoluta por la integridad de la mercadería, botes o cualquier objeto transportado desde la carga hasta la entrega efectiva. CLS no responderá por daños, hurtos o accidentes.
3. **COMISIÓN:** El Fletero se compromete a abonar el 15% del valor total del flete a CLS por concepto de gestión comercial.
4. **DOCUMENTACIÓN:** El Fletero declara bajo juramento tener su vehículo, seguro de carga y documentación personal al día y en regla según las leyes de Uruguay.
5. **ESTADO DEL VEHÍCULO:** Es responsabilidad del fletero mantener la unidad en óptimas condiciones mecánicas y de seguridad.
"""
st.markdown(f'<div class="contrato">{contrato_texto}</div>', unsafe_allow_html=True)

# --- 2. FORMULARIO DE DATOS ---
with st.form("registro_form"):
    acepto = st.checkbox("HE LEÍDO Y ACEPTO TODOS LOS TÉRMINOS DEL CONTRATO ANTERIOR")
    
    st.markdown("---")
    nombre = st.text_input("Nombre completo:")
    celular = st.text_input("Celular:")
    ciudad = st.text_input("Ciudad y Departamento:")
    domicilio = st.text_input("Domicilio y Nro de Casa:")
    
    st.markdown("---")
    st.subheader("Adjuntar Documentación")
    f_ci = st.file_uploader("Foto de Cédula", type=['jpg','png','jpeg'])
    f_lic = st.file_uploader("Foto de Licencia de Conducir", type=['jpg','png','jpeg'])
    f_lib = st.file_uploader("Foto de Libreta de Propiedad", type=['jpg','png','jpeg'])
    f_seg = st.file_uploader("Foto de Póliza de Seguro", type=['jpg','png','jpeg'])
    f_veh = st.file_uploader("Foto del Vehículo", type=['jpg','png','jpeg'])
    
    enviar = st.form_submit_button("✅ ENVIAR REGISTRO")

# --- 3. LÓGICA DE ENVÍO DE EMAIL ---
def enviar_email(nombre, celular, ciudad, domicilio, archivos):
    # Configura aquí tus datos de envío
    remitente = "leopcpay@gmail.com"
    destinatario = "leopcpay@gmail.com"
    password = "TU_CONTRASEÑA_DE_APLICACION" # Ver nota abajo

    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = f"NUEVO FLETERO: {nombre}"

    cuerpo = f"Nuevo registro en CLS:\n\nNombre: {nombre}\nCelular: {celular}\nCiudad: {ciudad}\nDomicilio: {domicilio}"
    msg.attach(MIMEText(cuerpo, 'plain'))

    for nombre_archivo, contenido in archivos.items():
        if contenido is not None:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(contenido.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={nombre_archivo}.jpg')
            msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remitente, password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Error al enviar email: {e}")
        return False

if enviar:
    if acepto and nombre and f_ci:
        archivos = {"CI": f_ci, "Licencia": f_lic, "Libreta": f_lib, "Seguro": f_seg, "Vehiculo": f_veh}
        exito = enviar_email(nombre, celular, ciudad, domicilio, archivos)
        
        if exito:
            st.balloons()
            st.success(f"¡Registro enviado con éxito, {nombre}!")
            st.info("Ya hemos recibido tu documentación en Conexión Logística Sur.")
    else:
        st.warning("Por favor, acepta el contrato y completa los datos obligatorios.")
