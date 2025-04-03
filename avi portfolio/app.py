from flask import Flask, render_template, request, jsonify, send_file
import os

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Here you can add code to send email or store the message
        return jsonify({'status': 'success', 'message': 'Thank you for your message!'})
    return render_template('contact.html')

@app.route('/download-resume')
def download_resume():
    # Make sure to add your resume.pdf in the static folder
    return send_file('static/resume.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True) 