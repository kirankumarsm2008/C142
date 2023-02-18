import requests
from bs4 import BeautifulSoup
import csv

START_URL = "http://www.stellar-database.com/Scripts/search_star.exe?Name=brightest&Radius=5&TableName=on&Limit=5&Button=++Search++&ShowColumns=Nd&DisplayMode=1&TabSize=0&PageSize=20"

# Define the headers for the data
headers = ["Name", "Distance", "Mass", "Radius"]

# Create an empty list to store the data
star_data = []

# Fetch the HTML page using requests module
response = requests.get(START_URL)

# Parse the HTML using BeautifulSoup module
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the tables on the page
tables = soup.find_all('table')

# Extract data from the first table
table = tables[0]

# Find all the rows in the table
rows = table.find_all('tr')

# Loop through each row and extract the data
for row in rows:
    data = {}
    # Find all the columns in the row
    cols = row.find_all('td')
    # Extract the data and store it in the dictionary
    data["Name"] = cols[0].text.strip()
    data["Distance"] = cols[1].text.strip()
    data["Mass"] = cols[2].text.strip()
    data["Radius"] = cols[3].text.strip()
    # Append the dictionary to the list
    star_data.append(data)

# Create a CSV file and write the data to it
with open("star_data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for data in star_data:
        writer.writerow(data)
