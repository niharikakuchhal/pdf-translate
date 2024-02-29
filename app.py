from flask import Flask, request, render_template, redirect
import fitz
from PIL import Image
import pytesseract
import io
from googletrans import Translator
from collections import Counter

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_with_ocr(pdf_stream):
    text = ''
    doc = fitz.open(stream=pdf_stream, filetype="pdf")
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # Load the current page
        pix = page.get_pixmap()  # Render page to an image
        img = Image.open(io.BytesIO(pix.tobytes()))  # Convert the image to a PIL Image
        text += pytesseract.image_to_string(img)  # Use PyTesseract to do OCR on the image
    return text

def process_text(text):
    # Basic text processing to extract "keywords"
    words = text.split()
    # Simple frequency-based extraction, this is not language-specific and can be improved
    word_counts = Counter(words)
    keywords = [word for word, count in word_counts.most_common(10)]

    # For summary, we take the first few lines of text assuming the introduction might be relevant
    summary_lines = text.split('\n')[:5]
    summary = ' '.join(summary_lines)

    return summary, keywords

def process_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ''
    for page in doc:
        text += page.get_text("text")
    doc.close()

    if len(text.strip()) < 50:  # Fallback to OCR if text extraction is insufficient
        pdf_file.seek(0)
        text = extract_text_with_ocr(pdf_file.read())

    summary, keywords = process_text(text)  # Process the extracted text

    # print("Extracted Text:", text[:500])
    return summary, keywords

def translate(summary, keywords):
    translator = Translator()
    summary_en = translator.translate(summary, src='mr', dest='en').text
    keywords_en = [translator.translate(kw, src='mr', dest='en').text for kw in keywords]
    return summary_en, keywords_en

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '' or not allowed_file(file.filename):
        return redirect(request.url)
    
    summary, keywords = process_pdf(file)
    summary_en, keywords_en = translate(summary, keywords)
    return render_template('results.html', summary=summary, keywords=keywords, summary_en=summary_en, keywords_en=keywords_en)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['pdf']

if __name__ == '__main__':
    app.run(debug=True)

