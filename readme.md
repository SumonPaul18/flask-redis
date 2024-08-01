#
# Containerize a Redis Flask Application using Docker Compose

  - <b>Flask</b> is an open-source Python micro framework for building web applications. It is implemented on implemented on Werkzeug and Jinja2. 
  - <b>Redis</b> is a vibrant open source in-memory data store platform. Developers use Redis as a message broker, database, streaming engine and for application caching.

We will use Redis for caching. Caching is a computing technique that enables applications to temporarily store data, files, and login details in the Random Access Memory. It enable faster retrievals of that data and the application will load faster.

In this tutorial, We will build a sample Python Flask application and implement Redis for caching. We will then containerize the Redis Flask application using Docker Compose. Docker Compose is a powerful Docker tool for creating and running multi-container Docker applications. Our application will have two containers. The first container will host the Flask application. The other container will be for Redis caching. Docker Compose will run the two containers as a single application. Lets get started

#### Prerequisites
Before you get started, you must understand Docker. You also need the following set up in your working machine:

  - Vs Code for code editing.
  - Python installed.
  - Docker Desktop set up.
