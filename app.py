from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks.append({"task": task, "completed": False})
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    tasks.pop(index)
    return redirect("/")

@app.route("/complete/<int:index>")
def complete(index):
    tasks[index]["completed"] = True
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
