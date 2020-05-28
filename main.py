import io

from pdfconvert import parsepdf,inter
from googletrans import Translator

with open("..\\output.txt", 'rb') as f:
    cont=f.read()
inter.splitInChunks(cont.decode('utf-8','ignore'))
#content=parsepdf.convert_pdf_to_txt("C:\\Users\\monty\\OneDrive\\Desktop\\bree_landregionguide.pdf")

#print(content)
#with io.open("..\\bree.pdf", "wb") as f:
 #   f.write(content)

translator = Translator()
#result = translator.translate(content, src='en', dest='it')
#print(result)