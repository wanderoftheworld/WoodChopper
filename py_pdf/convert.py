// Remotasks TaskID: 65d4e65ee718feaffb1610b9
// I've seen a couple of this.

import PyPDF2

# Open the file
pdf = open("lzvoyager-resume.pdf", "rb")

# Create PyPDF2 reader object
pdfReader = PyPDF2.PdfReader(pdf)

# Extract number of pages into list
page_num = len(pdfReader.pages)

# Loop through all the pages
for i in range(page_num):
    # Get the page content.
    page = pdfReader.pages[i]
    # Print document content of each page
    print(page.extract_text())

pdf.close()
