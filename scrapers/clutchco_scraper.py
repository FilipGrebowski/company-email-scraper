import requests
import bs4
import re
import countries

list_emails = []


class ClutchScraper:

    urls = []
    count = 0

    def remove_www(name):
        if name[:4] == 'www.':
            return name[4:]
        else:
            return name

    def remove_http_https(name):
        if name[:5] == 'https':
            return name[8:]
        else:
            return name[7:]

    def append_source(domain):
        email_beginning = ['social', 'marketing', 'hello', 'contact', 'support', 'info', 'press',
                           'media', 'team', 'sales', 'enquiries', 'help', 'business', 'service',
                           'career', 'community', 'opportunities']

        for i in range(len(email_beginning)):
            email_address = email_beginning[i] + '@' + domain
            list_emails.append(email_address)
            print(email_address)

    for i in range(250):
        if i == 0:
           urls.append('https://clutch.co/web-developers')
        else:
            urls.append('https://clutch.co/web-developers?page=' + str(i))

    for i in range(len(urls)):

        res = requests.get(urls[i])
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        for company in soup.find_all('li', {'class': 'provider-row'}):
            for domain in company.find_all('a', {'href': re.compile('^http')}):

                try:
                    countryName = company.find('span', {'class': re.compile('region')}).string

                    for country in countries.countries:

                        # Checking if a country exists in list and if the country is in Europe.
                        if countryName == country.get('name') and country.get('continent') == 'Europe':

                            if domain.get('href')[:14] != 'https://clutch':
                                print(country.get('name'))
                                domain = remove_www(remove_http_https(domain.get('href')))
                                append_source(re.split('[/?]', domain)[0])
                                count = count + 17
                except:
                    print('There was no country name provided on the website.')

        print('The current count is: ' + str(count))

    with open('emails.csv', 'a') as file:
        for key in list_emails:
            file.write("%s\n" % key)
