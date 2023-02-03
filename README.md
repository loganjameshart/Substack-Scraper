# Substack Scraper
Scrapes an inputted Substack newsletter page and outputs to a Word doc. 

## How It's Made:

Using a combination of the Requests and Beautiful Soup libraries, this program scrapes a newsletter page (or multiple) and creates a Word document with them.

My best friend writes a Substack newsletter, so I wanted to make something to get the raw text of his pages that I could later use to make one of those word-density cloud things. 

## Lessons Learned:

An original version would go through each page based upon a Substack writer's archive page, but that Archive page is dynamic and doesn't show all of the page links unless you scroll down. I'd maybe want to use Selenium or find another means by which to grab all of the links from the archive page. My workaround for now was just to add each page link manually to the program through the persistent GUI window, which creates a link list internally.
