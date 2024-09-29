# Service-Design-IoT23
Service Design assignment IoT23


# Flask API Project

This is a Flask-based API project that allows you to manage customer data and retrieve weather information through an external API. The project is designed to be easily set up with secure API key management using environment variables.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
- [API Endpoints](#api-endpoints)
- [Accessing API Documentation](#accessing-api-documentation)

## Features

- Add, retrieve, and manage customer data.
- Retrieve real-time weather information using the OpenWeatherMap API.
- API key management through a `.env` file for security.
- API documentation served at an accessible endpoint.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager)
- [Git](https://git-scm.com/)

## Getting Started

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository

First, clone the repository to your local machine using Git.

```bash
git clone https://github.com/your-username/API_service.git
cd API_service
```


### 2. Set Up Virtual Environment (Optional but recommended)

To avoid conflicts between dependencies, it's a good idea to create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate     # For Linux/Mac
# OR
venv\\Scripts\\activate        # For Windows
```

### 3. Install Dependencies

Install the project dependencies specified in the requirements.txt file.

```bash
pip install -r requirements.txt
```

### 4. Create and Configure the .env File

Create a .env file in the project root to securely store your API key:

```bash
touch .env
```

Add the following line to the .env file:

```env
API_KEY=your_openweathermap_api_key
```

Replace your_openweathermap_api_key with your actual API key from OpenWeatherMap.

### 5. Initialize the Database

Run the project to automatically create the SQLite database and table:

```python
python main.py
```

You should see that the database is initialized and the API is running at http://localhost:5000.

## Project Structure

Here's an overview of the key files and directories:

```
.
├── db.py              # Database connection and helper functions
├── main.py            # Main Flask application
├── api_docs.yaml      # API documentation in YAML format
├── requirements.txt   # Python dependencies
├── .env               # Environment variables (API key)
├── .gitignore         # Ignoring .env and other unnecessary files
└── README.md          # This readme file
```

## How to Use

### 1. Run the Flask App
Start the Flask development server:

```bash
python main.py
```

By default, the app runs on http://localhost:5000.

### 2. Interact with the API

You can now use any API client like Postman or curl to interact with the API.

For example, to add a customer:

```postman
curl -X POST http://localhost:5000/api/customer \\
-H "Content-Type: application/json" \\
-d '{
  "name": "John Doe",
  "info": "Regular customer, prefers online consultations."
}'
```

To retrieve the weather for a city:

```
curl http://localhost:5000/api/weather?city=London
```

## API Endpoints

| HTTP Method | Endpoint                        | Description                             |
|-------------|---------------------------------|-----------------------------------------|
| `GET`       | `/api/customers`                | Fetch all customers                     |
| `GET`       | `/api/customers/{id}`           | Fetch a customer by ID                  |
| `POST`      | `/api/customer`                 | Add a new customer                      |
| `GET`       | `/api/weather?city={city}`      | Fetch weather data for a given city     |



## Accessing API Documentation
The project includes auto-generated API documentation that can be accessed by visiting:

```bash
http://localhost:5000/api/docs
```

This will provide detailed information about each endpoint, including request parameters and example responses.
