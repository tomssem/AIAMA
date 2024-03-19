import os

from PyPDF2 import PdfWriter, PdfReader
from pyprojroot import here

# raw page numbers from context of book
chapters = {
    1: (1, 35),
    2: (36, 60),
    3: (63, 106),
    4: (110, 142),
    5: (146, 175),
    6: (180, 204),
    7: (208, 247),
    8: (251, 278),
    9: (280, 310),
    10: (314, 338),
    11: (344, 380),
    12: (385, 408),
    13: (412, 454),
    14: (461, 497),
    15: (500, 524),
    16: (528, 557),
    17: (562, 596),
    18: (599, 646),
    19: (651, 715),
    20: (721, 747),
    21: (750, 785),
    22: (789, 819),
    23: (823, 851),
    24: (856, 878),
    25: (881, 920),
    26: (925, 975),
    27: (981, 1006),
    28: (1012, 1015),
}

# page offset
offset = 13

data_root = os.path.join(here(), "book")
book_file = os.path.join(data_root, "AIAMA.pdf")
# load the PDF file
with open(book_file, "rb") as input_file:
    input_pdf = PdfReader(input_file)

    # iterate over the chapters
    for chapter_num, (start_page, end_page) in chapters.items():
        # create a new PDF writer for each chapter
        output_pdf = PdfWriter()

        # iterate over the pages in the current chapter
        for page_num in range(start_page + offset - 1, end_page + offset):
            # get the page from the input PDF
            page = input_pdf.pages[page_num]

            # add the page to the output PDF
            output_pdf.add_page(page)

        # save the chapter to a new PDF file
        output_file = os.path.join(data_root, f"chapter_{chapter_num}.pdf")
        print(output_file)
        with open(output_file, "wb") as output_file:
            output_pdf.write(output_file)

print("PDF split into chapters successfully!")
