# Flask Microservices Call ChatGPT API

This repository contains a Flask microservice that interacts with the ChatGPT API provided by OpenAI. The microservice allows you to send text prompts to the ChatGPT model and receive AI-generated responses.

## Getting Started

To get started with this microservice, follow the steps below:

### Prerequisites

1. Python 3.6 or higher installed on your system.
2. An OpenAI API key with access to the ChatGPT API. If you don't have an API key, visit the OpenAI website to create one.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Abelisme/extension-for-chatgpt.git
   ```

2. Navigate to the cloned directory:

   ```bash
   cd extension-for-chatgpt.git
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Open the `.env` file and replace `'OPENAI_API_KEY'` with your actual OpenAI API key.

### Starting the Microservice

1. Start the Flask microservice:

   ```bash
   python app.py
   ```

2. The microservice will now be running at `http://localhost:5000`.

## Making API Requests

You can make API requests to the microservice by sending a POST request to the `/chat` endpoint. The request payload should include a `prompt` parameter with the text prompt you want to send to the ChatGPT model. The microservice will respond with the generated AI response.

- Here's an example using cURL:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"message": "Where is Tokyo?"}' http://localhost:5000/api/openai/text/
    ```

    The response will be a JSON object containing the AI-generated `response` field.

## Additional Information

- The `app.py` file contains the Flask application code that handles incoming requests and interacts with the ChatGPT API.
- The `config.py` file contains the API key configuration.
- The `utils.py` file contains helper functions for making API requests and handling responses.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Acknowledgments

- This microservice was created using Flask and the OpenAI Python SDK.
- Thank you to the OpenAI team for providing the ChatGPT API.

## Image
![alt text](https://github.com/Abelisme/extension-for-chatgpt/blob/master/readme-images/curl-api-openai-text-200.png?raw=true)