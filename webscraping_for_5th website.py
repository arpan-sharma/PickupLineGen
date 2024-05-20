from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

def scrape_data(url):
    try:
        # Set up Firefox options
        options = Options()
        options.headless = True
        
        # Initialize the Firefox webdriver
        driver = webdriver.Firefox(options=options)
        
        # Open the URL
        driver.get(url)
        
        # Wait for the page to load
        driver.implicitly_wait(10)
        
        # Get the page source after waiting
        page_source = driver.page_source
        
        # Close the webdriver
        driver.quit()
        
        # Parse the HTML content
        soup = BeautifulSoup(page_source, 'html.parser')
        
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
url = "https://www.livehindustan.com/lifestyle/relationship/story-happy-flirting-day-2023-best-pick-up-lines-to-do-healthy-flirting-with-partner-or-crush-7787622.html"
p_data = scrape_data(url)

if p_data:
    print("Data from <p> tags with line numbers:")
    print(p_data)
    save_to_txt(p_data, 'p_data_livehindustan.txt')
else:
    print("Failed to retrieve data.")
