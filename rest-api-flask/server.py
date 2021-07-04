# Import Flask, the Python micro web framework
from flask import Flask, render_template
import connexion

app = connexion.App(__name__, specification_dir="./")

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
