from bs4 import BeautifulSoup
import requests
import json


def AkmolaParse(): 
    cont = True
    pageAmount = 0
    prevUrl = ""
    nextUrl = "http://astana.gov.kz/ru/search?query=коронавирус"
    while cont:
        pageAmount += 1
        page = requests.get(nextUrl).text
        s = BeautifulSoup(page, 'lxml')
        
        if nextUrl == prevUrl:
            break

        prevUrl = nextUrl

        try:
            nextUrl = s.find('a', attrs={'class': 'next'})['href']
        except:
            continue


    data = []
    i = 0

    while i < pageAmount-1:
        url = requests.get("http://astana.gov.kz/ru/search?query=коронавирус&page="+str(i+1)).text

        soup = BeautifulSoup(url, 'lxml')

        results = soup.findAll('div', attrs={'class': 'result'})

        for result in results:
            date = result.find('span').text
            title = result.find('a').text.strip()
            shortText = result.find('div').text.strip()
            url = "http://astana.gov.kz/" + result.find('a')['href']
            d = {
                'date': date,
                'title': title,
                'shortText': shortText,
                'url': url
            }
            data.append(d)

        i += 1
    return data
        