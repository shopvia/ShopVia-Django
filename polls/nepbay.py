# # learning file 
# from django.http import JsonResponse
# from django.http import HttpResponse
# from bs4 import BeautifulSoup
# from requests import get


# def index(request):
#     results = []
#     query = request.GET.urlencode()
# url = 'https://market.thulo.com/shopping/search?'+query
#     response = get(url)
#     html_soup = BeautifulSoup(response.text, 'html.parser')
#     for a in html_soup.find_all('div',  attrs={'class': 'ncs-ad-list'}):
#         name = a.find('div', attrs={'class': 'TGLBox'})
#         price = a.find('div', attrs={'class': 'TGLBox'})
#         # rating = a.find('i', attrs={'class': 'c3dn4k c3EEAg'})
#         # halfrating = a.find('i', attrs={'class': 'c3dn4k c3DcGB'})
#         result = {"Name": ("None" if(name == None) else name.h4.a.text), "Price": ("None" if(price == None) else price.p.span.text),
#                   "Rating": "None"}
#         results.append((result))

#     return JsonResponse({'searchResults': results})