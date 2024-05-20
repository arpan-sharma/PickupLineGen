import requests
from bs4 import BeautifulSoup

def scrape_li_data(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all <li> tags
            li_tags = soup.find_all('li')
            
            # Extract text from each <li> tag and concatenate into a single string
            li_texts = '\n'.join([li.get_text(strip=True) for li in li_tags])
            
            return li_texts
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_to_txt(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(data)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving to {filename}: {e}")

# Example usage
url = "https://www.stylecraze.com/hindi/flirty-lines-for-girlfriend-in-hindi/"
li_data = scrape_li_data(url)

if li_data:
    print("Data from <li> tags:")
    print(li_data)
    save_to_txt(li_data, 'li_data_stylecraze.txt')
else:
    print("Failed to retrieve data.")
