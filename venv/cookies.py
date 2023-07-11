from selenium import webdriver
import pickle

driver = webdriver.Chrome()
driver.get("https://freebitco.in")

# Log in and perform any necessary actions to generate the desired cookies
# ...

# Save the cookies to a file
with open("cookies.pkl", "wb") as file:
    pickle.dump(driver.get_cookies(), file)

driver.quit()
