import requests
import bs4
import re

res = requests.get('https://www.seedtable.com/startups-europe')
soup = bs4.BeautifulSoup(res.text, 'html.parser')


class Scraper:

    count = 0
    emails = []

    email_beginning = ['social', 'marketing', 'hello', 'contact', 'support', 'info', 'press',
                       'media', 'team', 'sales', 'enquiries', 'help', 'business', 'service',
                       'career', 'community', 'opportunities']

    list_emails = []

    for email in soup.find_all('a', {
        'href': [re.compile('^mailto'), re.compile('^http')]
    }):
        if 'mailto' in email.get('href'):
            if email.get('href')[7:] == '':
                domain = email.parent.parent.parent.find('a').get('href')
                if domain[:5] == 'https':
                    domain = domain[12:]
                    domain = re.sub('/', '', domain)
                    for i in range(len(email_beginning)):
                        email = email_beginning[i] + '@' + domain
                        list_emails.append(email)
                        count = count + 1
                else:
                    domain = domain[11:]
                    domain = re.sub('/', '', domain)
                    for i in range(len(email_beginning)):
                        email = email_beginning[i] + '@' + domain
                        list_emails.append(email)
                        count = count + 1
            else:
                count = count + 1
                email = email.get('href')[7:]
                list_emails.append(email)

    print(list_emails)

    with open('emails.csv', 'a') as file:
        for email in list_emails:
            file.write("%s\n" % email)
