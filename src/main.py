from document_handler import DocumentHandler
from qa_assistant import QAAssistant

if __name__ == "__main__":
    url = input("Enter the URL: ")

    document_handler = DocumentHandler(url)
    pdf_path = document_handler.create_pdf()

    if pdf_path:
        document_handler.display_document()
        qa_assistant = QAAssistant(pdf_path)
        qa_assistant.run_assistant()