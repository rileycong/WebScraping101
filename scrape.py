from bs4 import BeautifulSoup
import requests
import csv

# link to the web
source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')

# Cho vào file csv sau khi scrape
csv_file = open('web_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

## The Scrape Begins ##
# Find all article to scrape
for article in soup.find_all('article'):
    # Get the headline
    headline = article.h2.a.text
    print(headline)

    # Get the summary
    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    # Use try and except to not be thrown an error when there is no link
    try:
        # Get the YouTube source
        vid_src = article.find('iframe', class_='youtube-player')['src']
        # Get the id
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        # Final link
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as lol:  
        yt_link = None
    print(yt_link)
    
    # Cách dòng giữa mỗi lần iterate
    print()

    # Put data in CSV
    csv_writer.writerow([headline, summary, yt_link])

# Close CSV vì không dùng cái context manager 'with open ... as'
csv_file.close()