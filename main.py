import requests

with open('valid_proxies.txt', 'r') as f:
    proxies = f.read().split('\n')

sites_to_check = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html',
        'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html',
        'http://books.toscrape.com/catalogue/category/books/childrens_11/index.html']

counter = 0

for site in sites_to_check:
    try:
        print(f'using the proxy: {proxies[counter]}')
        res = requests.get(site, proxies={'http': proxies[counter],
            'https': proxies[counter]})
        print(res.status_code)

    except:
        print('failed')

    counter += 1
    counter %= len(proxies)
