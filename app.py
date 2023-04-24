from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/movie", methods=["POST"])
def movie_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    all_users = list(db.moviess.find({}, {'_id': False}))
    return jsonify({'msg':'GET 연결 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=8080, debug=True)