############ Seyhan Van Khan & Alizeh Khan
############ Sex Homework Society - sexhomeworksociety.com
############ put description here
############ January 2021

################################ IMPORT MODULES ################################


from socket import gethostbyname_ex, gethostname

from flask import Flask, redirect, render_template, request, send_from_directory, url_for
from flask_assets import Environment, Bundle


################################### INIT APP ###################################


app = Flask(__name__, static_url_path='/assets', static_folder='assets')
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('stylesheets/scss/*.scss', filters='pyscss', output='stylesheets/css/all.css')
assets.register('scss_all', scss)


##################################### INDEX ####################################


@app.route('/')
def index():
	return render_template("index.html")


##################################### ABOUT ####################################


@app.route('/about')
def about():
	return render_template("about.html")


############################ COURSES - SHS SEASON 1 ############################


@app.route('/courses/sex-homework-society-season-1')
def shs_season1():
	return render_template("courses/shs-season-1.html")


############################ COURSES - SHS SEASON 2 ############################


@app.route('/courses/sex-homework-society-season-2')
def shs_season2():
	return render_template("courses/shs-season-2.html")


############################ COURSES - BOUNDARIES ############################


@app.route('/courses/boundaries')
def boundaries():
	return render_template("courses/boundaries.html")


################################### COACHING ###################################


@app.route('/coaching')
def coaching():
	return render_template("coaching.html")


################################## MEMBERSHIP ##################################


@app.route('/membership')
def membership():
	return render_template("membership.html")


##################################### APPLY ####################################


@app.route('/apply')
def apply():
	return render_template("apply.html")


##################################### TERMS ####################################


@app.route('/terms')
@app.route('/termsconditions')
@app.route('/terms-conditions')
def terms():
	return render_template("terms.html")


##################################### PRIVACY POLICY ####################################


@app.route('/privacy')
@app.route('/privacypolicy')
@app.route('/privacy-policy')
def privacy():
	return render_template("privacy.html")


############################## FAVICONS & SITEMAP ##############################


@app.route('/apple-touch-icon.png')
@app.route('/favicon.ico')
@app.route('/icon-192.png')
@app.route('/icon-512.png')
@app.route('/icon.svg')
@app.route('/manifest.webmanifest')
@app.route('/og-image.png')
def favicons():
	return send_from_directory('assets/images/favicons', request.path[1:])


@app.route('/sitemap.xml')
def sitemap():
	return send_from_directory('assets', 'sitemap.xml')


############################## OTHER ROUTES - 404 ##############################


@app.errorhandler(404)
def not_found(e):
	print(e)
	return """
		<h1> error 404 - url not found </h1>
		<h2> probs cuz you havent told seyhan to add it to routes </h2>
		<img src="https://i.ytimg.com/vi/BnlTjw4f4cE/maxresdefault.jpg">
	"""


##################################### RUN ######################################


if __name__ == "__main__":
	ipAddress = gethostbyname_ex(gethostname())[-1][-1]
	if ipAddress[:3] == "192":
		app.run(debug=True, host=ipAddress)
	else:
		app.run(debug=True)
