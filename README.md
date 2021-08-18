# Work Sample
## Description
This project contains a Flask App API with two endpoints:
* POST /crawl - Send POST request with a payload containing URL. See formatting example under 'How to use it'. The endpoint will scrape the page if available, store the scraped content as a JSON and return the ID to the corresponding entry. Endpoint will return "Inconsistent URL - try again" if URL is not correctly formatted.

* GET /retrieve/<ID> - Get the corresponding JSON with scraped content for a given ID in the query. If there is no content for saved for the given ID, an empty JSON will be returned.

## Requirements
Requirements are stated in file requirements.txt. Make virtual environment and download the requirements using 'pip install -r /path/to/requirements.txt'

## How to use it
Download folder. Enter virtual enviroment and ensure all requirements are installed correctly. Start server using 'python flaskapp.py'. Send requests in using i.e. Postman, Apache Jmeter or Python Requests. 

Examples using Requests from command:

> r=requests.post('http://localhost:5000/crawl', data={'URL':'https://quotes.toscrape.com'})
  
> r.text

>'46075364-150c-4e1a-b0f7-6475ab9d44a2'

> r=requests.get('http://localhost:5000/retrieve/46075364-150c-4e1a-b0f7-6475ab9d44a2')
  
> r.text

>'{"date":"2021-08-17 15:29:09.943488","title":"[<title>Quotes to Scrape</title>]","url":"https://quotes.toscrape.com"}\n'


## Comments
1. This solution is based on my understanding of the task. Main assumption is that the first endpoint is not supposed to extract new links and continue scraping, but only scrape the given URL. 
2. Flask App is implemented to handle concurrent requests by necessary threads. 
3. Information is stored in memory dictionary for the purpose of this task.
