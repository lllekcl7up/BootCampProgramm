from flask import Flask, render_template
from LoginForm import Lf
from AuthForm import AuthF

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello hello world'


@app.route('/') 
def main():
    return render_template('base.html')

@app.route('/register', methods=['GET','POST'])
def reg():
    form = Lf()
    if form.validate_on_submit():
        if form.password_again.data != form.password.data:
            return render_template('register.html', title='Регистрация', form=form,
                                    message='Пароли не совпадают')
        
        with open('BootCampProgramm/Post,Get,Form/file.txt','a', encoding='utf-8') as file:
            file.write(f'{form.name.data};{form.email.data};{form.password.data}\n')
        return render_template('register.html', message='Регистрация успешна')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/log', methods=['GET','POST'])
def log():
    form = AuthF()
    if form.validate_on_submit():
        with open('BootCampProgramm/Post,Get,Form/file.txt','r', encoding='utf-8') as file:
            data = ' '.join(file.readlines())

        if form.email.data not in data:
            return render_template('login.html', form=form, message='Вы не зарегестрированы')
        else:
            for i in data.split():
                # print(i) #выводит в консоль значения 
                if form.email.data in i:
                    # print(i.split(';')[-1],form.password.data) #выводит в консоль пароли для сравнения
                    if i.split(';')[-1] == form.password.data:
                        return render_template('login.html', message='Вы успешно авторизовались')

    return render_template('login.html', form=form)



if __name__ =='__main__':
    app.run()









