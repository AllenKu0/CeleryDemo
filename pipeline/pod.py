# -*- coding: UTF-8 -*-
from celery import Celery
import time
import requests

celery_app = Celery(
    __name__,
    backend = 'redis://localhost:6379/0',
    broker = 'redis://localhost:6379/1',
)

# queue = "add"
@celery_app.task(queue = "add")
def pod1_add(a,b):
    print("-------------test-pod-1 start------------")
    print(a+b)
    # time.sleep(5)
    print("-------------test-pod-1 end--------------")
    return a + b

@celery_app.task(queue = "mul")
def pod2_mul(x,y):
    print("-------------test-pod-2 start------------")
    print(x*y)
    # time.sleep(5)
    print("-------------test-pod-2 end--------------")
    return x * y

@celery_app.task(queue = "add")
def add_callback(request):
    print("---------callback-----------")
    response = requests.post("https://5199e5e9-9315-4f19-9965-0d726e73ab76.mock.pstmn.io/callback")
    print(request)
    print(response.status_code)
    print(response.json())
    return request
    
# @celery_app.task(queue = "mul")
# def mul_callback(request):
#     print("---------callback-----------")
#     response = requests.post("https://5199e5e9-9315-4f19-9965-0d726e73ab76.mock.pstmn.io/callback")
#     print(request)
#     print(response.status_code)
#     print(response.json())