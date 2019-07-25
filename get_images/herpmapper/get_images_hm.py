import urllib2, re, os, urllib, random
from bs4 import BeautifulSoup

for i in range(1,65):
    # Parse HTML
    if i > 1:
        page = "&p=" + str(i)
    else:
        page = ""
    url = "https://www.herpmapper.org/records?taxon=Agkistrodon+contortrix" + page
    print(url)
    print(i)
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html, features="html.parser")

    # Get records
    recs = []
    for link in soup.find_all('a', href = re.compile("/record/")):
        recs.append(link['href'])
    recs = map(str,(list(set(recs))))

    # Get URL
    b = []
    for rec in recs:
        my_url = 'http://www.herpmapper.org' + rec
        html2 = urllib2.urlopen(my_url)
        soup2 = BeautifulSoup(html2, features="html.parser")
        for link in soup2.find_all('a', href = re.compile("full")):
            m = re.sub(r'large|medium|small', 'full', str(link.img.get('src')))
            b.append('http://www.herpmapper.org' + m)

    # Download images
    count = 1
    for a in b:
        urllib.urlretrieve(a, '/Users/js/Desktop/copperhead/' + str(i) + '-' + str(count) + '.jpg')
        count += 1
