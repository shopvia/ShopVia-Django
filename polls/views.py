from django.http import JsonResponse
from django.http import HttpResponse
from bs4 import BeautifulSoup
from requests import get


def index(request):
    # tested using request format like http: // localhost: 8000/polls /?q = hp
    results = []
    query = request.GET.urlencode()


# flipkart
    # url = 'https://www.flipkart.com/search?'+query + \
    #     '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    # response = get(url)
    # html_soup = BeautifulSoup(response.text, 'html.parser')
    # for a in html_soup.find_all('div',  attrs={'class': '_3liAhj'}):
    #     name = a.find('a', attrs={'class': '_2cLu-l'})
    #     price = a.find('div', attrs={'class': '_1vC4OE'})
    #     rating = a.find('div', attrs={'class': 'hGSR34'})
    #     result = {"Name": name.text, "Price": price.text,
    #               "Rating": ("None" if(rating == None) else rating.text)}
    #     results.append((result))

# daraz
    # url = 'https://www.daraz.com.np/catalog/?'+query + \
    #     '&_keyori=ss&from=input&spm=a2a0e.11779170.search.go.287d2d2bwlEWRd'
    # response = get(url)
    # html_soup = BeautifulSoup(response.text, 'html.parser')
    # for a in html_soup.find_all('div',  attrs={'class': 'c2prKC'}):
    #     name = a.find('div', attrs={'class': 'c16H9d'})
    #     price = a.find('span', attrs={'class': 'c13VH6'})
    #     # rating = a.find('i', attrs={'class': 'c3dn4k c3EEAg'})
    #     # halfrating = a.find('i', attrs={'class': 'c3dn4k c3DcGB'})
    #     result = {"Name": ("None" if(name == None) else name.a.text), "Price": ("None" if(price == None) else price.text),
    #               "Rating": "None"}
    #     results.append((result))

# sastodeal done
    # url = 'https://www.sastodeal.com/catalogsearch/result/?'+query+'&p=2'
    # response = get(url)
    # html_soup = BeautifulSoup(response.text, 'html.parser')
    # print("Response Response Response Response"+response.text)
    # for a in html_soup.find_all('li',  attrs={'class': 'product-item'}):
    #     name = a.find('strong', attrs={'class': 'product-item-name'})
    #     price = a.find('div', attrs={'class': 'price-final_price'})
    #     # rating = "null"
    #     # halfrating = a.find('i', attrs={'class': 'c3dn4k c3DcGB'})
    #     result = {"Name": ("None" if(name == None) else name.a.text), "Price": ("None" if(price == None) else price.span.span.text),
    #               "Rating": "None"}
    #     results.append((result))

# nepbay
    url = 'https://market.thulo.com/shopping/search?'+query
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    for a in html_soup.find_all('div',  attrs={'class': 'ncs-ad-list'}):
        name = a.find('div', attrs={'class': 'TGLBox'})
        price = a.find('div', attrs={'class': 'TGLBox'})
        # rating = a.find('i', attrs={'class': 'c3dn4k c3EEAg'})
        # halfrating = a.find('i', attrs={'class': 'c3dn4k c3DcGB'})
        result = {"Name": ("None" if(name == None) else name.h4.a.text), "Price": ("None" if(price == None) else price.p.span.text),
                  "Rating": "None"}
        results.append((result))

    return JsonResponse({'searchResults': results})
    # return HttpResponse(response.text)
