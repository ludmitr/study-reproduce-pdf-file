# https://academy.masterschool.com/ns/books/published/swe/WritingFiles/8-UsingExternalLibraries.html
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def main():
    pdf_reader = PyPDF2.PdfReader("resume.pdf")

    # create_pdf_from_page(pdf_reader.pages[0], "resume_first_page.pdf")
    #
    # pdf_writer = rotate_last_page_left(pdf_reader)
    # save_pdf(pdf_writer, "resume_last_page.pdf")

    replace_text_in_pdf("resume.pdf", "resume_replaced.pdf", "demonstrate", "exhibit", pdf_reader)


def replace_text_in_pdf(input_file, output_file, old_text, new_text, reader):
    """ replace text in pdf, and create new pdf with replaced text"""
    num_pages = len(reader.pages)

    # Create a new PDF with the same number of pages
    output_canvas = canvas.Canvas(output_file, pagesize=letter)

    for page_num in range(num_pages):
        # Extract text from the current page
        page = reader.pages[page_num]
        text = page.extract_text()

        # Replace the old text with the new text
        text = text.replace(old_text, new_text)

        # Write the text to the new PDF
        output_canvas.setFont('Helvetica', 12)
        x, y = 50, 750
        for line in text.split('\n'):
            output_canvas.drawString(x, y, line)
            y -= 14

        # Move to the next page
        output_canvas.showPage()

    # Save the new PDF
    output_canvas.save()



def rotate_last_page_left(pdf_reader: PyPDF2.PdfReader) -> PyPDF2.PdfWriter:
    """Rotate last page left 90 and returns PyPDF2.PdfWriter """
    pages_length = len(pdf_reader.pages)
    pdf_writer = PyPDF2.PdfWriter()

    # adding all pages except last to pdf_writer
    for num_page in range(pages_length):
        pdf_writer.add_page(pdf_reader.pages[num_page])

    pdf_writer.pages[-1].rotate(-90)
    return pdf_writer

def create_pdf_from_page(page, path_for_new_page):
    """Creates new pdf file with one page"""
    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(page)
    save_pdf(pdf_writer, path_for_new_page)


def save_pdf(pdf_writer,path_for_new_page):
    """ saves pdf_writer in path_for_new_page"""
    with open(path_for_new_page, "wb") as pdf_file:
        pdf_writer.write(pdf_file)


if __name__ == '__main__':
    main()