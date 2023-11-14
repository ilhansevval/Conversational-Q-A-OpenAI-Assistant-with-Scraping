import os
import logging
import weasyprint
from pdf2image import convert_from_path
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocumentHandler:
    def __init__(self, url, output_dir="data"):
        self.url = url
        self.output_dir = output_dir

    def create_pdf(self):
        try:
            pdf = weasyprint.HTML(self.url).write_pdf()
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)
            file_path = os.path.join(self.output_dir, 'sample.pdf')
            with open(file_path, 'wb') as f:
                f.write(pdf)
            logger.info(f"PDF created successfully: {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Error creating PDF: {e}")
            return None

    def display_document(self):
        try:
            pdf_path = os.path.join(self.output_dir, 'sample.pdf')
            images = convert_from_path(pdf_path)
            _, axs = plt.subplots(3, 3, figsize=(25, 25))
            axs = axs.flatten()
            for img, ax in zip(images, axs):
                ax.set_xticks([])
                ax.set_yticks([])
                ax.imshow(img)
            plt.show()
        except Exception as e:
            logger.error(f"Error displaying document: {e}")