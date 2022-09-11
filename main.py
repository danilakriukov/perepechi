from flask import Flask, render_template, request, redirect, url_for
import time
from datetime import datetime
import pickle


class Member:
	def __init__(self, name):
		self.name = name
	def access(self):
		result = True
		return result


app = Flask(__name__)


@app.route('/')
def begin():
	return redirect(url_for('main'))


@app.route('/main')
def main():
	'''class Member:
		def access (self, name):
			result = True
			return result'''
	member = Member.access('danila')
	return render_template("main.html",result=member)


if __name__ == "__main__":
	app.run()
