from flask import Flask, render_template, request, redirect, url_for
from modules.data import details, topics, learning_log_data

app = Flask(__name__)


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("home.html")


# ---------------- REGISTER ----------------

# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Password Validation
        if password != confirm_password:

            return render_template(
                "register.html",
                error="Password and Confirm Password do not match.",
                name=name,
                email=email,
                username=username
            )

        # Username Already Exists Validation
        for user in details:

            if user["username"] == username:

                return render_template(
                    "register.html",
                    error="Username already exists.",
                    name=name,
                    email=email,
                    username=username
                )

        # Save User
        new_user = {

            "name": name,
            "email": email,
            "username": username,
            "password": password

        }

        details.append(new_user)

        return render_template(
            "login.html",
            success="Registration Successful. Please Login."
        )

    return render_template("register.html")

# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        entered_username = request.form["username"]
        entered_password = request.form["password"]

        for user in details:

            if user["username"] == entered_username:

                if user["password"] == entered_password:

                    return redirect(url_for("command_center"))

                else:

                    return render_template(
                        "login.html",
                        error="Password Incorrect."
                    )

        return render_template(
            "login.html",
            error="Username Incorrect."
        )

    return render_template("login.html")


# ---------------- COMMAND CENTER ----------------

@app.route("/command_center")
def command_center():
    return render_template("command_center.html")


# ---------------- KNOWLEDGE BUILDER ----------------

@app.route("/knowledge_builder", methods=["GET", "POST"])
def knowledge_builder():

    if request.method == "POST":

        topic = {

            "topic_name": request.form["topic_name"],
            "category": request.form["category"],
            "difficulty": request.form["difficulty"],
            "status": request.form["status"]

        }

        topics.append(topic)

        return redirect(url_for("knowledge_vault"))

    return render_template("knowledge_builder.html")


# ---------------- KNOWLEDGE VAULT ----------------

@app.route("/knowledge_vault")
def knowledge_vault():

    return render_template(
        "knowledge_vault.html",
        topics=topics
    )


# ---------------- REVISION HUB ----------------

@app.route("/revision_hub")
def revision_hub():

    pending_topics = []

    for topic in topics:

        if topic["status"] == "Not Started":
            pending_topics.append(topic)

    return render_template(
        "revision_hub.html",
        topics=pending_topics
    )


# ---------------- LEARNING LOG ----------------

@app.route("/learning_log", methods=["GET", "POST"])
def learning_log():

    if request.method == "POST":

        log = {

            "date": request.form["date"],
            "topic": request.form["topic"],
            "hours": request.form["hours"],
            "remarks": request.form["remarks"]

        }

        learning_log_data.append(log)

        return redirect(url_for("learning_log"))

    return render_template(
        "learning_log.html",
        logs=learning_log_data
    )


# ---------------- GROWTH ANALYTICS ----------------

@app.route("/growth_analytics")
def growth_analytics():

    total_topics = len(topics)

    completed_topics = 0

    for topic in topics:

        if topic["status"] == "Completed":
            completed_topics += 1

    pending_topics = total_topics - completed_topics

    total_logs = len(learning_log_data)

    return render_template(
        "growth_analytics.html",
        total_topics=total_topics,
        completed_topics=completed_topics,
        pending_topics=pending_topics,
        total_logs=total_logs
    )


# ---------------- ABOUT ----------------

@app.route("/about")
def about():
    return render_template("about.html")


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():
    return redirect(url_for("home"))


# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)