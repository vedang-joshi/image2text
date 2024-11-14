import easyocr
import pandas as pd

reader = easyocr.Reader(['en']) # Specify the language(s) you want to recognize
result = reader.readtext("Files_that_are_replaced_when_loading_a_new_IETM_part_one.jpg")

text_list = []
for (bbox, text, prob) in result:
    text_list.append(text)

df = pd.DataFrame(text_list)
df.to_excel('output.xlsx', index=False)