from flask import Flask, request, redirect, url_for, render_template
from jinja2 import Template, Environment, FileSystemLoader


environment="development"

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

app = Flask(__name__, static_url_path='/static')


def count_vowel(stringv):
    lista = map(stringv.lower().count, "aeiou")
    return sum(lista)

def count_consonants(stringv):
    lista = map(stringv.lower().count, "bcdfghjklmnñpqrstvwxyz")
    return sum(lista)

def up_down(stringv):
    updstring = ""
    position = 1
    for letra in stringv:
        if position % 2 == 0:
            updstring = updstring + letra.lower()
        else:
            updstring = updstring + letra.upper()
        position = position + 1
    return updstring

def naive_vowels(stringv):
    mystr = stringv
    mystr = mystr.replace("a", "@")
    mystr = mystr.replace("e", "3")
    mystr = mystr.replace("i", "!")
    mystr = mystr.replace("o", "0")
    mystr = mystr.replace("u", ")")
    return mystr




@app.route('/', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        mystring = request.form['codigo']

        #operaciones
        palabra = (mystring)
        reverse = (mystring[::-1])
        largo = (len(mystring))
        upper = (mystring.upper())
        lower = (mystring.lower())
        vowel = count_vowel(mystring)
        consonants = count_consonants(mystring)
        updown = up_down(mystring)
        naive = naive_vowels(mystring)
        print('reverse len upper lower',reverse,largo,upper,lower)
        #template = env.get_template('form.html')
        return render_template("form.html",
            palabra=palabra,
            reverse=reverse,
            largo=largo,
            upper=upper,
            lower=lower,
            vowel = vowel,
            consonants = consonants, 
            updown = updown,
            naive= naive)
        #return template.render()
        #return redirect(url_for('index'))
    
    if request.method == 'GET': 
        print('GET')
        template = env.get_template('form.html')
        return template.render()
    else:
        print('else')
        template = env.get_template('form.html')
        return template.render()



if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    print("Local change")
    app.run(host="0.0.0.0")


