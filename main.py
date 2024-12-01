"""
JACKARYWARE

Thank you for using. This script is intended for Freebitco.in

PLEASE READ THE README.

I would much appreciate if you use my referral link: https://freebitco.in/?r=51036102

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import time
import random
import os
from pathlib import Path
import logging

home_dir = Path.home()
log_file_path = os.path.join(home_dir, 'Documents', 'Clicker_Log.txt')

logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

winnings_log_file_path = os.path.join(home_dir, 'Documents', 'Winnings.txt')
winnings_log = logging.getLogger('winnings_log')
winnings_log.setLevel(logging.INFO)
winnings_file_handler = logging.FileHandler(winnings_log_file_path)
winnings_file_handler.setLevel(logging.INFO)
winnings_log.addHandler(winnings_file_handler)


def humanImitator(min_time, max_time):
    sleep_time = random.uniform(min_time, max_time)
    time.sleep(sleep_time)


def close_popup(driver):
    try:
        deny_button = driver.find_element(By.XPATH, '//*[@class="pushpad_deny_button"]')
        driver.execute_script("arguments[0].click();", deny_button)
    except NoSuchElementException:
        pass

def roll(driver):
    target_div = driver.find_element(By.XPATH, '//*[@id="free_play_form_button"]')
    x = target_div.location['x']
    y = target_div.location['y']
    driver.execute_script(f"window.scrollTo({x}, {y});")
    target_div.click()


def writeScore(driver, log_total_count):
    reward_element = driver.find_element(By.XPATH, '//*[@id="winnings"]')
    reward_amt = reward_element.text.strip()

    roll_amt = ""
    try:
        ordinals = ["first", "second", "third", "fourth", "fifth"]
        for ordinal in ordinals:
            digit_element = driver.find_element(By.XPATH,f'//*[@id="free_play_digits"]/span[@id="free_play_{ordinal}_digit"]')
            roll_amt += digit_element.text.strip()
    except NoSuchElementException:
        error_message = "ERROR: Roll number digits not found!"
        print(error_message)
        logging.error(error_message)

    rollAmt_int = int(roll_amt)

    if rollAmt_int == 10000:
        logging.info("*^*JACKPOT*^*\t| BTC: " + reward_amt)
        winnings_log.info("*^*JACKPOT*^*\t| BTC: " + reward_amt)
        print("*^*JACKPOT*^*\t| BTC: " + reward_amt)
    elif 9986 < rollAmt_int < 10000:
        logging.info("LUCKY!!\t| Roll: " + roll_amt + "\t| BTC: " + reward_amt)
        winnings_log.info("LUCKY!!\t| Roll: " + roll_amt + "\t| BTC: " + reward_amt)
        print("LUCKY!!\t| Roll: " + roll_amt + "\t| BTC: " + reward_amt)
    elif 9886 < rollAmt_int < 9986:
        logging.info("NICE!\t| BTC: " + reward_amt)
        winnings_log.info("NICE!\t| BTC: " + reward_amt)
        print("NICE!\t| BTC: " + reward_amt)
    else:
        logging.info("ROLLED\t| Roll: " + roll_amt + "\t| BTC: " + reward_amt)
        winnings_log.info("ROLLED\t| Roll: " + roll_amt + "\t| BTC: " + reward_amt)
        print("ROLLED\t| Roll: " + roll_amt + "\t| BTC: " + reward_amt)

    log_total_count[0] += 1

    if log_total_count[0] % 7 == 0:
        try:
            balance = driver.find_element(By.XPATH, '//*[@id="balance"]')
            logging.info(">>>Current Balance: \t" + "BTC: " + str(balance.text))
            winnings_log.info(">>>Current Balance: \t" + "BTC: " + str(balance.text))
            print(">>>Current Balance: \t" + "BTC: " + str(balance.text))
        except NoSuchElementException:
            error_message = "ERROR: Balance element not found!!"
            print(error_message)
            logging.error(error_message)


def autoMacro():
    logging.info("[STARTUP]")
    print("[STARTUP]")
    logging.info("Initializing...")
    print("Initializing...")

    log_total_count = [0]

    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1280, 720)

    try:
        while True:
            logging.info("Waiting for login...")
            print("WELCOME: Please log in...")

            driver.get("https://freebitco.in/#")
            print("MACRO: This script takes about 30 seconds to activate, use that time to log in.\nIf you do not "
                  "have an"
                  "account, https://freebitco.in/?r=51036102.")
            print("\n")
            print("WELCOME: Please log in...")

            time.sleep(4.5)
            close_popup(driver)
            time.sleep(10.5)
            print("ACTIVE: Log file being written to " + log_file_path)
            print("MACRO: Winnings being written to " + winnings_log_file_path + "\nMACRO: 15 seconds remaining till "
                                                                                 "first click")
            time.sleep(15)

            try:
                while True:
                    try:
                        close_popup(driver)
                        time.sleep(1)

                        roll(driver)
                        time.sleep(2)

                        writeScore(driver, log_total_count)
                        time.sleep(3601)
                        humanImitator(14, 83)

                    except NoSuchElementException:
                        error_message = "ERROR: Roll button not found!\nHave you logged in?"
                        print(error_message)
                        logging.error(error_message)
                        print("WAITING: 15 seconds for login")
                        logging.info("Login timed out, waiting...")
                        time.sleep(15)

                    except ElementNotInteractableException:
                        error_message = "ERROR: Button not interactable. Checking for pop-up or " \
                                        "wait-timer..."
                        print(error_message)
                        logging.error("ERR: Roll button found, not interactable")
                        close_popup(driver)
                        try:
                            wait_time_element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[7]/div[3]/div[1]/span/span[1]/span")
                            wait_time_in_minutes = int(
                                wait_time_element.text.strip())

                            print(f"Waiting for {wait_time_in_minutes+60} minutes...")
                            time.sleep((wait_time_in_minutes * 60) + 60)
                        except NoSuchElementException:
                            print("Wait Timer not found.\nHave you logged in? Trying again in 10 seconds.")
                            logging.error("ERR: Wait timer not found!")
                            time.sleep(10)

            except NoSuchElementException:
                error_message = "ERROR: Roll button not found!\nHave you logged in?"
                print(error_message)
                logging.error(error_message)
                print("WAITING: 15 seconds for login")
                logging.info("Login timed out, waiting...")
                time.sleep(15)

    except KeyboardInterrupt:
        driver.quit()

if __name__ == "__main__":
    autoMacro()
