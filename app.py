import json
from bs4 import BeautifulSoup

# Read index.html file
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements with the specified class
divs = soup.find_all('div', class_='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16')

# Prepare a list to store the extracted data
data = []

# Iterate over each div and extract the desired information
for div in divs:
    # Find the img element and extract the link
    img = div.find('img', class_='s-image')
    link = img['src'] if img else ''

    # Find the span element for the title
    span_title = div.find('span', class_='a-size-medium a-color-base a-text-normal')
    title = span_title.text if span_title else ''

    # Find the span element for the rating
    span_rating = div.find('span', class_='a-icon-alt')
    rating = span_rating.text if span_rating else ''

    # Find the span element for the price
    span_price = div.find('span', class_='a-price-whole')
    price = span_price.text if span_price else ''

    # Create a dictionary with the extracted data
    item_data = {
        'link': link,
        'title': title,
        'rating': rating,
        'price': price
    }

    # Append the item data to the list
    data.append(item_data)

# Write the extracted data to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print('Data extraction and JSON writing complete.')
