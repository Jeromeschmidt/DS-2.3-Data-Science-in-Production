# from flask import Flask, request, render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def my_form():
#     return render_template('my-form.html')
#
# @app.route('/', methods=['POST'])
# def my_form_post():
#     num = int(request.form['text'])
#     new_num = num+2
#     return new_num

# from flask import Flask, request
# from datetime import datetime
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello():
#     num = int(request.args['num']) + 2
#     return """
#          <html><body>
#              <h1>{0}</h1>
#          </body></html>
#          """.format(
#              str(num))
#
# # Launch the FlaskPy dev server
# app.run(host="localhost", debug=True)

# from flask import Flask, request, jsonify
# app = Flask(__name__)
#
#
# def summation(a, b):
#     return a + b
#
#
# @app.route('/', methods=['GET'])
# def my_route():
#     n = request.args.get('n', type=int)
#     m = request.args.get('m', type=int)
#     r = summation(n, m)
#     print(r)
#     return jsonify({'add': r})
#
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)

# from flask import Flask, render_template, request
# from wtforms import Form, FloatField, validators
# import math
#
# app = Flask(__name__)
#
# # Model
# class InputForm(Form):
#     r = FloatField(validators=[validators.InputRequired()])
#
# def compute(r):
#     return math.sin(r)
# # View
# @app.route('/hw1', methods=['GET', 'POST'])
# def index():
#     form = InputForm(request.form)
#     if request.method == 'POST' and form.validate():
#         r = form.r.data
#         s = compute(r)
#         return render_template("view_output.html", form=form, s=s)
#     else:
#         return render_template("view_input.html", form=form)
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask_restplus import Api, Resource, fields
from flask import Flask, jsonify, request, make_response, abort, render_template, redirect, url_for

app = Flask(__name__)
api = Api(app, version='1.0', title='MuseFind Tagging API', description='Automated Tagging By NLP')
ns = api.namespace('MuseFind_api', description='Methods')
single_parser = api.parser()
single_parser.add_argument('n', type=int, required=True, help= 'first number')
single_parser.add_argument('m', type=int, required=True, help= 'second number')


def summation(a, b):
    return a+b


@ns.route('/addition')
class Addition(Resource):
    """Uploads your data to the recommender system"""
    @api.doc(parser=single_parser, description='Enter Two Integers')
    def get(self):
        """Uploads a new transaction to Rex (Click to see more)"""
        args = single_parser.parse_args()
        n1 = args.n
        m1 = args.m
        r = summation(n1, m1)
        print(r)
        return {'add': r}


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=3000)
    app.run(debug=True)
