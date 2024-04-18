from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    response = '<table>'
    response += '<thead>'
    response += '<tr>'
    response += '<td><strong>Key</strong><td>'
    response += '<td><strong>Value</strong></td>'
    response += '</tr>'
    response += '</thead>'
    response += '<tbody>'
    for header in request.headers:
        response += '<tr>'
        response += '<td>' + header[0] + '<td>'
        response += '<td>' + header[1]  + '</td>'
        response += '</tr>'
    response += '</tbody>'
    response += '</table>'
    return response