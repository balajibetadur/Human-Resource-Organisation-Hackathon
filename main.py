
import PyPDF2
pdfFileObj = open('a.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
str =  pageObj.extractText()
str=str.replace(" \n"," ")
pdfFileObj.close()
