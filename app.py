from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    submitted_data = None
    if request.method == 'POST':
        # Get data from form
        name = request.form.get('name')
        dob = request.form.get('dob')
        email = request.form.get('email')  # example extra field

        submitted_data = {
            'Name': name,
            'Date of Birth': dob,
            'Email': email
        }

    return render_template('form.html', data=submitted_data)

if __name__ == '__main__':
    # Run on 0.0.0.0 to listen on all IPs, port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
