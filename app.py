from flask import Flask, render_template,request
import ibm_db 

app = Flask(__name__)

conn= ibm_db.connect("DATABASE=bludb; HOSTNAME=125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud; PORT=30426;UID=lcs69469;PWD=lSUZ2kJbkj1wVOoo; SECURITY = ssl;SSLSERVERCERTIFICATE=DigiCertGlobalRootCA.crt", " ", " ")
print(ibm_db.active(conn))
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/login", methords=["GET","POST"])
def login():
    if request.method =="POST":
        uname = request.form['username']
        pword = request.form['password']
        print(uname,pword)
    sql ='select * FROM REGISTER WHERE USERNAME=? AND PASSWORD=?'
    Stmt= Ibm-db.prepare(conn,sql)
    ibm_db.blind_param(stmt,1,uname)
    ibm_db.execute(stmt)
    out = ibm_db.fetch_assoc(stmt)
    print(out)
    if out==False:
        role=Out('ROLE')
        if role == 0:
         return render_template("profile_admin.html")
        elif role == 1:
         return render_template("profile_student.html")
        else:
         return render_template("profile_faculty.html")
    else:
     msg ="Invalid Credentials"
    return render_template("login.html",login_message=msg)
    return render_template("login.html")

    if __name__ == "__main__":
     app.run(debug = True, host="0.0.0.0")