import requests, os, bs4

url = 'https://xkcd.com'

os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print('Downloading page %s.... ' % url)
    url = 'https, #'

    res = requests.get(url)
    res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

comElement = soup.select('#comic img')
if comElement == []:
    print('not found')
else:
    comURL = 'https:' + comElement[0].get('src')
    print('Downloading image %s...' %(comURL))
    res = requests.get(comURL)
    res.raise_for_status()
    imagFile = open(os.path.join('xkcd', os.path.basename(comURL)), 'wb')
    for chunk in res.iter_content(10):
        imagFile.write(chunk)
    imagFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')



print('Done.')