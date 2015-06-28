# Scraping SO

## Install

- pip install -r requirements.txt

## Running the crawler

- `scrapy crawl stack_crawler`
	
	- To pipe the contents of crawled response to a file:

	`scrapy crawl stack 2> crawled.txt`

	- To save the JSON response in another file:
	
	`scrapy crawl stack_crawler -o final.json -t json`

## Suggestions and Issues

Start an issue in the issue tracker or send a pull request .
