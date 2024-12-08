from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def morning_routine_automation():
    # Set up WebDriver (Replace the path with your WebDriver's location)
    driver = webdriver.Chrome(executable_path="path/to/chromedriver")
    
    # Define URLs
    urls = {
        "Meditation Music": "https://open.spotify.com/playlist/37i9dQZF1DWZqd5JICZI0u",  # Meditation playlist
        "Online Timer": "https://www.google.com/search?q=online+timer",  # Timer
        "Speaking Practice": "https://www.youtube.com/c/VinhGiang",  # Vinh Giang's channel
        "Tech News": "https://techcrunch.com/",
        "Finance News": "https://www.bloomberg.com/",
        "Shower Thoughts Recorder": "https://keep.google.com/"  # Google Keep
    }
    
    # Open each URL in a new tab
    for name, url in urls.items():
        driver.execute_script(f"window.open('{url}', '_blank');")
        time.sleep(1)  # Pause to avoid overwhelming the browser
    
    print("Morning routine tabs are ready!")
    
    # Optionally, you can close the driver after use
    # driver.quit()

# Run the automation
morning_routine_automation()
