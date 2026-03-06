# Market Data Analyzer

Simple Python project that fetches Bitcoin price from the CoinGecko API and stores it in a local SQLite database.

## Features

- Fetch cryptocurrency price from public API
- Store price history in SQLite database
- Add timestamp for each observation
- Display stored price history

## Tech Stack

- Python
- Requests (HTTP API calls)
- SQLite
- SQL

## How to run

Create virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install requests

Run the program:
python3 main.py

## Project purpose

This project demonstrates a simple data pipeline:

API → Python → SQL database