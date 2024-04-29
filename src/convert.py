import PyPDF2
from docx import Document
import os


class ConvertToWord:

    def __init__(self, pdf_path: str) -> None:
        _, pdf_name = os.path.split(pdf_path)
        self.output_dir = 'output'
        os.makedirs(self.output_dir, exist_ok=True)
        name, extension = os.path.splitext(pdf_name)
        if extension != '.pdf':
            raise ValueError("pdf 副檔名錯誤")
        self.pdf_name = pdf_name
        self.word_name = f'{name}.docx'

    def pdf_to_text(self):
        self.text = ""
        with open(self.pdf_name, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page_num in range(len(reader.pages)):
                self.text += reader.pages[page_num].extract_text()

    def text_to_word(self):
        doc = Document()
        doc.add_paragraph(self.text)
        doc.save(os.path.join(self.output_dir, self.word_name))

    def pdf_to_word(self):
        self.pdf_to_text()
        self.text_to_word()
