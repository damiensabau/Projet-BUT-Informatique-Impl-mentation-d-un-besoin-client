from flask import Flask, render_template
from main import *
import base64
from io import BytesIO
from matplotlib.figure import Figure

app = Flask(__name__, static_folder='css', template_folder='html')

@app.route('/a')
def home():
    return render_template('index.html')

@app.route("/")
def hello():
    # Générez la figure sans utiliser pyplot.
    fig = Figure()
    ax = fig.subplots()

    graph = main()
    ax.plot(graph)
    # Enregistrez-le dans un tampon temporaire.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Intégrez le résultat dans la sortie html.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
