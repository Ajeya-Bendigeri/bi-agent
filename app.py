from flask import Flask, render_template, request
from services.database import load_data
from services.query_generator import generate_query
from services.utils import run_query
from services.chart_generator import generate_chart
import os 

app = Flask(__name__)

con = load_data()


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    chart = None
    query = None

    if request.method == "POST":

        question = request.form["question"]

        query = generate_query(question)

        # print("Generated SQL:", query)

        result = run_query(con, query)

        if not isinstance(result, str):
            chart = generate_chart(result)

    return render_template("index.html", result=result, chart=chart, query = query)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
