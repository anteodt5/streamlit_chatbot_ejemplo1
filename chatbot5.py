import streamlit as st
from groq import Groq
import datetime
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Chatbot con Groq", page_icon="🤖", layout="centered")

# Inicializar cliente de Groq
client = Groq(api_key="tu api")

# Inicializar historial de la conversación en sesión
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Encabezado
st.title("🤖 Chatbot con Groq y Streamlit")
st.write("Chatea con el modelo de Groq (llama-3.1-8b-instant).")

# Definir modelo fijo
model = "llama-3.1-8b-instant"

# Área para mostrar conversación estilo chat
chat_container = st.container()

with chat_container:
    for msg in st.session_state["messages"]:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.markdown(msg["content"])
        else:
            with st.chat_message("assistant"):
                st.markdown(msg["content"])

# Entrada del usuario estilo chat
if user_input := st.chat_input("Escribe tu mensaje..."):
    # Agregar mensaje del usuario al historial
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Llamada a la API de Groq
    response = client.chat.completions.create(
        model=model,
        messages=st.session_state["messages"]
    )

    # Obtener respuesta del asistente
    bot_reply = response.choices[0].message.content

    # Guardar en historial
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

    # Mostrar respuesta en tiempo real como hace ChatGPT
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

# Funcionalidades extra
st.subheader("⚙️ Funcionalidades adicionales")

# Guardar historial en archivo de texto
if st.button("Descargar historial en TXT"):
    chat_text = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state["messages"]])
    filename = f"chat_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    st.download_button("📥 Descargar TXT", chat_text, file_name=filename)

# Nueva funcionalidad: guardar historial en CSV
if st.button("Descargar historial en CSV"):
    df = pd.DataFrame(st.session_state["messages"])
    filename_csv = f"chat_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    csv_data = df.to_csv(index=False)
    st.download_button("📊 Descargar CSV", csv_data, file_name=filename_csv, mime="text/csv")

# Limpiar historial
if st.button("🗑️ Limpiar historial"):
    st.session_state["messages"] = []
    st.success("Historial borrado correctamente.")

# 📊 Sección de estadísticas de uso (desplegable con botón)
with st.expander("📊 Mostrar estadísticas de uso"):
    if st.session_state["messages"]:
        total_msgs = len(st.session_state["messages"])
        user_msgs = sum(1 for m in st.session_state["messages"] if m["role"] == "user")
        bot_msgs = sum(1 for m in st.session_state["messages"] if m["role"] == "assistant")
        avg_length = sum(len(m["content"].split()) for m in st.session_state["messages"]) / total_msgs

        st.metric("Total de mensajes", total_msgs)
        st.metric("Mensajes de usuario", user_msgs)
        st.metric("Respuestas del bot", bot_msgs)
        st.metric("Promedio de palabras por mensaje", round(avg_length, 2))
