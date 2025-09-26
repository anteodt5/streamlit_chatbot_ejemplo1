🤖 Chatbot con Groq y Streamlit
Una aplicación web interactiva de chatbot construida con Streamlit que utiliza el potente modelo de lenguaje Llama 3.1 8B Instant de Groq para generar respuestas en tiempo real. La aplicación incluye funcionalidades avanzadas como guardado de historial y estadísticas de uso.

✨ Características Principales
Interfaz Chat en Tiempo Real: Experiencia de usuario similar a ChatGPT con mensajes que se muestran en tiempo real.

Modelo Llama 3.1 de Groq: Utiliza uno de los modelos de lenguaje más rápidos y eficientes disponibles.

Persistencia de Conversación: Mantiene el historial de la conversación durante toda la sesión.

Exportación de Datos: Permite descargar el historial del chat en formatos TXT y CSV.

Estadísticas de Uso: Muestra métricas detalladas sobre la conversación.

Diseño Responsivo: Interfaz centrada y adaptable gracias a Streamlit.

🛠️ Tecnologías Utilizadas
Streamlit: Framework para crear aplicaciones web interactivas en Python.

Groq API: Para acceder al modelo de lenguaje Llama 3.1 8B Instant.

Pandas: Procesamiento de datos para la exportación en CSV.

Datetime: Gestión de timestamps para los archivos exportados.

📁 Estructura del Código
Configuración Inicial
python
# Configuración de la página de Streamlit
st.set_page_config(page_title="Chatbot con Groq", page_icon="🤖", layout="centered")

# Inicialización del cliente de Groq
client = Groq(api_key="tu_api_key_aqui")
Gestión del Estado de la Sesión
El historial de mensajes se almacena en st.session_state["messages"]

Cada mensaje contiene un rol (user o assistant) y el contenido del mensaje

Flujo Principal del Chat
Entrada del Usuario: Interfaz de chat input para recibir mensajes del usuario.

Llamada a la API: Envío del historial completo a Groq para mantener contexto.

Respuesta en Tiem Real: La respuesta del bot se muestra inmediatamente después de recibirla.

Funcionalidades Adicionales
📥 Exportación de Historial
Formato TXT: Descarga simple en formato de texto plano.

Formato CSV: Descarga estructurada usando Pandas para análisis de datos.

📊 Estadísticas de Uso
Total de mensajes en la conversación.

Distribución entre mensajes del usuario y del bot.

Promedio de palabras por mensaje.

🗑️ Gestión de Historial
Botón para limpiar completamente el historial de la conversación.

🚀 Cómo Usar
Escribe tu mensaje en la caja de texto en la parte inferior.

Presiona Enter para enviar el mensaje al bot.

Espera la respuesta generada por el modelo de Groq.

Utiliza los botones en la sección inferior para:

Descargar el historial de la conversación

Ver estadísticas de uso

Limpiar el historial cuando sea necesario

⚙️ Instalación y Ejecución
Clona este repositorio:

bash
git clone [url-del-repositorio]
Instala las dependencias:

bash
pip install streamlit groq pandas
Ejecuta la aplicación:

bash
streamlit run app.py
🔐 Configuración de API Key
Importante: Para usar esta aplicación, necesitas:

Obtener una API key gratuita de Groq

Reemplazar "tu api" con tu propia key

📋 Requisitos del Sistema
Python 3.7+

Conexión a Internet estable

Navegador web moderno

🎯 Posibles Mejoras Futuras
Agregar selección de múltiples modelos de Groq

Implementar modo de conversación por temas/hilos

Añadir soporte para imágenes y archivos

Implementar autenticación de usuarios

Agregar más métricas y análisis de conversaciones
