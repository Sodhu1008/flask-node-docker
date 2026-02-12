from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    # name = request.form.get('name')
    # email = request.form.get('email')

    return f"""
    <h2>Data Received Successfully!</h2>
    <p>Name: {name}</p>
    <p>Email: {email}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
