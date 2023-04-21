# https://academy.masterschool.com/ns/books/published/swe/WritingFiles/8-UsingExternalLibraries.html
import PyPDF2


def main():
    pdf_reader = PyPDF2.PdfReader("resume.pdf")
    create_pdf_from_page(pdf_reader.pages[0], "resume_first_page.pdf")


def create_pdf_from_page(page, path_for_new_page):
    """Creates new pdf file with one page"""
    write_page = PyPDF2.PdfWriter()
    write_page.add_page(page)
    with open(path_for_new_page, "wb") as pdf_file:
        write_page.write(pdf_file)


if __name__ == '__main__':
    main()