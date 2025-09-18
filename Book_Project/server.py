from flask import Flask,redirect, render_template, request
from story import stories

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('story.html')

@app.route('/display_text', methods=['POST'])
def save_story():

    data = {
        "title" : request.form['title'],
        "author" : request.form['author'],
        "year" : int(request.form['year']),
        "plot" : request.form['plot']
    }
    
    stories.add_story(data)
    

    
    return render_template("display.html",
                           title=data['title'],
                           author=data['author'],
                           year=data['year'],
                           plot=data['plot'])
    
   




if __name__ == '__main__':
    app.run(debug=True)