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
            
            # Find all <p> tags
            p_tags = soup.find_all('p')
            
            # Initialize a counter
            line_number = 1
            
            # Extract text from each <p> tag and concatenate into a single line
            p_texts = ''
            for p in p_tags:
                p_texts += f"{line_number}. {p.get_text(strip=True)}\n"
                line_number += 1
            
            return p_texts
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
url = "https://impressivelovehindi.blogspot.com/p/romantic-fialogir.html?m=1"
p_data = scrape_data(url)

if p_data:
    print("Data from <p> tags with line numbers:")
    # print(p_data)
    save_to_txt(p_data, 'p_data.txt')
else:
    print("Failed to retrieve data.")
