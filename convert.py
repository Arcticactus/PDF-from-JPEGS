from os import listdir, getcwd
from os.path import isfile, join

import img2pdf

# Run with python convert.py

def create_pdf(source_images, pdf_name):
    if not pdf_name.endswith(".pdf"):
        print("pdf_name must end in .pdf.")
        return
    with open(pdf_name, "wb") as output:
        output.write(img2pdf.convert(source_images))


if __name__ == '__main__':
    cwd = getcwd()
    images = [image for image in listdir(cwd) if isfile(join(cwd, image))]
    images = images[:-1]  # To ignore convert.py.
    # Assumption: convert.py is the last file in lexical order.
    create_pdf(images, "output.pdf")
