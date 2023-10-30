from flask import Flask,render_template
from celery import chain,signature
from pod import pod1_add,pod2_mul,add_callback
import requests


app = Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html')


@app.route("/pod_1")
def pod_1():
   return str(pod1_start(1,2))

@app.route("/pod_2")
def pod_2():
   return str(pod2_start(1,2))

@app.route("/pod_1_to_pod_2")
def pod_1_to_pod_2():
   return str(chain_pod1_to_pod2())

@app.route("/pod_2_to_pod_1")
def pod_2_to_pod_1():
   return str(chain_pod2_to_pod1())

# --------------------------------
def pod1_start(x,y):
    # res = pod1_add.delay(x,y)
    res = pod1_add.apply_async((x,y),link = add_callback.s())
    # callback(res.get())
    return res.get()
    
def pod2_start(a,b):
    res = pod2_mul.delay(a,b)
    return res.get()
    
def chain_pod1_to_pod2():
    task_chain = chain(
        pod1_add.s(1,2),
        pod2_mul.s(3),
        add_callback.s()
    )
    result = task_chain.delay()
    print(result.get())
    return result.get()
    
def chain_pod2_to_pod1():
    task_chain = chain(
        pod2_mul.s(1,2),
        pod1_add.s(3)
    )
    result = task_chain.delay()
    print(result.get())    
    return result.get()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port = 5000)