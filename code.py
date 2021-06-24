'''
To scrape BBC headlines from
https://www.bbc.com/news/world/asia/india

author: Ankan Bera
created: 24/06/2021
'''
import requests
import bs4
import re
from datetime import datetime


def write_to_html(title, headlines, summaries, links, min_len, base_url):
    html_head= '''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>''' +title.text +'''</title>
                </head>
                <body>
                '''

    html_headlines= []
    html_summary= []
    html_links = []
    for i in range(min_len):
        heading= '<h2>' +headlines[i].text + '</h2>'
        html_headlines.append(heading) if heading not in html_headlines else None
        summary = '<p>'+summaries[i].text +'</p>'
        html_summary.append(summary) if summary not in html_summary else None
        link = '<a href="' + base_url + links[i]['href'] + '" target="_blank">Link</a>'
        html_links.append(link) if link not in html_links else None

    html_body = '''<body>
                    <h2>''' + datetime.strftime(datetime.today(),'%A, %B %d, %Y')+ '''</h2>
                    <h1> Today's headlines </h1>'''

    min_len = min([len(html_headlines), len(html_links), len(html_summary)])
    for i in range(min_len):
        html_body += html_headlines[i] +'\n' + html_summary[i]+ '\n' + html_links[i] + '\n'
    
    html_body += '</body>\n</html>'
    html_full = html_head + html_body
    html_file = 'D:\\BBC_Headlines.html'

    with open(html_file, 'w') as f:
        f.write(html_full)

def main_function():
    base_url = 'https://www.bbc.com'

    url = '/news/world/asia/india'
    result= requests.get(base_url+url)

    soup = bs4.BeautifulSoup(result.text,'lxml')

    title = soup.select('title')

    soup = soup.select('.no-mpu')[0]

    headlines= soup.select('h3', title= re.compile('^gs-c-promo-heading'))

    links = soup.find_all('a', class_= re.compile('^gs-c-promo-heading'))

    summary= soup.find_all('p', class_= re.compile('^gs-c-promo-summary'))

    min_len = min([len(headlines), len(links), len(summary)])

    write_to_html(title[0], headlines, summary, links, min_len, base_url)

    return True

if __name__ == "__main__":
    main_function()
