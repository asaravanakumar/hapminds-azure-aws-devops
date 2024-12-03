from flask import Flask, jsonify, request 
  
app = Flask(__name__) 
  
  
@app.route('/', methods=['GET']) 
def helloworld(): 
    badCode = True
    if badCode:
        print("read bad code but executes")
    else:
        pass
    if badCode:
        print("do nothing")
    else:
        pass
    if(request.method == 'GET'): 

        data = {"data": "Hello Azure"} 
        return jsonify(data) 
  
if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=80) 
