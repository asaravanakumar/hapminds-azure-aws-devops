from flask import Flask, jsonify, request 
  
app = Flask(__name__) 
  
  
@app.route('/', methods=['GET']) 
def helloworld(): 
    if(request.method == 'GET'): 
        data = {"data": "Greetings Everyone"} 
        return jsonify(data) 
  
  
if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=80) 
