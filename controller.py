from flask import Flask,render_template
app=Flask(__name__)
app.secret_key="wdjnwu"

#displays login form
@app.route("/")
def home():
    return render_template("login.html")

#registration form
@app.route("/register")
def register():
    return render_template("register_form.html")

# a form to display all bucket lists
@app.route("/bucketlist")
def bucketlist():
    return render_template("bucket_lists.html")

# form to display specific bucket list
@app.route("/single")
def single():

    return render_template("single_bucket.html")
if __name__ == "__main__":
   app.run(debug=True)