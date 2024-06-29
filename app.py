from flask import Flask, render_template, request, redirect
from helper import preprocessing,vectorizer,get_prediction

app = Flask(__name__)
print('flask server started')

data = dict()
reviews = []
positive = 0
negative = 0

@app.route("/")
def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative
    print('===========open home page============')
    return render_template('index.html', data=data)

@app.route("/", methods = ['post'])
def my_post():
    text = request.form['text']
    print(f'Text : {text}')

    preprocessed_txt = preprocessing(text)
    print(f'preprocessed Text : {preprocessed_txt}')

    vectorized_txt = vectorizer(preprocessed_txt)
    print(f'vectorized Text : {vectorized_txt}')

    prediction = get_prediction(vectorized_txt)
    print(f'prediction Text : {prediction}')

    if prediction == 'negative':
        global negative
        negative += 1
    else:
        global positive
        positive += 1

    reviews.insert(0, text)
    return redirect(request.url)


if __name__ == "__main__":
    app.run()
