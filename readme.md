# Introduction
This web scraper demo extracts information from the CHIME Experiment homepage, specifically targeting the publications section. It will save the title, URL, and notes of each publication in a CSV file in the working directory.

# Execution

### Requirement
There are two dependencies required for this script to run.

```
BeautifulSoup4
requests
```

### Virtual Environment
It is recommended that you create a Python virtual environment to isolate dependencies.
To set up, follow these steps:

1. Create a Python virtual environment using
```python3 -m venv scrapper```.
  
3. Then enter the directory 'scrapper'
```cd scrapper```.

5. Activate the virtual environment
```source bin/activate```.

6. Clone this repository
```git clone https://github.com/justincodesample/python-web-scrapper.git```.

7. Enter the directory 'python-web-scrapper'
```cd python-web-scrapper```.

9. Install the dependencies
```pip install -r requirements.txt```

10. Execute the script
```python3 scrapper.py```

The result will be saved into a CSV file in the current working directory.
