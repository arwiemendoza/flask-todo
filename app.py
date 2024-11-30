from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

todos = []
completed = []

@app.route("/", methods=["GET", "POST"])
def home():
  if request.method == "POST":
    todos.append(request.form.get("activity"))
    print(todos)
  return render_template("form.html", todos=todos)

@app.route("/delete-all", methods=["POST"])
def delete_all():
  global todos
  todos = []
  return redirect(url_for("home"))

@app.route("/complete/<int:index>", methods=["POST"])
def complete(index):
  global todos, completed
  if 0 <= index - 1 < len(todos):
    completed.append(index - 1)
    todos.pop(index - 1)
    print(completed)
  return redirect(url_for("home"))
