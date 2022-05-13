import requests, os

class Info:
    def search(search = "", page = 1):
        try: 
            from urllib.parse import urlencode
        except ImportError:
            print("Please install urllib")
            return
        data = {'search': search, 'page': page}
        url = "https://yiffer.xyz/api/comicsPaginated" + "?" + urlencode(data)
        response = requests.get(url)
        response = response.json()
        return response
        
    def getName(name):
        url = f'https://yiffer.xyz/api/comics/{name}'
        response = requests.get(url)
        response = response.json()
        return response['name']

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
        if not os.path.exists(f'comics/{name}'):
            os.makedirs(f'comics/{name}')
        with open(f'comics/{name}/{format(page, "03d")}.jpg', 'wb') as f:
            f.write(Comic.getPage(name, page))

    def downloadComic(name):
        '''Download the entire given comic'''
        comicName = Info.getName(name)
        pageCount = Info.getPageCount(comicName)
        print(f'Downloading "{comicName}" with {pageCount} pages')
        for page in range(1, pageCount + 1):
            print(f'Downloading page {page}/{pageCount}', end='\r')
            Comic.downloadPage(comicName, page)
        print(f'Finished downloading {pageCount} pages of "{comicName}"')

if __name__ == '__main__':
    comicName = input('Comic name: ')
    Comic.downloadComic(comicName)
    with open(f'comics/{comicName}/! Tags.txt', 'w') as f:
        tags = Info.getTags(comicName)
        for tag in tags:
            f.write(tag + '\n')
    with open(f'comics/{comicName}/! Rating.txt', 'w') as f:
        rating = Info.getRating(comicName)
        f.write(f'{rating}/10\n')
        presentage = round(rating * 10)
        f.write(f'{presentage}%')