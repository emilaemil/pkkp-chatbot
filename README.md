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

To run the application locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/emilaemil/pkkp-chatbot.git
   cd ML
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Flask Application

1. **Provide Model and Dataset**

   Place the `chatbot_model.h5` and `dataset.json` files in your project directory.

2. **Run the Flask application**:

   ```bash
   python app.py
   ```

3. **Access the Application**:

   Open your browser and go to `http://127.0.0.1:5000/` to see the Flask app running.

## API Testing

You can test the chatbot API by sending a POST request to the /chatbot endpoint with the following JSON format:

```bash
{
  "message": "Your message"
}
```

The API response will contain the chatbot's response in JSON format:

```bash
{
  "responses": "Chatbot's response"
}
```

## Author

- Emila
