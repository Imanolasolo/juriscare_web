import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="AI JurisCare",
    page_icon=":gavel:",
    layout="wide",
)

# Título y descripción principal
col1, col2 = st.columns([1,4])
with col1:
    st.image('logo.png',width=150)
with col2:    
    st.title("AI JurisCare")
st.markdown("""
Bienvenido a **AI JurisCare**, la solución de inteligencia artificial diseñada específicamente para profesionales legales en Ecuador. Nuestra plataforma ofrece herramientas avanzadas para mejorar la atención al cliente, optimizar la gestión de citas y proporcionar asistencia legal automatizada.
""")

# Sección: Características
with st.expander("Características de AI JurisCare"):
    st.markdown("""
    - **Asistente Virtual**: Un chatbot inteligente que responde a preguntas frecuentes y proporciona información sobre servicios legales.
    - **Gestión de Citas**: Un sistema integrado para agendar, modificar y cancelar citas con facilidad.
    - **Consultas Iniciales Automatizadas**: Evaluación inicial de las necesidades del cliente y redirección al abogado adecuado.
    - **Documentación y Formularios**: Acceso a documentos legales y formularios necesarios para los clientes.
    """)

# Sección: Beneficios
with st.expander("Beneficios para Profesionales Legales"):
    st.markdown("""
    - **Eficiencia Mejorada**: Automatización de tareas repetitivas para que los abogados puedan centrarse en casos complejos.
    - **Atención al Cliente Superior**: Respuestas rápidas y precisas a las consultas de los clientes.
    - **Gestión Simplificada**: Herramientas fáciles de usar para la gestión de citas y documentos.
    - **Disponibilidad 24/7**: Asistencia constante para los clientes, incluso fuera del horario laboral.
    """)

# Sección: Testimonios
st.header("Testimonios de Usuarios")
st.info("""
*"_AI JurisCare ha transformado la forma en que interactuamos con nuestros clientes. La eficiencia y precisión del asistente virtual nos han permitido dedicar más tiempo a casos importantes._"* 

*"La gestión de citas nunca ha sido tan fácil. Mis clientes pueden agendar y modificar sus citas en cualquier momento, lo que ha reducido significativamente el trabajo administrativo."* 
""")

# Sección: Contacto
st.header("Contáctanos")
st.markdown("""
¿Interesado en AI JurisCare? Contáctanos para más información y una demostración en vivo de nuestra plataforma.
- **Email**: jjusturi@gmail.com
""")

# Pie de página
st.markdown("---")
st.markdown("© 2024 AI JurisCare. Todos los derechos reservados.")
