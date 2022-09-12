from flask import Flask, render_template, request, redirect, url_for
import random
import time
from datetime import datetime
import pickle

# Dummy data
names = [
    'member1',
    'member2',
    'member3',
    'member4',
    'member5',
    'member6',
    'member7',
    'member8',
    'member9',
    'member10',
]

instances = []


class Member:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    # def access(self):
    # 	result = True
    # 	return result


# Collect all existing names from class
for item in names:
    member = Member(item)
    instances.append(member.name)


app = Flask(__name__)


@app.route('/')
def begin():
    return redirect(url_for('main'))


@app.route('/main')
def main():
    return render_template("main.html", result=random.sample(instances, 8))


if __name__ == "__main__":
    app.run()
