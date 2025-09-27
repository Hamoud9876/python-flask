from flask import Flask, request, make_response

app = Flask(__name__)

#static parameter
@app.route('/')
def first():
    return "hello world"

#path parameters
@app.route('/greeting/<name>')
def hello(name):
    return f"hello {name}"

#path parameter
@app.route("/cal/<int:num1>/<int:num2>")
def cal(num1,num2):
    return f"{num1} + {num2} = {num1+num2}"

#query parameter is just a dict with key value pairs
#get is safe as it will return None if the key does not exists
#indexing the value will throw key error if it does not ecists (args.[f_name])
@app.route("/query")
def query():
    first_name = request.args.get('f_name')
    second_name = request.args.get("s_name")
    return f"your name is {first_name} {second_name}"


#use curl to test
@app.route('/post', methods=['POST'])
def posting():
    return "this is a post method"

#created custom response header and body
@app.route('/custom_response')
def custom():
    response = make_response("hello")
    response.status_code = 202
    response.headers["content-type"] = 'somehting'
    return response





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
