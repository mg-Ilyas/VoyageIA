from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    cards = [
        {
            'image': 'static/joiZnB1QfRkYy6SDKXRR3gVFlUQMBH0gMEWon7m2_lg.png',
            'description': 'Description for Card 1'
        },
        {
            'image': 'static/joiZnB1QfRkYy6SDKXRR3gVFlUQMBH0gMEWon7m2_lg.png',
            'description': 'Description for Card 2'
        },
        {
            'image': 'static/joiZnB1QfRkYy6SDKXRR3gVFlUQMBH0gMEWon7m2_lg.png',
            'description': 'Description for Card 3'
        }
    ]
    return render_template('index.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)
