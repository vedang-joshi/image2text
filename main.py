import easyocr
import pandas as pd

reader = easyocr.Reader(['en']) # Specify the language(s) you want to recognize
result = reader.readtext("img_to_be_converted_to_txt.jpg")

text_list = []
for (bbox, text, prob) in result:
    text_list.append(text)

df = pd.DataFrame(text_list)
df.to_excel('output.xlsx', index=False)
