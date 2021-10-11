from flask import *
import requests

def create_app():
  app=Flask(__name__)

  @app.route('/')
  def index():
    return render_template('index.html')
  @app.route('/',methods=["POST"])
  def search():
    form=request.form
    r=requests.get('https://goweather.herokuapp.com/weather/{}'.format(form.get('q')))
    try:
      weather=r.json()
      return render_template('search.html',temp=weather['temperature'],wind=weather['wind'])
    except Exception as e:
      print(e)
      return render_template('search.html',not_found_error='CITY NOT FOUND')

  return app