# Risecodes_Demo
This is demo script for the assignment given by Risecodes for the role of QA &amp; Automation Tester. Language used is Python and framework used are Selenium and PytTest. This script can only be used on Chrome browser and windows OS.

In-order to run the script please make sure you have below mentioned packages and drivers installed on your windows operating system:

Python 3.8+ Verison. (https://www.python.org/downloads/) <- Downdload from here.

Check your chrome version and download chrome web driver. (https://www.businessinsider.com/guides/tech/what-version-of-google-chrome-do-i-have) <- How to check chrome version.

Download chrome web-driver and place it in same directory where the script file is present. (https://chromedriver.chromium.org/downloads) <- Dowload chrome web driver from here according to your chrome browser version.

Install these python packages before you run the script:
Selenium (https://pypi.org/project/selenium/) -> cmd to install selenium if python is installed -> (pip install selenium)
Pytest (https://pypi.org/project/pytest/) -> cmd to install pytest if python is installed -> (pip install pytest)

Once above enviroment setup is ready, open your terminal and go directory where script file is present.
In my case its "cd Risecodes_Demo"
Then type this command to run the script
"py.test -v -s"

It will start the script and ask for username and password input for first test case and rest of the test cases has pre-defined values just to demonstrate each test case.

