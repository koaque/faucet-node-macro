"""
JACKARYWARE

Thank you for using. This script is intended for Freebitco.in

PLEASE READ THE README.

I would much appreciate if you use my referral link: https://freebitco.in/?r=51036102

"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import time
import random
import os
import signal
import sys
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
    rewardAmt = reward_element.text.strip()

    rollAmt = ""
    try:
        ordinals = ["first", "second", "third", "fourth", "fifth"]
        for ordinal in ordinals:
            digit_element = driver.find_element(By.XPATH,f'//*[@id="free_play_digits"]/span[@id="free_play_{ordinal}_digit"]')
            rollAmt += digit_element.text.strip()
    except NoSuchElementException:
        error_message = "ERROR: Roll number digits not found!"
        print(error_message)
        logging.error(error_message)

    rollAmt_int = int(rollAmt)

    if rollAmt_int == 10000:
        logging.info("*^*JACKPOT*^*\t| BTC: " + rewardAmt)
        winnings_log.info("*^*JACKPOT*^*\t| BTC: " + rewardAmt)
        print("*^*JACKPOT*^*\t| BTC: " + rewardAmt)
    elif 9993 < rollAmt_int < 9994:
        logging.info("LUCKY!!\t| Roll: " + rollAmt + "\t| BTC: " + rewardAmt)
        winnings_log.info("LUCKY!!\t| Roll: " + rollAmt + "\t| BTC: " + rewardAmt)
        print("LUCKY!!\t| Roll: " + rollAmt + "\t| BTC: " + rewardAmt)
    else:
        logging.info("SUCCESS\t| Roll: " + rollAmt + "\t| BTC: " + rewardAmt)
        winnings_log.info("SUCCESS\t| Roll: " + rollAmt + "\t| BTC: " + rewardAmt)
        print("SUCCESS\t| Roll: " + rollAmt + "\t| BTC: " + rewardAmt)

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

    options = Options()
    options.add_argument('--headless=False')

    # Browser size control
    options.add_argument('window-size=1400x1000')
    driver = webdriver.Firefox(options=options)

    driver.set_window_size(1200, 700)

    def signal_handler(signal, frame):
        driver.quit()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

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
            print("ACTIVE: Log file being written to " + log_file_path + "\nMACRO: 15 seconds remaining till first click")
            time.sleep(15)
            time.sleep(2)

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
                                        "wait-timer.\nAttempting again in 30 seconds.\nIf this persists longer than 2 " \
                                        "hours, please check the Readme.txt"
                        print(error_message)
                        logging.error(error_message)
                        close_popup(driver)
                        time.sleep(30)

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
