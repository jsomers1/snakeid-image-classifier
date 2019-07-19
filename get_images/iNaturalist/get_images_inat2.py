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


c = a[len(a)//2:]
count = 1854
for x in c:
    urllib.urlretrieve(x, '/Users/js/Desktop/copperhead/' + str(count) + '.jpg')
    print(count)
    count += 1
