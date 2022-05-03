from flask import Flask, render_template, request
import nltk
import os
import re
from wordlesolver import wordle_solver

app = Flask(__name__)
nltk.download('words')


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/data/', methods = ['POST'])
def data():
    form_data = request.form
    discovered_letter_order = [form_data.get('dl1'), form_data.get('dl2'), 
        form_data.get('dl3'), form_data.get('dl4'), form_data.get('dl5')]
    app.logger.info(form_data)
    possible_words = wordle_solver(
        discovered_letter_order = discovered_letter_order,
        bad_letters = re.findall('\w', form_data.get('bad_letters')),
        bad_letter_order_one = re.findall('\w', form_data.get('glbo1')),
        bad_letter_order_two = re.findall('\w', form_data.get('glbo2')),
        bad_letter_order_three = re.findall('\w', form_data.get('glbo3')),
        bad_letter_order_four = re.findall('\w', form_data.get('glbo4')),
        bad_letter_order_five = re.findall('\w', form_data.get('glbo5'))
    )
    return render_template('data.html', possible_words = possible_words)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)