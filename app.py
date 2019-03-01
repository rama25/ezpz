from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/id")
def main():
    if 'id' in request.args:
        myid = request.args.get('id')
        print("Received id = ", myid)
        #return render_template(myid)
        #sleep
        return "airplace"

#rendering the HTML page which has the button
@app.route('/json')
def json():
    return render_template('json.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print("Hello")
    return "nothing"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=10000)