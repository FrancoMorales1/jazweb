from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name=data["name"]
        email=data["email"]
        phone=data["phone"]
        message=data["message"]
        file = database.write(f'\n{name},{email},{phone},{message}')
        
@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/')
    else:
        return redirect('/')