# Import the required module for text
# to speech conversion
from gtts import gTTS
#This is used to read and convert pdf to txt
import slate3k as slate


import os

pdf_path = "D:\Kaylen_python/pdf_text_file.pdf" #Location on device where pdf file is located
file_to_read = "output_from_pdf.txt" #This is the output file from converting the pdf file. For me it was in my current project folder.
store_pdf_file = ''
stored_data = ''
file = ''


#This function takes the pdf file you want to convert and saves it into the txt file which you will use to read out loud.
def read_and_convert_pdf(data, file):
    with open(pdf_path, 'rb') as f:
        extracted_text = slate.PDF(f)
        pdf_string = extracted_text
        print(pdf_string)
    file = open("output_from_pdf.txt", "wt")
    n = file.write(pdf_string[0])
    file.close()

    return file


#This is used to read the saved .txt file from the above function
def read_file(data, file):
    file = open(file_to_read, "r")
    data = file.read()
    stored_data = data
    return stored_data


read_and_convert_pdf(store_pdf_file, file)

# The text that you want to convert to audio
mytext = read_file(file_to_read, file)

# Language in which you want to convert
language = 'en'


myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

# Playing the converted file
os.system("welcome.mp3")