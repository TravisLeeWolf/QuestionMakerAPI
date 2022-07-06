from flask import Flask, render_template,request

app = Flask(__name__)

data = [{'pk':1,'id':1,'text':'hello, how are you?','translation_text':'gonnichiwa', 'tags':['easy','sports'],'grads':'JuniorHigh2','chapter':3,'pic_url':'https://github.com/TravisLeeWolf/WipeoutEnglish/raw/main/wipeout_game.png'},
{'pk':2,'id':2,'text':'how old are you?','translation_text':'??', 'tags':['easy','angry'],'grads':'JuniorHigh2','chapter':3,'pic_url':'https://github.com/TravisLeeWolf/WipeoutEnglish/raw/main/wipeout_game.png'}]
grade= ['Junior High Grade 1','Junior High Grade 2','Junior High Grade 3','Elementary Grade 1','Elementary Grade 2','Elementary Grade 3','Elementary Grade 4','Elementary Grade 5','Elementary Grade 6']
@app.route("/")
def index():
    return render_template('index.html', data=data, grade=grade)


@app.route("/view")
def view():
    return render_template('template/questionViewer.html')


@app.route("/make")
def make():
    return render_template('template/questionMaker.html')

@app.route("/helper")
def helper():
    return render_template('template/apiHelper')


if __name__ == "__main__":
    app.run()