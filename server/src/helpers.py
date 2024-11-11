from langchain_text_splitters import RecursiveCharacterTextSplitter
import PyPDF2

class TextActions:
    @staticmethod
    def extract_text_from_pdf(pdf_file) -> str:
        with open(pdf_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        return text
    
    @staticmethod
    def split_chucks(text, chunk_size=500) -> list[str]:
        text_splitter = RecursiveCharacterTextSplitter(
          chunk_size=chunk_size,
          chunk_overlap=20,
          length_function=len,
          is_separator_regex=False,
        )

        return text_splitter.split_text(text)

