import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = "https://a.msn.com/54/en-us/ct34.056,-117.183?ocid=ansmsnweather"
response = requests.get(url)
response.raise_for_status()  # Ensure we notice bad responses

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract temperatures
# Note: The actual HTML structure needs to be inspected to find the correct tags and classes
current_temp_tag = soup.find('span', class_='current-temp-class')  # Replace with actual class
current_temp = current_temp_tag.text if current_temp_tag else "N/A"
low_temp_tag = soup.find('span', class_='low-temp-class')  # Replace with actual class

high_temp = high_temp_tag.text if high_temp_tag else "N/A"
low_temp = low_temp_tag.text if low_temp_tag else "N/A"

# Step 4: Print the temperatures
print(f"Today's high temperature: {high_temp}")
print(f"Today's low temperature: {low_temp}")