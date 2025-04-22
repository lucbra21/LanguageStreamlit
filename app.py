import streamlit as st
import common.traslators as traslators
from PIL import Image

# Inicializar traducciones y selector de idioma
translations = traslators.load_translations()
language = st.sidebar.selectbox("Language / Idioma", ["es", "en"])

# Añadir botones con banderas debajo del selector
col1, col2 = st.sidebar.columns(2)
with col1:
    if st.button("🇪🇸"):
        language = "es"  # Cambia el idioma a español
with col2:
    if st.button("🇬🇧"):
        language = "en"  # Cambia el idioma a inglés

t = lambda text_key: traslators.translate(text_key, language, translations)

# Mostrar elementos en la aplicación con soporte de múltiples idiomas
st.title(t("welcome_message"))
st.write(t("description"))

# Selector de opciones
option = st.selectbox(t("choose_option"), ["Option 1", "Option 2", "Option 3"])

# Botón de envío
if st.button(t("button_text")):
    st.write(f"You selected: {option}")

# Nota en el pie de página
st.write("---")
st.write(t("footer_note"))
