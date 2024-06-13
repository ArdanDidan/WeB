from flask import Flask, render_template
import random
import os
import pass_generator 

app = Flask(__name__)

# Home/1st page
@app.route("/")
def pertama():
    # <a> anchor tag with its attribute
    return """
    <h1>Hello, World!</h1><br>
    <p>Nice to see you</p>
    <p>Please check:</p>
    <a href='/random_fact'>View a random fact!</a><br>
    <a href='/modern_fact'>View a modern fact!</a><br>
    <a href='/flip_coin'>Lempar koin!</a><br>
    <a href='/random_image'>Lihat gambar acak!</a><br>
    <a href='/generate_password'>Generate a password!</a>
    """
    
# 2nd page
@app.route("/random_fact")
def kedua():
    txt_name = random.choice(os.listdir("fact_list"))
    # formatted string
    with open(f'fact_list/{txt_name}', 'r') as f:
        document = f.read()
    return f'{document}'
# 2nd page
@app.route('/modern_fact')
def index():
    return render_template('dasar.html')#folder templates


# Halaman Lempar Koin
@app.route('/flip_coin')
def flip_coin():
    result = random.choice(["It's Heads", "It's Tails"])
    return f'<h1>{result}</h1><br><a href="/">Kembali ke beranda</a>'

# Halaman Gambar Acak
@app.route('/random_image')
def random_image():
    img_name = random.choice(os.listdir("static/img"))
    return f'<img src="/static/img/{img_name}" alt="Gambar Acak"><br><a href="/">Kembali ke beranda</a>'

# Halaman Generator Kata Sandi
@app.route('/generate_password')
def generate_password():
    password = pass_generator.gen_pass(12)  # Generate a 12-character password
    return f'<h1>Password: {password}</h1><br><a href="/">Kembali ke beranda</a>'

if __name__ == '__main__':
    app.run(debug=True)