Prerequisites:

Before running the tests, ensure you have the following installed:

- Python 3.x
- Selenium (pip install selenium)
- Pytest (pip install pytest)
- Google Chrome and ChromeDriver

Clone the repository using commands:

- git clone <repository-url>
- cd <repository-directory>

Or you can clone the repository by:

- Open PyCharm
- Go to Git tab and select Clone
- Fill in the URL with: https://github.com/cameliag90/PhytonAutomation.git
- Click clone

Set up a virtual environment (optional but recommended):

- python -m venv venv
- source venv/bin/activate   # For Linux/MacOS
- venv\Scripts\activate      # For Windows

Install required dependencies:

- pip install -r requirements.txt

Update the chromedriver.exe path in the setup code if necessary.

Run Test Script:

- Right-click on your Python file in PyCharm.
- Choose "Run 'filename'" to execute your test script. or
- Open terminal and run: pytest path_to_test - for one test (ex: pytest regression/test_place_order_guest.py )