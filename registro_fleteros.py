import streamlit as st
import urllib.parse

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Registro CLS", page_icon="🚛", layout="centered")

# --- ESTILO ---
st.markdown("""
    <style>
    .contrato-scroll {
        background-color: #f8f9fa;
        padding: 15px;
        border: 1px solid #d1d5db;
        border-radius: 10px;
        height: 200px;
        overflow-y: scroll;
        font-size: 13px;
        margin-bottom: 20px;
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
        font-size: 20px;
        text-decoration: none;
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚛 Registro de Fletero")
st.markdown("### CONEXIÓN LOGÍSTICA SUR")

# --- 1. CONTRATO VISIBLE CON SCROLL ---
st.subheader("Paso 1: Leer y Aceptar Contrato")
contrato_legal = """
<div class="contrato-scroll">
<b>CONTRATO DE ADHESIÓN Y DESLINDE DE RESPONSABILIDAD - CLS</b><br><br>
Por la presente, el Fletero acepta los siguientes términos:<br>
1. <b>INTERMEDIACIÓN:</b> CLS actúa como nexo comercial. No existe relación de dependencia.<br>
2. <b>RESPONSABILIDAD:</b> El Fletero es el único responsable por la integridad de la carga, botes o mercadería desde el origen hasta el destino.<br>
3. <b>COMISIÓN:</b> Se acepta el pago de una comisión del 15% a CLS por cada flete gestionado.<br>
4. <b>DOCUMENTACIÓN:</b> El Fletero declara bajo juramento tener seguros y habilitaciones vigentes.<br>
5. <b>SIN RECLAMOS:</b> El Fletero deslinda a CLS de cualquier daño, siniestro o pérdida durante el traslado.
</div>
"""
st.markdown(contrato_legal, unsafe_allow_html=True)

# --- 2. FORMULARIO DE DATOS ---
with st.form("registro_datos"):
    acepto = st.checkbox("HE LEÍDO Y ACEPTO LOS TÉRMINOS DEL CONTRATO")
    
    st.markdown("---")
    st.subheader("Paso 2: Completar tus Datos")
    nombre = st.text_input("Nombre y Apellido completo:")
    celular = st.text_input("Tu número de celular:")
    ciudad = st.text_input("Ciudad y Departamento:")
    domicilio = st.text_input("Domicilio y Nro de Casa:")
    
    enviar = st.form_submit_button("✅ GENERAR FICHA Y FINALIZAR")

# --- 3. LÓGICA DE ENVÍO ---
if enviar:
    if acepto and nombre and celular:
        st.balloons()
        
        # Resumen del contrato para que te quede en el chat de WhatsApp
        resumen_contrato = "Acepto Contrato CLS: Intermediación, Deslinde de Responsabilidad por carga y 15% comisión."
        
        texto_wa = (
            f"🚛 *NUEVO REGISTRO FLETERO - CLS*\n\n"
            f"👤 *Nombre:* {nombre}\n"
            f"📱 *Celular:* {celular}\n"
            f"📍 *Ciudad:* {ciudad}\n"
            f"🏠 *Domicilio:* {domicilio}\n\n"
            f"📝 *CONTRATO:* {resumen_contrato}\n"
            f"---------------------------\n"
            f"¡Hola Leonardo! Completé mi registro. Ahora te adjunto las fotos de mi Cédula, Licencia, Libreta y Seguro aquí debajo. 👇"
        )
        
        wa_url = f"https://wa.me/59899417716?text={urllib.parse.quote(texto_wa)}"
        
        st.success("¡Datos procesados!")
        st.markdown(f"""
            <div style="background-color: #f1f8e9; padding: 20px; border-radius: 12px; text-align: center; border: 2px solid #2e7d32;">
                <h3 style="color: #2e7d32;">¡PASO FINAL!</h3>
                <p>Tocá el botón verde para enviarme tu ficha por WhatsApp y <b>adjuntame las fotos de la documentación en el chat.</b></p>
                <a href="{wa_url}" target="_blank" class="btn-final">
                    📲 ENVIAR FICHA A LEONARDO
                </a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("⚠️ Por favor, marcá que aceptás el contrato y completá tus datos.")

st.sidebar.caption("CLS - Logística e Ingeniería 2026")
