import requests, os

class Info:
    def getPageCount(name):
        '''Get the page count of the given comic name'''
        url = f'https://yiffer.xyz/api/comics/{name}'
        response = requests.get(url).json()
        return response['numberOfPages']

    def getTags(name):
        '''Get the tags of the given comic name'''
        url = f'https://yiffer.xyz/api/comics/{name}'
        response = requests.get(url).json()
        return response['keywords']

    def getRating(name):
        '''Get the rating of the given comic name'''
        url = f'https://yiffer.xyz/api/comics/{name}'
        response = requests.get(url).json()
        return response['userRating']

    def getComicOrder(name):
        '''Get the next and previous comics of the given comic name'''
        url = f'https://yiffer.xyz/api/comics/{name}'
        response = requests.get(url).json()
        return {"nextComic": response['nextComic'], "previousComic": response['previousComic']}

class Comic:
    def getPage(name, page):
        '''Get the page data of the given comic name and page number'''
        page = format(page, "03d")
        url = f'https://static.yiffer.xyz/comics/{name}/{page}.jpg'
        response = requests.get(url)
        return response.content

    def downloadPage(name, page):
        '''Download the given comic name and page number'''
        print(f'Downloading page {page} of "{name}"', end='\r')
        if not os.path.exists(comicName):
            os.makedirs(comicName)
        with open(f'{name}/{format(page, "03d")}.jpg', 'wb') as f:
            f.write(Comic.getPage(name, page))

    def downloadComic(name):
        '''Download the entire given comic'''
        pageCount = Info.getPageCount(name)
        print(f'Downloading "{name}" with {pageCount} pages')
        for page in range(1, pageCount + 1):
            Comic.downloadPage(name, page)
        print(f'Finished downloading {pageCount} pages of "{name}"')

if __name__ == '__main__':
    comicName = input('Comic name: ')
    Comic.downloadComic(comicName)