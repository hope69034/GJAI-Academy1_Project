from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return '''
<h1> eeeee Hello World!</h1>
<hr>
<p>디 </p>
'''
if __name__ == '__main__':
    app.run(debug=True)