from flask import Flask, render_template, request, current_app
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('01.index.html')

@app.route('/menu', methods = ['GET', 'POST']) #겟 포스트   실행취소링크
def menu():
    try:
        if request.method == 'GET': #취소누르면 새로고침
            languages = [
            {'disp':'미세각질', 'val':'en'},
            {'disp':'피지과다', 'val':'jp'},
            {'disp':'모낭사이홍반', 'val':'cn'},
            {'disp':'모낭홍반농포', 'val':'fr'},
            {'disp':'비듬', 'val':'es'},
            {'disp':'탈모', 'val':'tm'}
            ]

            return render_template('02.Menu.html' , options=languages) # laguages - 서버에서 클라이언트로 정보 전달 (인터넷창에표시)

        else: #실행눌럿을 떄 결과화면으로 # post - 실행 버튼 부분
            
            #index = request.form['index'] # 유저의 인풋을 서버로 전송
            lang = request.form['lang']
            #lyrics = request.form['lyrics']
            print(lang) # 시엠디창을 보면 서버로 입력값이 전송된 것을 확인할 수 잇다.
            # 사용자가 입력한 파일을 읽어서 업로드
            f_image = request.files['image']
            print(f_image.filename) # 서버(cmd)창으로 유저가 올린 이미지의 파일이름을 받음

            filename = os.path.join(current_app.root_path, 'static/upload/') + f_image.filename
            print(filename)
            f_image.save(filename) #업로드폴더에 파일을 세이브
            #fname = f_image.filename
            #모델실행후 결과를 돌려줌 # 여기 모델 실행 후 결과 코드를 올림
            result = f_image.filename +  ' 탈모 (71.23%)'
            return render_template('03.Menu_res.html' , result=result, fname = f_image.filename)
    except:
        # 이미지 안올리고 실행 누르면 에러 > 처리
            languages = [
            {'disp':'미세각질', 'val':'en'},
            {'disp':'피지과다', 'val':'jp'},
            {'disp':'모낭사이홍반', 'val':'cn'},
            {'disp':'모낭홍반농포', 'val':'fr'},
            {'disp':'비듬', 'val':'es'},
            {'disp':'탈모', 'val':'tm'}
            ]

            return render_template('02.Menu.html' , options=languages) # laguages - 서버에서 클라이언트로 정보 전달 (인터넷창에표시)
 
        
#@app.route('/menu_res')
#def menu_res():
#    return render_template('03.Menu_res.html')

if __name__== '__main__' :
    app.run(debug=True)