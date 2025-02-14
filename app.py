from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='.')

@app.route('/')
def love_letter():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
