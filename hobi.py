from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hobi/<string:nama>')
def getnama(nama):
    nama = "Nama saya {}" .format(nama)
    hobi = ['bermain game','mendengarkan music']
    return render_template ('hobi.html', hobi = hobi, nama = nama)

if __name__ == '__main__':
        app.run(debug=True)