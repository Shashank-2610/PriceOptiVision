# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import os
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

@app.route('/', methods=['POST'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def h1():
    try:
         if request.method == 'POST' or request.method == 'GET':
             f = [x for x in request.form.values()]
             print("Input Feature : ", f)
             #f = request.files['image']
             print("F : ",f)
             basepath = os.path.dirname(__file__)
             filepath = os.path.join(basepath, 'uploads')
             #f.save(filepath)
             print("FilePath : ", filepath)
             #result = model_predict(filepath)
             #return render_template('index.html',prediction_text=result)
         return None
    except:
        return render_template('index.html',prediction_text="Cannot Detect Number Plate!!!")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
