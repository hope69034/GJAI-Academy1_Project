from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('01.index.html')

@app.route('/menu', methods = ['GET', 'POST']) #겟 포스트   실행취소링크
def menu():
    if request.method == 'GET': #취소누르면 새로고침
        return render_template('02.Menu.html')
    else: #실행눌럿을 떄 결과화면으로
        return render_template('03.Menu_res.html')

@app.route('/menu_res')
def menu_res():
    return render_template('03.Menu_res.html')

if __name__== '__main__' :
    app.run(debug=True)