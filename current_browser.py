from selenium import webdriver

# Open a driver (e.g., Firefox)
driver = webdriver.Chrome()

# Extract URL and session ID from the driver object
url = driver.command_executor._url  # "http://127.0.0.1:60622/hub"
session_id = driver.session_id      # '4e167f26-dc1d-4f51-a207-f761eaf73c31'

# Check if the URL is valid
if url:
    try:
        # Use the URL and session ID to reconnect to the driver
        driver = webdriver.Remote(command_executor=url)
        driver.close()  # This prevents the dummy browser
        driver.session_id = session_id
        # Now you are connected to your driver again
        driver.get("http://www.mrsmart.in")
    except Exception as e:
        print("Error:", e)
else:
    print("Command executor URL is not valid.")
