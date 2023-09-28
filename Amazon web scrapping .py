#!/usr/bin/env python
# coding: utf-8

# In[18]:


from bs4 import BeautifulSoup as soup
import requests
import smtplib
import time
import datetime


# In[19]:


# Connect to Website and pull in data

import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}

try:
    page = requests.get(URL, headers=headers)
    page.raise_for_status()  # Check for any request errors

    soup1 = BeautifulSoup(page.content, "html.parser")

    # Find the title
    title_element = soup1.find(id='productTitle')
    if title_element:
        title = title_element.get_text(strip=True)
    else:
        title = 'Title not found'

    # Find the price
    price_element = soup1.find(id='priceblock_ourprice')
    if price_element:
        price = price_element.get_text(strip=True)
    else:
        price = 'Price not found'

    print("Title:", title)
    print("Price:", price)

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
except Exception as e:
    print("An unexpected error occurred:", e)


# In[20]:


# Clean up the data a little bit
if title is not None:
    title = title.strip()
else:
    title = "Title not found"

if price is not None:
    price = price.strip()[1:]
else:
    price = "Price not found"

print("Title:", title)
print("Price:", price)


# In[21]:


# Create a Timestamp for your output to track when data was collected

import datetime

today = datetime.date.today()

print(today)


# In[22]:


# Create CSV and write headers and data into the file

import csv
from datetime import date

header = ['Title', 'Price', 'Date']

# Assuming you have values for title and price
title = "Product Title"
price = 19.99

# Get today's date
today = date.today().strftime("%Y-%m-%d")

data = [title, price, today]

with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[39]:


import pandas as pd

# Use a raw string or double backslashes in the file path
file_path = r'C:\Users\nzekwe.patrick\OneDrive - Emerging Markets Telecommunication Services Limited\Documents\Book1.csv'

df = pd.read_csv(file_path)

print(df)


# In[37]:


#Now we are appending data to the csv

import csv  # Import the csv module

# Define your data as a list of values (replace this with your actual data)
data = ["Value1", "Value2", "Value3"]

# Open the CSV file in 'a+' mode to append data
with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[31]:


#Combine all of the above code into one function


import requests
from bs4 import BeautifulSoup
import datetime
import csv


# In[32]:


def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
    }

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title_element = soup2.find(id='productTitle')
    price_element = soup2.find(id='priceblock_ourprice')

    if title_element and price_element:
        title = title_element.get_text().strip()
        price = price_element.get_text().strip()[1:]
    else:
        title = "Title not found"
        price = "Price not found"

    today = datetime.date.today()

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('Book1.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

# Call the check_price() function to execute the web scraping and data writing
check_price()


# In[33]:


# Runs check_price after a set time and inputs data into your CSV

import requests
from bs4 import BeautifulSoup
import datetime
import csv
import time

def check_price():
    # ... (the rest of your check_price() function as before)

#while True:
    try:
        check_price()
        print("Data scraped successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    time.sleep(86400)  # Sleep for 24 hours (86,400 seconds)


# In[34]:


import pandas as pd

df = pd.read_csv(r'c:\Users\nzekwe.patrick\OneDrive - Emerging Markets Telecommunication Services Limited\Documents\Book1.csv')

print(df)


# In[36]:


#If you want to try sending yourself an email (just for fun) when a price hits below a certain level you can try it
# out with this script

def send_mail():
   server = smtplib.SMTP_SSL('smtp.gmail.com',465)
   server.ehlo()
   #server.starttls()
   server.ehlo()
   server.login('AlexTheAnalyst95@gmail.com','xxxxxxxxxxxxxx')
   
   subject = "The Shirt you want is below $15! Now is your chance to buy!"
   body = "Alex, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
  
   msg = f"Subject: {subject}\n\n{body}"
   
   server.sendmail(
       'AlexTheAnalyst95@gmail.com',
       msg
    
   )


# In[ ]:




