# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Welcome to Video Streaming Platform"

# if __name__ == '__main__':
#     app.run(debug=True)

# 
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/upload')
# def upload():
#     return render_template('upload.html')

# if __name__ == '__main__':
#     app.run(debug=True)


# 

# from flask import Flask, render_template, request, send_from_directory
# import os
# import sqlite3
# app = Flask(__name__)

# UPLOAD_FOLDER = "uploads"
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/')
# def home():
#     videos = os.listdir("uploads")
#     return render_template("home.html", videos=videos)
# @app.route('/')
# def home():

#     conn = sqlite3.connect("videos.db")
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM videos")

#     videos = cursor.fetchall()

#     conn.close()

#     return render_template(
#         "home.html",
#         videos=videos
#     )
# @app.route('/upload', methods=['GET', 'POST'])
# def upload():

#     if request.method == 'POST':

#         file = request.files['video']

        # if file:
        #     file.save(
        #         os.path.join(
        #             app.config['UPLOAD_FOLDER'],
        #             file.filename
        #         )
        #     )

        #     return "Video Uploaded Successfully! <br><a href='/'>Go Home</a>"
#         if file:
#             file.save(
#                  os.path.join(
#                       app.config['UPLOAD_FOLDER'],
#                       file.filename
#         )
#     )

#     conn = sqlite3.connect("videos.db")
#     cursor = conn.cursor()

#     cursor.execute(
#         "INSERT INTO videos(filename) VALUES(?)",
#         (file.filename,)
#     )

#     conn.commit()
#     conn.close()

#     return "Video Uploaded Successfully!"


#  return render_template('upload.html')

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(
#         app.config['UPLOAD_FOLDER'],
#         filename
#     )

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, send_from_directory
# import os
# import sqlite3

# app = Flask(__name__)

# UPLOAD_FOLDER = "uploads"
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# @app.route('/')
# def home():

#     conn = sqlite3.connect("videos.db")
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM videos")
#     videos = cursor.fetchall()

#     conn.close()

#     return render_template("home.html", videos=videos)


# @app.route('/upload', methods=['GET', 'POST'])
# def upload():

#     if request.method == 'POST':

#         file = request.files['video']

#         if file and file.filename != "":

#             file.save(
#                 os.path.join(
#                     app.config['UPLOAD_FOLDER'],
#                     file.filename
#                 )
#             )

#             conn = sqlite3.connect("videos.db")
#             cursor = conn.cursor()

#             cursor.execute(
#                 "INSERT INTO videos(filename) VALUES(?)",
#                 (file.filename,)
#             )

#             conn.commit()
#             conn.close()

#             return '''
#             <h2>Video Uploaded Successfully!</h2>
#             <a href="/">Go Home</a>
#             '''

#     return render_template("upload.html")


# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(
#         app.config['UPLOAD_FOLDER'],
#         filename
#     )

# @app.route('/signup', methods=['GET', 'POST'])
# def signup(if request.method == 'POST':

#     username = request.form['username']
#     password = request.form['password']

#     conn = sqlite3.connect("videos.db")
#     cursor = conn.cursor()

#     cursor.execute(
#         "INSERT INTO users(username, password) VALUES(?, ?)",
#         (username, password)
#     )

#     conn.commit()
#     conn.close()

#     return '''
#     <h2>Account Created Successfully!</h2>
#     <a href="/login">Login Here</a>
#     '''

# return render_template("signup.html")):
#     # signup code here


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # login code here



# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, send_from_directory,session,redirect
import os
import sqlite3

app = Flask(__name__)
app.secret_key="mysecretkey"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# @app.route('/')
# def home():
#     if "user" not in session:
#         return redirect('/login')

#     return render_template('home.html')

#     conn = sqlite3.connect("videos.db")
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM videos")
#     videos = cursor.fetchall()

#     conn.close()

#     return render_template("home.html", videos=videos)
@app.route('/')
def home():

    if "user" not in session:
        return redirect('/login')

    conn = sqlite3.connect("videos.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()

    conn.close()

    return render_template("home.html", videos=videos)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if "user" not in session:
        return redirect('/login')
    if request.method == 'POST':

        file = request.files['video']

        if file and file.filename != "":

            file.save(
                os.path.join(
                    app.config['UPLOAD_FOLDER'],
                    file.filename
                )
            )

            conn = sqlite3.connect("videos.db")
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO videos(filename) VALUES(?)",
                (file.filename,)
            )

            conn.commit()
            conn.close()

            return '''
            <h2>Video Uploaded Successfully!</h2>
            <a href="/">Go Home</a>
            '''

    return render_template("upload.html")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename
    )


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("videos.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users(username, password) VALUES(?, ?)",
            (username, password)
        )

        conn.commit()
        conn.close()

        return '''
        <h2>Account Created Successfully!</h2>
        <a href="/login">Login Here</a>
        '''

    return render_template("signup.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("videos.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        if user:
            session["user"]=username

        conn.close()

        if user:
             return redirect('/upload')
        else:
            return "Invalid Username or Password"

    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)