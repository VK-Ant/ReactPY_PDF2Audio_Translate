#!pip install -r requirements.txt

#import library
import pdfplumber as pp
from gtts import gTTS
from tqdm import tqdm

#Extract text from pdf
pdf_text = ''

with pp.open('HDE.pdf') as pdf:
    for page in tqdm(pdf.pages):
        pdf_text += page.extract_text()

#convert extracted text to speech
tts = gTTS(text=pdf_text, lang='en')
tts.save('HDE.mp3')