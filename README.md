# Nouvelles Center

## Built By [Faith Kwamboka Okong'o](https://github.com/FaithKwamboka)

## Description
Nouvelles is a web app that allows the user to view global news of different categories and sources. The app also allows users to see the date an article wa published and read the full article. This is achieved by using the [News API](https://newsapi.org/).

You can view the site at:[Heroku](https://nouvelles1.herokuapp.com/)

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* See various news sources and categories
![news1](https://user-images.githubusercontent.com/100117264/166223780-de5a599e-f1aa-4102-b809-19c5fbe45cfc.png)

* Select the ones they prefer
* Navigate to a particular news source e.g https://nouvelles1.herokuapp.com/CNN
* See the news articles from that news source
* See the image, description and time the news article was created
![news2](https://user-images.githubusercontent.com/100117264/166223793-bcb6b86d-d80e-44ab-86e2-fdf750705921.png)

* Click on an article and read it fully from the news source

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news by category from different sources | **On page load** | List of various news sources is displayed in a list |
| Display articles from a news source by category | **On tab link click** | Redirected to a page with articles of the specified category from the source |
| Display articles from a news source | **On navigation via the tab e.g: https://nouvelles1.herokuapp.com/CNN  ** | Redirected to a page with articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image,description and publication date |
| To Read an entire article  | **Click an article** | Redirected to the news source's site to read the entire article |


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* virtualenv

### Cloning
* In your terminal:

        $ git clone https://github.com/FaithKwamboka/News_API.git
        $ cd NewsAPI

## Running the Application
* Creating the virtual environment

        $ virtualenv virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ pip install flask
        $ pip install flask-bootstrap
        $ pip install Flask-Script
        $ pip install flask-wtf

* Setting up the API Key

        To be able to gather article info from the News API you will need an API Key.

        * Visit https://newsapi.org/ and register for an API key.
        * In the root directory of the project folder create a file: start.sh
        * Insert the following info into it:

                export NEWS_API_KEY='<Your-Api-Key>'
                python3.8 manage.py server

        * Insert the API Key you received from News Api where <Your-Api-Key> is.

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.8 manage.py tests

## Technologies Used
* Python3.8
* Flask
* HTML
* CSS

## [License](https://github.com/FaithKwamboka/News_API/blob/master/LICENSE)


