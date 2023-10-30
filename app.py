# # -*- coding: UTF-8 -*-
# from celery import chain,signature
# from pod import pod1_add,pod2_mul

# print("Start celery")

# def pod1_start(x,y):
#     pod1_add.s(x,y)
    
# def pod2_start(a,b):
#     pod2_mul.s(a,b)
    
# def chain_pod1_to_pod2():
#     task_chain = chain(
#         pod1_add.s(1,2),
#         pod2_mul.s(3)
#     )
#     result = task_chain.delay()
#     print(result.get())
    
# def chain_pod2_to_pod1():
#     task_chain = chain(
#         pod2_mul.s(1,2),
#         pod1_add.s(3)
#     )
#     result = task_chain.delay()
#     print(result.get())    

# if __name__ == "__main__":
#     print("開始Pod1->Pod2")
#     chain_pod1_to_pod2()