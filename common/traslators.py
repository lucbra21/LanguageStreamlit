import json

# Cargar las traducciones desde el archivo JSON
def load_translations():
    with open("data/translations.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Función para obtener el texto traducido según el idioma seleccionado
def translate(text_key, language, translations):
    return translations.get(language, {}).get(text_key, text_key)