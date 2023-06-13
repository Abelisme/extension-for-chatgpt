from flask import Flask, jsonify, request, render_template
# from flask_cors import CORS
import openai
import os
from config import api_key, base_templates_path

app = Flask(__name__, template_folder = base_templates_path)
# app.config['EXPLAIN_TEMPLATE_LOADING'] = True #for test templete folder path will show INFO
# refer:https://stackoverflow.com/questions/23327293/flask-raises-templatenotfound-error-even-though-template-file-exists
# CORS(app)

# with open("key.txt") as f:
#     openai.api_key = f.read().strip("\n")
openai.api_key = api_key

@app.route('/')
def home():
    # app.logger.debug('A value for debugging')
    return render_template('/home/index.html', title='Home Page', userName='quk')

@app.route('/api/openai/text/', methods=['POST'])
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