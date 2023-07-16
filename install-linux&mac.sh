#!/bin/bash

echo "Preparing your system for Selenium and webdriver_manager..."

# Ensure pip is installed
python3 -m ensurepip --upgrade

# Install virtualenv
pip3 install virtualenv

# Create and activate a virtual environment
python3 -m venv selenium_env
source selenium_env/bin/activate

# Upgrade pip and setuptools
pip3 install --upgrade pip setuptools

# Install required packages
pip3 install selenium
pip3 install webdriver_manager

echo "System preparation completed successfully."

echo "Downloading main.py and requirements.txt..."

# Download main.py and requirements.txt from GitHub
curl -O -L "https://raw.githubusercontent.com/koaque/faucet-node-macro/main/main.py"
curl -O -L "https://raw.githubusercontent.com/koaque/faucet-node-macro/main/requirements.txt"

echo "Download completed."

echo "You can now proceed with running your Selenium scripts using Python and the required dependencies."

# Create a shortcut-like script on the desktop
echo "Creating executable script on the desktop..."

echo '#!/bin/bash' > ~/Desktop/faucet_macro.sh
echo 'source selenium_env/bin/activate' >> ~/Desktop/faucet_macro.sh
echo 'python3 main.py' >> ~/Desktop/faucet_macro.sh

# Make the script executable
chmod +x ~/Desktop/faucet_macro.sh

echo "Executable script created on the desktop."
echo "You can double-click the \"Faucet Macro\" script to run your Selenium script."
