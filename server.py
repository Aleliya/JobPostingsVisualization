from flask import Flask, render_template, json

app = Flask(__name__)

with open('data/clean_categorized_vacancies.json', 'r', encoding='utf-8') as f:
    vacancies_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return vacancies_data

if __name__ == '__main__':
    app.run(debug=True)