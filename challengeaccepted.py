import re
import pandas as pd

file_path = 'new_kamusalay.csv'
dfalay = pd.read_csv(file_path, encoding='ISO-8859-1', header=None)

alay_dict_map = dict(zip(dfalay[0], dfalay[1]))

def normalize_alay(text):
    return ' '.join([alay_dict_map[word] if word in alay_dict_map else word for word in text.split(' ')])

def cleandata(input_string):
    input_string = re.sub(r'\bUSER\b', '', input_string)
    input_string = re.sub(r'\bx([a-fA-F0-9]{2})', '', input_string)
    input_string = input_string.lower()
    input_string = re.sub(r'http\S+', '', input_string)
    input_string = re.sub(r'[^a-zA-Z0-9 -]', '', input_string)
    input_string = normalize_alay(input_string)
    return input_string

