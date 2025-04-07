# Creating a database from Ebay search terms

**Description:** 

In order to demonstrate Python's functionality to open and extract information from webpages, this program collects product information from the first ten pages of an ebay listing and stores them in a json file. 

## Running the file

Follow the steps below to run the `ebay-dl.py` script and generate the three JSON files in the repository.

---

## 1. Set Up the Environment

I used Python 3.13 and used the following libraries: 


```bash
pip install bs4
pip install argparse
pip install requests
pip install json

```
In order to enter the search term, you write this on command line:

```bash
python3 ebay-dl.py search-term
```

My inputs were:

```bash
python3 ebay-dl.py travis scott jordans
python3 film camera
python3 sushi micromallow
```
The json files are then stored in a folder in the Downloads folder: you would have to change the code that relates to file locations in order to get it to work properly.

Here is a [link](https://github.com/mikeizbicki/cmc-csci040/tree/2025spring/project_03_webscraping#project-3-scraping-from-ebay) to the course project to which this project owes its allegiance.



