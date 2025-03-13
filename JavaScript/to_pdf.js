// include the jsPDF library in your HTML file
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.5.3/jspdf.min.js"></script>

// JavaScript function to convert HTML to PDF
function convertHTMLtoPDF() {
  const htmlContent = document.getElementById('htmlToConvert').innerHTML;
  const pdf = new jsPDF('p', 'pt', 'a4');
  pdf.addHTML(htmlContent, function() {
    pdf.save('your_file_name.pdf');
  });
}

