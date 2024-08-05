import PyPDF2
import pyttsx3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog


class PDFtoMP3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        def initUI(self):
            self.setWindowTitle("PDF to MP3 Converter")
            layout = QVBoxLayout()
            self.select_button = QPushButton("Select PDF", self)
            self.select_button.clicked.connect(self.select_pdf)
            layout.addWidget(self.select_button)

            self.setLayout(layout)

            def select_pdf(self):
                options = QFileDialog.Options()
                pdf_path, _ = QFileDialog.getOpenFileNames(
                    self, "Select PDF", "", "PDF Files (*.pdf)", options=options
                )
                if pdf_path:
                    text = extract_txt(pdf_path)
                    text_to_audio = (text, "output.mp3")

        if __name__ == "__main__":
            app = QApplication(sys.argv)
            converter = PDFtoMP3()
            converter.show()
            sys.exit(app.exec_())


def extract_txt(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
    return text


def text_to_audio(text, output_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()
