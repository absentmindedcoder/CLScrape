CLScrape
========

Python script to scrape multiple craigslist locations

Requires
========

* BeautifulSoup4

Setup
========

* `sites` - the list of regional craigslist urls
* `searches` - list of dictionaries that contain two entries. `url` is the search is what is after the base url that contains all the terms to execute the search. `item` is used in the output to inform you how many results were found for the search
* `days` - how many days back a post in the results can appear
* `resultsPath` - path to where the output file. Default: the directory the script is run in.
 
How to run
===========

`python scrape.py`
