from flask import Flask, render_template, redirect, url_for, send_file
import os
import uuid
from urllib import request

app = Flask(__name__)

@app.get("/<path:path>")
def download (path):
    pdfuuid = str(uuid.uuid4())
    URL = path
    path = "static/" + pdfuuid + ".pdf"
    response = request.urlretrieve(URL, path)
    os.system("pdf2htmlEX " + path + " ./static/" + pdfuuid + ".html")
    os.remove(path)
    return send_file("static/" + pdfuuid + ".html", as_attachment=True)