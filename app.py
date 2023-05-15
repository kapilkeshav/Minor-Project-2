from flask import Flask, render_template, request, redirect, url_for
import mes_send as ms
import mes_rec as mr

app = Flask(__name__)

messages = []

@app.route('/')
def home():
    return render_template('home.html', messages=messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    sender = request.form['sender']
    message = request.form['message']
    ms.mes_send(message)
    fin_message = mr.mes_rec()
    messages.append({'sender': sender, 'message': fin_message})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)