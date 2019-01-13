import newsbot
import classifier
import trainer
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/search')
def my_form():
    return render_template('WebPage1.html')

@app.route('/search', methods=['POST'])
def my_form_post():
    text = request.form['text']
    articles = newsbot.getnews(text)
    tag2d = []
    for lst in articles:
        tag2d.append(classifier.classifier(lst))
    helpval = trainer.mlplearn(tag2d)
    
    
