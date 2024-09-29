from flask import Flask, request, jsonify, make_response
import requests
import db
import logging
import os
from dotenv import load_dotenv

app = Flask(__name__)


load_dotenv()

API_KEY = os.getenv('API_KEY')

logging.basicConfig(filename='api.log', level=logging.DEBUG)

EXTERNAL_API_URL = 'http://api.openweathermap.org/data/2.5/weather'


@app.route('/api/customers', methods=['GET'])
def get_all_customers():
    """Get all customer records."""
    try:
        customers = db.get_all_customers()
        customer_list = [{"id": customer[0], "name": customer[1], "info": customer[2]} for customer in customers]
        return jsonify(customer_list)
    except Exception as e:
        app.logger.error(f"Error fetching customers: {str(e)}")
        return make_response(jsonify({"error": "Error fetching customers"}), 500)


@app.route('/api/customers/<int:data_id>', methods=['GET'])
def get_customer_by_id(data_id):
    """Get a customer by their ID."""
    try:
        customer = db.get_customer(data_id)
        if customer:
            return jsonify({"id": customer[0], "name": customer[1], "info": customer[2]})
        else:
            return make_response(jsonify({"error": "Customer not found"}), 404)
    except Exception as e:
        app.logger.error(f"Error fetching customer by ID: {str(e)}")
        return make_response(jsonify({"error": "Error fetching customer"}), 500)


@app.route('/api/customer', methods=['POST'])
def add_customer():
    """Add a new customer record."""
    try:
        new_data = request.json
        name = new_data.get("name")
        info = new_data.get("info")
        db.add_customer(name, info)
        return make_response(jsonify({"message": "Data added successfully"}), 201)
    except Exception as e:
        app.logger.error(f"Error adding data: {str(e)}")
        return make_response(jsonify({"error": "Error adding data"}), 500)


@app.route('/api/weather', methods=['GET'])
def get_weather():
    """Get weather information for a city using an external API."""
    city = request.args.get('city')
    if not city:
        return make_response(jsonify({"error": "City not provided"}), 400)

    try:
        params = {'q': city, 'appid': API_KEY}
        response = requests.get(EXTERNAL_API_URL, params=params)
        data = response.json()
        if response.status_code == 200:
            return jsonify(data)
        else:
            return make_response(jsonify({"error": data.get("message", "Error fetching weather")}), response.status_code)
    except Exception as e:
        app.logger.error(f"Error fetching weather: {str(e)}")
        return make_response(jsonify({"error": "Error fetching weather"}), 500)


@app.route('/api/docs', methods=['GET'])
def get_api_docs():
    """Serve API documentation in YAML format."""
    try:
        with open('api_docs.yaml', 'r') as docs:
            return make_response(docs.read(), 200, {'Content-Type': 'text/yaml'})
    except FileNotFoundError:
        return make_response(jsonify({"error": "API documentation not found"}), 404)



if __name__ == '__main__':
    db.create_table()
    app.run(debug=True)
