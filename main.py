import numpy as np
import tensorflow as tf
from flask import Flask,jsonify,render_template,request
import json
from mnist import model
x = tf.placeholder('float', [None, 784])
sess = tf.Session()

with tf.variable_scope('regression'):
    y1, variables = model.regression(x)
saver = tf.train.Saver(variables)
saver.restore(sess,"mnist/data/regression.ckpt")

with tf.variable_scope("convolutional"):
    keep_prob = tf.placeholder('float')
    y2, variables = model.convolutional(x,keep_prob)
saver = tf.train.Saver(variables)
saver.restore(sess, "mnist/data/convolutional.ckpt")

def regression(input):
    return sess.run(y1, feed_dict={x:input}).flatten().tolist()
def convolutional(input):
    return sess.run(y2, feed_dict={x:input,keep_prob:1.0}).flatten().tolist()


app = Flask(__name__)
@app.route('/api/mnist', methods=['post'])
def mnist():
    input = ((255 - np.array(request.json, dtype=np.uint8)) / 255.0).reshape(1,784)
    output1 = regression(input)
    output2 =  convolutional(input)

    output = {}
    output["output1"] = output1
    output["output2"] = output2
    res = []
    res.append(output)
    a = {}
    a['site'] = res
    mydata = json.dumps(a, ensure_ascii=False).encode("utf8")
    return mydata
@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run(port=9000)