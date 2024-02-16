from flask import Flask
from flask import request

from backend.utils import Utils
from backend.results import Results

app = Flask(__name__)
utils = Utils()
results = Results()

@app.route('/')
def index():
  return utils.templatizeFile('main.html')

@app.route('/api/search', methods=['POST'])
def search():
  query = request.form['input']
  r = results.returnTop3Matches(query)
  return utils.templatizeFile('search.html', query=query, results=r)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='5500', debug=True)
