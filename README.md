# lichess consumer
This is my submission for the ktp take home project

## Overview
This application uses pocketbase to locally host the database as well as streamlit locally host the frontend service

The applications are port forwarded through docker so if you click the links in the logs they will not work

Instead visit these domains to view the application

>view the frontend at localhost:8200

>view the database admin console at localhost:8100/_/

The username and password are `admin@gmail.com` and `password123`

## Components
`main_app` contains logic for interacting the the lichess api and writes the data to `data.csv` then uses the csv file to write to the database

`db` contains dockercompose to set up pocketbase server

`frontend` consumes from pocketbase api to read the database and shows data for the top 25 users

## Dependencies
[Docker desktop](https://docs.docker.com/desktop/) is needed for this application

## Running application
Make sure docker desktop is running

To start the application use `docker compose up` from the root directory of project



