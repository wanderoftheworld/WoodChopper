import fitz


# Open the file
file = "lzvoyager-resume.pdf"
doc = fitz.open(file)

# Loop through all pages
for i, page in enumerate(doc.pages(), start=1):
  text = page.get_text("text")
  print("Reading page {} from {} ...".format(i, file))
  print("Text from page {}:\n'{}'\n".format(i, text))

# Close document
doc.close()
