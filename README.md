# Hotwire Native Demo (Django version)

A small web app to demonstrate how to use Hotwire with the Hotwire Native frameworks. The demo app is available at [https://hotwire-native-demo.placepython.com](https://hotwire-native-demo.placepython.com) and the source code can be found at [https://github.com/placepython/hotwire-native-demo-django](https://github.com/placepython/hotwire-native-demo-django).

This demo version is a port of the [original application](https://github.com/hotwired/hotwire-native-demo) written in Node.js and Express.js. 

## Running Locally

I use [uv](https://docs.astral.sh/uv/) as my python venv and dependency manager. Feel free
to substitute with your own preference (pipenv, poetry, or... why not, venv+pip).

Clone the repo, and then:

```
$ uv venv 
$ uv sync --dev
$ uv run python manage.py migrate
$ uv run python manage.py runserver
```

The server is running on [`localhost:8000`](http://localhost:8000). You can open that url in the browser and ensure the native app is using the same url.