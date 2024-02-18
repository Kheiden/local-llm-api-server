import logging
 
from flask import Flask
from flask import request

from backend.utils import Utils
from backend.results import Results

from logging.config import dictConfig
from flask import has_request_context, request
from flask.logging import default_handler
from dotenv import load_dotenv

load_dotenv()

class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)

formatter = RequestFormatter(
    '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
    '%(levelname)s in %(module)s: %(message)s'
)
default_handler.setFormatter(formatter)
# mail_handler.setFormatter(formatter)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)


file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

utils = Utils()
results = Results()
 
@app.route('/')
def index():
  app.logger.info('Returning main.html')
  return utils.templatizeFile('main.html')

@app.route('/api/search', methods=['POST'])
def search():
  query = request.form['input']
  r = results.returnTop3Matches(query)
  return utils.templatizeFile('search.html', query=query, results=r)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='5500', debug=True)
