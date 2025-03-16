import requests
import os
import matplotlib.pyplot as plt
import random
# global_lib = plt.scatter(x, y, color='red')
#
#
# def func_2(x: list, y: list):
#     global global_lib
#     dict1 = requests.get('https://olimp.miet.ru/ppo_it/api').json()['message']['data']
#
#
#
# # x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
# # y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86]
# #
# # func_2(x, y)


def func():
    dict1 = requests.get('https://olimp.miet.ru/ppo_it/api').json()['message']['data']
    list_x = []
    list_y = []
    k = -1
    m = 0
    for j in range(len(dict1) - 1):
        list_x.append(dict1[j])
        list_y.append(dict1[j + 1])
    plt.scatter(list_x, list_y, color='red')
    plt.xlabel('X-ось')
    plt.ylabel('Y-ось')
    n = ''.join(random.choices('1234567890', k=5)) + 'jpg'
    plt.savefig('templates/' + n)
    return n


