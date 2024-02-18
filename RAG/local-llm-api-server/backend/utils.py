import logging
from flask import render_template_string

class Utils:

  def templatizeFile(self, filename, **kwargs):
    with open('templates/' + filename) as f:
      filestr = f.read()
    templete_str = render_template_string(filestr, **kwargs)
    return templete_str