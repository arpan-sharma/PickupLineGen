import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all <li> tags
            li_tags = soup.find_all('li')
            
            # Extract text from each <li> tag
            li_texts = [li.get_text(strip=True) for li in li_tags]
            
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
            for item in data:
                file.write(item + '\n')
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving to {filename}: {e}")

# Example usage
url = "https://thepleasantconversation.com/cute-pick-up-lines/"
li_data = scrape_data(url)

if li_data:
    save_to_txt(li_data, 'li_data.txt')
else:
    print("Failed to retrieve data.")
