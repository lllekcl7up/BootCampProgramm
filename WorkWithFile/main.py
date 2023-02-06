from flask import Flask, render_template
from random import randint as rd # (тут переменная рандомит число)

app = Flask(__name__)


@app.route('/index') 
# @app.route('/index ')
def main():
    with open('MyLinux/WorkWithFile/file.txt','r',encoding='utf-8') as file:
        resultData = list()
        for line in file.readlines():
            resultData.append(tuple(line.split('\n')[0].split(' ')))
    # name = rd(0,1)# тут рандомится число
    # return render_template('base.html', name=name)
    return render_template('base.html',data=resultData)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ =='__main__':
    app.run()


# Конспект по лекции "Работа с файлами"
# file = open('MyLinux/WorkWithFile/file.txt', 'r', encoding='utf-8')

# list_1 = list()
# resultData = list()
# for line in file.readlines():
#     resultData.append(tuple(line.split('\n')[0].split(' ')))
#     # print(line.split('\n')[0].split(''))# изменяем список с данными
# # print(file.read()) выводит содержимое файла в консоль

# file.close
# print(resultData)
# '''
# a - режим добавления
# w - режим на запись (очищает файл)
# r - режим считывания 
# '''



