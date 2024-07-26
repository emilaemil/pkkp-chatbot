# PKKP Chatbot

## Description

The PKKP Chatbot is a web-based application that uses machine learning models to provide automated responses to user messages. The application is built using Flask as the web framework and TensorFlow for the machine learning model.

## Project Structure

- `app.py`: The main file containing the Flask application code, including input processing, model prediction, and response delivery.
- `dataset.json`: Dataset containing patterns and tags used to train the chatbot model.
- `chatbot_model.h5`: TensorFlow model file trained for the chatbot.
- `templates/index.html`: HTML template for the user interface.
- `static/images/`: Folder for static file such as image logo.

## Prerequisites

Before running the application, ensure you have all the following dependencies installed:

- Python 3.11
- TensorFlow
- Flask
- NumPy
- scikit-learn

## Installation

1. **Clone Repository**

   ```sh
   git clone https://github.com/username/repo-name.git
   cd repo-name

   ```

2. **Install Depedencies**

   Create and activate a virtual environment (optional but recommended)

   ````sh
   git clone https://github.com/username/repo-name.git
   cd repo-name

   Install all dependencies using `pip`
   ```sh
   pip install -r requirements.txt

   If you don't have `requirements.txt`, you can create it with
   ```sh
   pip freeze > requirements.txt

   ````

3. **Provide Model and Dataset**

   Place the `chatbot_model.h5` and `dataset.json` files in your project directory.

## Running the Application

To run the Flask application, use the following command:

````sh
python app.py

The application will be available at `http://localhost:5000` by default. You can access the user interface through a browser and interact with the chatbot.

## API Testing

You can test the chatbot API by sending a POST request to the /chatbot endpoint with the following JSON format:
```json
{
  "message": "Your message"
}

The API response will contain the chatbot's response in JSON format:
```json
{
  "responses": "Chatbot's response"
}

## Author
- Emila
````
