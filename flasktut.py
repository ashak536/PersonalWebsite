from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(200))

    def __repr__(self):
        return f"Project('{self.name}')"


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/projects")
def projects():
    all_projects = Project.query.all()
    return render_template("projects.html", projects=all_projects)


@app.route("/projects/add", methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        project = Project(
            name=request.form["name"],
            description=request.form["description"],
            url=request.form["url"],
        )
        db.session.add(project)
        db.session.commit()
        return redirect(url_for("projects"))
    return render_template("add_project.html")


@app.route("/projects/edit/<int:id>", methods=["GET", "POST"])
def edit_project(id):
    project = Project.query.get_or_404(id)
    if request.method == "POST":
        project.name = request.form["name"]
        project.description = request.form["description"]
        project.url = request.form["url"]
        db.session.commit()
        return redirect(url_for("projects"))
    return render_template("edit_project.html", project=project)


@app.route("/projects/delete/<int:id>", methods=["POST"])
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("projects"))


if __name__ == "__main__":
    app.run(debug=True)