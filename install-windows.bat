@echo off

echo Preparing your system for Selenium and webdriver_manager...

REM Install pip
python -m ensurepip --upgrade --default-pip

REM Install virtualenv
pip install virtualenv

REM Create and activate a virtual environment
python -m venv selenium_env
call selenium_env\Scripts\activate.bat

REM Upgrade pip and setuptools
pip install --upgrade pip setuptools

REM Install required packages
pip install selenium
pip install webdriver_manager

echo System preparation completed successfully.

echo Downloading main.py and requirements.txt...

REM Download main.py and requirements.txt from GitHub
curl -O -L "https://raw.githubusercontent.com/koaque/faucet-node-macro/main/main.py"
curl -O -L "https://raw.githubusercontent.com/koaque/faucet-node-macro/main/requirements.txt"

echo Download completed.

echo You can now proceed with running your Selenium scripts using Python and the required dependencies.

REM Create a shortcut on the desktop
echo Creating shortcut on the desktop...
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = "%USERPROFILE%\Desktop\Faucet Macro.lnk" >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "%CD%\selenium_env\Scripts\python.exe" >> CreateShortcut.vbs
echo oLink.Arguments = "%CD%\main.py" >> CreateShortcut.vbs
echo oLink.WindowStyle = 1 >> CreateShortcut.vbs
echo oLink.IconLocation = "%CD%\selenium_env\Lib\site-packages\selenium\webdriver\common\chromedriver.exe" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs
cscript CreateShortcut.vbs

echo Shortcut created on the desktop.
echo You can double-click the "Faucet Macro" shortcut to run your Selenium script.

REM Clean up temporary script file
del CreateShortcut.vbs
