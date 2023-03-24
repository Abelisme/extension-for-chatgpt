from flask import Flask, jsonify, request
# from flask_cors import CORS
import openai
import os

app = Flask(__name__)
# CORS(app)

with open("key.txt") as f:
    openai.api_key = f.read().strip("\n")
# openai.api_key = open("key.txt", "r").read().strip("\n")

@app.route('/api/data/', methods=['POST'])
def get_data():
    data = request.get_json()
    input = data['message']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)