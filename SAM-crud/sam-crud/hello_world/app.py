import json
from flask_lambda import FlaskLambda
import boto3
from flask import request

app = FlaskLambda(__name__)
ddb = boto3.resource('dynamodb')
table = ddb.Table('students')


@app.route('/hello')
def hello():
    data = {
        "message": "Hello World"
    }
    return (
        json.dumps(data),
        200,
        {'Content-Type': 'application/json'}
    )

@app.route('/students', methods=['GET', 'POST'])
def add_and_get_student():
    if request.method == 'GET':
        students = table.scan()['Items']
        return (
            json.dumps(students),
            200,
            {'Content-Type': 'application/json'}
        )
    else:
        item = request.get_json()
        table.put_item(Item=item)
        return (
            json.dumps({"message": "student entry created"}),
            200,
            {'Content-Type': 'application/json'}
        )

@app.route("/students/<id>", methods=['GET','PATCH','DELETE'])
def get_patch_delete_students(id):
    key = {'id': id}
    if request.method == 'GET':
        student = table.get_item(Key=key).get('Item')
        if student:
            return (
                json.dumps(student),
                200,
                {'Content-Type': 'application/json'}
            )
        else:
            return (
                json.dumps({"message": "Student nott found"})
            )
    elif request.method == 'PATCH':
        att_update = {key: {'Value': value, 'Action': 'PUT'}
                         for key, value in request.get_json().items()}
        table.update_item(
            Key=key, 
            AttributeUpdates=att_update
        )
        return (
            json.dumps({"message": "student entry updated"}),
            200,
            {'Content-Type': 'application/json'}
        )
    else:
        table.delete_item(Key=key)
        return (
            json.dumps({"message": "student entry deleted"}),
            200,
            {'Content-Type': 'application/json'}
        )