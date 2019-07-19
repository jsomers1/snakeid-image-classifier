import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import urllib
import re

df = pd.read_excel('observations-44360.xlsx')
a = df['image_url'].tolist()
a = [x.encode('ascii') for x in a]
a[:] = [b.replace('medium', 'large') for b in a]


b = a[:len(a)//2]
count = 1
for x in b:
    urllib.urlretrieve(x, '/Users/jonahsomers/Desktop/copperhead/' + str(count) + '.jpg')
    print(count)
    count += 1
