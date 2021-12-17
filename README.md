# FastAPI TODO crude example

This is a simple project to test difference in performance between asynchronous and synchronous endpoints. All endpoints
were created in both ways in very similar fashion for easier compare

## How to start?
The easiest way to start and test project is by using docker-compose. In the main directory of project just type
in terminal:

> $ docker-compose up

### Setting up database and populating data
Before testing and of endpoint it is good idea to create all required tables and some sample data in database. You
can achieve it using this commands when PostgreSQL container is running:

To create all tables:
> $ docker-compose run app python manage.py initdb 

To populate DB with data:
> $ docker-compose run app python manage.py populatedb
