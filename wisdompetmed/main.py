import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.wisdompetmed.com/'

response = requests.get(BASE_URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Find where the first title tag occurs in the code for veterinarian business name
print(soup.find('title').get_text())

#find all times the article tag occurs in the code for list of services
services = soup.find_all('article')

for service in services:
    print(service.get_text())

#find the business phone number
print('Phone number: ', soup.find('span', class_='phone').get_text().strip(), '\n')

#find all featured testimonials
print('----Testimonials----\n')
featured_testimonials = soup.find_all('blockquote')

for testimonial in featured_testimonials:
    print(testimonial.text)

#find all staff members
print('----Staff Members----\n')
staff = soup.find_all(
    'div', class_='info col-xs-8 col-xs-offset-2 col-sm-7 col-sm-offset-0 col-md-6 col-lg-8')

for s in staff:
  print(s.text)


#find all links on the Wisdom Pet Medicine website
print('----Page Links----\n')
links = soup.find_all('a')

for link in links:
    print(link.text, link.get('href'))

# write HTML code we pulled to a text file
with open('wisdom_vet.txt', 'w') as f:
    f.write(soup.prettify())