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

Optional params:
* `-a` - outputs each site being scraped instead of a percentage 

Licence
========
Open Source Initiative OSI - The MIT License

http://www.opensource.org/licenses/mit-license.php

Copyright (c) 2014 Alan Salnikov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
