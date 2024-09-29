from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/screening/<int:number>', methods=['GET'])
def screening(number):
    results = []

    if number % 3 == 0 and number % 5 == 0:
        results.append("KanzWay")
    elif number % 3 == 0:
        results.append("Kanz")
    elif number % 5 == 0:
        results.append("Way")
    else:
        results.append(str(number))

    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
