import requests, os

class Info:
    def getPageCount(name):
        url = f'https://yiffer.xyz/api/comics/{name}'
        response = requests.get(url).json()
        return response['numberOfPages']

    def getTags(name):
        url = f'https://yiffer.xyz/api/comics/{name}'
        response = requests.get(url).json()
        return response['keywords']

    def getRating(name):
        url = f'https://yiffer.xyz/api/comics/{name}'
        response = requests.get(url).json()
        return response['userRating']

    def getComicOrder(name):
        url = f'https://yiffer.xyz/api/comics/{name}'
        response = requests.get(url).json()
        return {"nextComic": response['nextComic'], "previousComic": response['previousComic']}

def getPage(name, page):
    page = format(page, "03d")
    url = f'https://static.yiffer.xyz/comics/{name}/{page}.jpg'
    response = requests.get(url)
    return response.content

def downloadPage(name, page):
    print(f'Downloading page {page} of "{name}"', end='\r')
    if not os.path.exists(comicName):
        os.makedirs(comicName)
    with open(f'{name}/{format(page, "03d")}.jpg', 'wb') as f:
        f.write(getPage(name, page))

def downloadComic(name):
    pageCount = Info.getPageCount(name)
    print(f'Downloading "{name}" with {pageCount} pages')
    for page in range(1, pageCount + 1):
        downloadPage(name, page)
    print(f'Finished downloading {pageCount} pages of "{name}"')

if __name__ == '__main__':
    comicName = input('Comic name: ')
    downloadComic(comicName)