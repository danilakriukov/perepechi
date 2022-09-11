from flask import Flask, render_template, request, redirect, url_for
import time
from datetime import datetime
import pickle


app = Flask(__name__)


@app.route('/')
def begin():
	return redirect(url_for('main'))


@app.route('/main')
def main():
	return render_template("main.html")


if __name__ == "__main__":
	app.run()
