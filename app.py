from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

# Configure DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('HelloWorldMessages')

# Main Route
@app.route('/')
def index():
    return '''
        <form action="/submit" method="POST">
            Name: <input type="text" name="name"><br>
            Message: <input type="text" name="message"><br>
            <input type="submit">
        </form>
    '''

# Submit Message Route
@app.route('/submit', methods=['POST'])
def submit_message():
    name = request.form['name']
    message = request.form['message']

    # Insert into DynamoDB
    table.put_item(Item={'name': name, 'message': message})

    return jsonify({'status': 'Message saved!'})

# Run Flask App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
