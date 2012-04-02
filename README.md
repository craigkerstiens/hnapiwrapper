HN API Wrapper
--------------

## Overview

HN API Wrapper is intended to be several things. First it is a wrapper for the [hnsearch.com](www.hnsearch.com/api) API that supports returning JSONP allowing you to create callbacks as you like. Secondly it has a button for embedding on your site/blog to display your votes on HN as well as submit it.

## Setting up your own
To re-use this on your site simply:

* Clone this repository
* Create a heroku app for stack cedar
* Push the app to Heroku

To create your own version of the button you must edit the page location you've deployed to in button.js.

## Using the button

Include the below script within your page:

    <script type="text/javascript" src="http://hnapiwrapper.herokuapp.com/static/js/button.js"></script>
	

## To setup your own version

- Clone this repository
- Create a new heroku application
- Update your application name within js/button.js to include the correct url
- git push heroku master