from bs4 import BeautifulSoup
import csv
import requests

page = requests.get("https://chime-experiment.ca/en")

# check if the request is successful
print(page.status_code)

# save raw, unprocessed data into a variable.
raw = page.content
soup = BeautifulSoup(raw, 'html.parser')

# our target is the "CHIME Publications".
header = ['Titles', 'URL', 'Notes']
rows = []

# find the list of publications under "CHIME Publications" section.
for li in soup.find(name='h2', text='CHIME Publications').find_next_sibling(name='ul'):
    url = li.find(href=True)
    rows.append([li.find('a', href=True).contents[0], url['href'], li.contents[2]])

# save the data into a CSV file.
with open('chime-experiment-publications.csv', 'w', encoding='utf-8', newline='\n') as pg:
    writer = csv.writer(pg, delimiter =',', dialect='excel', lineterminator='\r\n')
    writer.writerow(header)
    for x in rows:
        writer.writerow(x)
