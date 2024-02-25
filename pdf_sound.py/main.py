import pyttsx3
from PyPDF2 import PdfReader  

# Insert the name of your PDF
pdfname = 'book.pdf'
pdfreader = PdfReader(pdfname)  
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    page = pdfreader.pages[page_num]  
    text = page.extract_text()  
    if text:  # Checking if text is not None
        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)
        speaker.save_to_file(clean_text, 'story.mp3')

speaker.runAndWait()
speaker.stop()
