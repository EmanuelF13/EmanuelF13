import pdfkit

#Define path to wkhtmltopdf.exe
path_to_wkhtmltopdf = r'C:\Users\Emy\Desktop\Html CV\libs\wkhtmltopdf\bin\wkhtmltopdf.exe'

#Define path to HTML file
path_to_file = r'C:\Users\Emy\Desktop\Html CV\CVpage.html'

#Point pdfkit configuration to wkhtmltopdf.exe
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

#Convert HTML file to PDF
pdfkit.from_file(path_to_file, output_path='test.pdf', configuration=config)