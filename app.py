from flask import Flask, render_template, request, jsonify
app = Flask(__name__)



from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta



@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form["bucket_give"]

    bucket_list = list(db.bucket.find({}, {'_id': False}))
    num = len(bucket_list) + 1

    doc = {
        'num': num,
        'bucket': bucket_receive,
        'done': 0
    }

    db.bucket.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
    return jsonify({'msg': '버킷완료'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    buckets_list = list(db.bucket.find({},{'_id':False}))
    return jsonify({'buckets':buckets_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)