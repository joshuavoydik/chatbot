from flask import Flask, render_template, request, jsonify
import openai

openai.api_key = "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"

app = Flask(__name__)

def get_response(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message['content']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)


