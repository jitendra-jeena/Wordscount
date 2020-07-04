#importing necessary modules
from flask import Flask,render_template,request
from bs4 import BeautifulSoup
import requests
import frequency
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    error = None
    success = None
    result = dict()
    if request.method == "POST":

        try:
            url = request.form["url"]
            #get the webpage and store the response in  r
            r = requests.get(url)

        except:

            error = "Unable to get URL. Please make sure it's a valid URL"
            return render_template("index.html", error=error)
        if r:
            #Text Preprocessing
            website_content = BeautifulSoup(r.text, 'html.parser').get_text()
            website_content = website_content.replace("\n"," ")
            result = frequency.calculate_frequency(website_content)
            success=url
    return render_template("index.html",result = result,success=success)

if __name__ == "__main__":
    app.run()