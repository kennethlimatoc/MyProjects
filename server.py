from flask import Flask, render_template, request, redirect
from car import model  

app = Flask(__name__)

@app.route('/')
def car_form():
    all_models = model.display_cars() 
    return render_template('car.html', all_models=all_models)

@app.route('/solid', methods=['POST']) 
def info_cars():
    data = {
        "Make": request.form['Make'],
        "Model": request.form['Model'],
        "Year": int(request.form['Year']),
        "Description": request.form['Description']
    }
    model.add_cars(data)
    return redirect('/')

#for delete
@app.route('/delete/<id>')
def delete_cars(id):
    data = {
        "id": id
    }
    model.delete_info(data)
    return redirect('/')



#for update 
@app.route('/solid2', methods=['POST']) 
def UpdateInfo_cars():
    data = {
        "id": request.form['id'],
        "Make": request.form['Make'],
        "Model": request.form['Model'],
        "Year": int(request.form['Year']),
        "Description": request.form['Description']
    }
    model.update_info(data)
    return redirect('/')


@app.route('/update/<id>')
def update_story(id):
    data = {
        "id": id
    }
    all_models = model.retrieve_info(data)
    return render_template('car_update.html', all_models=all_models)





if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)

