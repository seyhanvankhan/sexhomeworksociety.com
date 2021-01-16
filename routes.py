############ Seyhan Van Khan & Alizeh Khan
############ Sex Homework Society - sexhomeworksociety.com
############ put description here
############ January 2021

################################ IMPORT MODULES ################################


from socket import gethostbyname_ex, gethostname

from flask import Flask, redirect, render_template, request, send_from_directory, url_for
from sass import compile as sass_compile


################################### INIT APP ###################################


app = Flask(__name__, static_url_path='/assets', static_folder='assets')
sass_compile(dirname=('assets/stylesheets/scss', 'assets/stylesheets/css'), output_style='compressed')


##################################### INDEX ####################################


@app.route('/')
def index():
	return render_template("index.html")


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
