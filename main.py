"""
JACKARYWARE

Thank you for using. This script is intended for Freebitco.in

PLEASE READ THE README.

I would much appreciate if you use my referral link: https://freebitco.in/?r=51036102

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
import signal
import sys
from pathlib import Path
import logging

home_dir = Path.home()
log_file_path = os.path.join(home_dir, 'Documents', 'Clicker_Log.txt')

# Configure the logging
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def autoclicker():
    logging.info("[STARTUP]")
    logging.info("Initializing...")

    log_total_count = 0

    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)

    def signal_handler(signal, frame):
        driver.quit()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    logging.info("Waiting for login.")
    print("WELCOME: Please log in...")

    driver.get("https://freebitco.in/#")
    print("This script takes about 30 seconds to activate, use that time to log in.\nIf you do have have an "
          "account, https://freebitco.in/?r=51036102.")
    print("\n\n")
    print("WELCOME: Please log in...")
    time.sleep(30)

    print("ACTIVE: Log file being written to " + log_file_path)

    try:
        while True:
            try:
                target_div = driver.find_element(By.XPATH, '//*[@id="free_play_form_button"]')
                x = target_div.location['x']
                y = target_div.location['y']

                driver.execute_script(f"window.scrollTo({x}, {y});")

                target_div.click()

                try:
                    reward_element = driver.find_element(By.XPATH, '//*[@id="winnings"]')
                    rewardAmt = reward_element.text.strip()

                    rollAmt = "00000"
                    try:
                        ordinals = ["first", "second", "third", "fourth", "fifth"]
                        for ordinal in ordinals:
                            digit_element = driver.find_element(By.XPATH, f'//*[@id="free_play_{ordinal}_digit"]')
                            rollAmt += digit_element.text.strip()

                    except NoSuchElementException:
                        error_message = "ERROR: Roll number digits not found!"
                        print(error_message)
                        logging.error(error_message)

                    rollAmt_int = int(rollAmt)

                    if rollAmt_int == 10000:
                        logging.info("*^*JACKPOT*^*\t| BTC: " + rewardAmt)
                        print("*^*JACKPOT*^*\t| BTC: " + rewardAmt)
                    elif 9993 < rollAmt_int < 9994:
                        logging.info("LUCKY!!\t| Roll: " + rollAmt + "\t| BTC: " + rewardAmt)
                        print("LUCKY!!\t| Roll: " + rollAmt + "\t| BTC: " + rewardAmt)
                    else:
                        logging.info("SUCCESS\t| Roll: " + rollAmt + "\t| BTC: " + rewardAmt)
                        print("SUCCESS\t| Roll: " + rollAmt + "\t| BTC: " + rewardAmt)


                    log_total_count += 1

                    if log_total_count % 7 == 0:
                        try:
                            balance = driver.find_element(By.XPATH, '//*[@id="balance"]')
                            logging.info(">>>Current Balance: \t" + "BTC: " + str(balance.text))
                        except NoSuchElementException:
                            error_message = "ERROR: Balance element not found!!"
                            print(error_message)
                            logging.error(error_message)

                except NoSuchElementException:
                    error_message = "ERROR: Reward or Roll element not found!"
                    print(error_message)
                    logging.error(error_message)
                    rewardAmt = "Null"
                    rollAmt = "0000"

            except NoSuchElementException:
                error_message = "ERROR: Roll button not found! Have you logged in?"
                print(error_message)
                logging.error(error_message)
                print("WAITING: 30 seconds")
                logging.info("WAITING: 30 seconds")
                time.sleep(30)

            time.sleep(3610)

    except KeyboardInterrupt:
        driver.quit()


if __name__ == "__main__":
    autoclicker()
