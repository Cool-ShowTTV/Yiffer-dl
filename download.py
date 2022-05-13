import requests, os

def getPageCount(name):
    url = f'https://yiffer.xyz/api/comics/{name}'
    response = requests.get(url).json()
    return response['numberOfPages']

def getPage(name, page):
    page = format(page, "03d")
    url = f'https://static.yiffer.xyz/comics/{name}/{page}.jpg'
    print(url)
    response = requests.get(url)
    return response.content

def downloadPage(name, page):
    print(f'Downloading page {page} of {name}', end='\r')
    with open(f'{name}/{format(page, "03d")}.jpg', 'wb') as f:
        f.write(getPage(name, page))

def downloadComic(name):
    pageCount = getPageCount(name)
    for page in range(1, pageCount + 1):
        downloadPage(name, page)

if __name__ == '__main__':
    comicName = input('Comic name: ')
    if not os.path.exists(comicName):
        os.makedirs(comicName)
    downloadComic(comicName)