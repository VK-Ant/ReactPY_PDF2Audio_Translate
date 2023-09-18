import streamlit as st
from googletrans import Translator
from googletrans.constants import LANGUAGES
from streamlit_extras.add_vertical_space import add_vertical_space
def main():

a
    with st.sidebar:
        st.title('🔗VK - 107 Language Translator App🤗')
        st.markdown('''
        ## About APP:

        The app's primary resource is utilised to create::

        - [streamlit](https://streamlit.io/)

        ## About me:

        - [Linkedin](https://www.linkedin.com/in/venkat-vk/)
        
        ''')

        add_vertical_space(4)
        st.write('💡All about Translate, created by VK🤗')


    # Input text
    input_text = st.text_area("Enter text to translate:")

    # Language selection
    src_lang = st.selectbox("Select source language:", list(LANGUAGES.values()))
    dest_lang = st.selectbox("Select destination language:", list(LANGUAGES.values()))

    # Translate button
    if st.button("Translate"):
        if input_text:
            try:
                translator = Translator()
                translation = translator.translate(input_text, src=src_lang, dest=dest_lang)
                st.write(f"**Translated text ({dest_lang}):** {translation.text}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
