import os
import datetime
import time

from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

# if os.getenv("TESTING") == "true":
#     print("Running in test mode")
#     mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
# else:
#     mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
#                          user=os.getenv("MYSQL_USER"),
#                          password=os.getenv("MYSQL_PASSWORD"),
#                          host=os.getenv("MYSQL_HOST"),
#                          port=3306
#                          )
#
# print(mydb)
#

@app.route('/')
def index():
    return render_template('index.html', title="Ekam Ghai", url=os.getenv("URL"))


@app.route('/about')
def about():
    return render_template('about.html', title="About", url=os.getenv("URL"))


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"))


@app.route('/education')
def education():
    return render_template('education.html', title="Education", url=os.getenv("URL"))


@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects", url=os.getenv("URL"))


# @app.route('/timeline')
# def timeline():
#     data = get_time_line_post()
#     return render_template('timeline.html', title="Timeline", url=os.getenv("URL"), data=data["timeline_posts"])

#
# # Model
# class TimelinePost(Model):
#     name = CharField()
#     email = CharField()
#     content = TextField()
#     created_at = DateTimeField(default=datetime.datetime.now)
#
#     class Meta:
#         database = mydb
#
#
# mydb.connect()
# mydb.create_tables([TimelinePost])
#
# # api
#
# @app.route('/api/timeline_post', methods=['POST'])
# def post_time_line_post():
#     name = request.form.get('name', "")
#     email = request.form.get('email', "")
#     content = request.form.get('content', "")
#     timeline_post = TimelinePost.create(name=name, email=email, content=content)
#     return model_to_dict(timeline_post)
#
#
# @app.route('/api/timeline_post', methods=['GET'])
# def get_time_line_post():
#     return {
#         'timeline_posts': [
#             model_to_dict(p)
#             for p in
#             TimelinePost.select().order_by(TimelinePost.created_at)
#         ]
#     }
