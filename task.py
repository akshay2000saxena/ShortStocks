import newsbot
import classifier
import trainer
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/search', methods=["GET"])
def my_form():
    return render_template('WebPage1.html')

@app.route('/search', methods=['POST'])
def my_form_post():
    text = request.form['query']
    articles = newsbot.getnews(text)
    tag2d = []
    for lst in articles:
        tag2d.append(classifier.classifier(lst))
    helpval = trainer.mlplearn(tag2d)
    artprint = newsbot.getarticle(text)
    finalarr = []
    
    for i in range(0, len(helpval)):
        if (helpval[i] == 1):
            finalarr.append(artprint[i])

    print(finalarr)

    return "blah", 200
