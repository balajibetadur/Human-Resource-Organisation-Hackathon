from flask import Flask, render_template, request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
import os
from werkzeug import secure_filename
from datetime import datetime
import math


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.secret_key ='super_secrete_key'
app.config['UPLOAD_FOLDER']=params['upload_location']

# app.config.update(
#     MAIL_SERVER = 'smtp.gmail.com',
#     MAIL_PORT = '465',
#     MAIL_USE_SSL = True,
#     MAIL_USERNAME = params['gmail-user'],
#     MAIL_PASSWORD=  params['gmail-password']
# )
# mail = Mail(app)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['mysql://root:@localhost/codingthunder']

db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class Register(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=True)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    skills = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    
    
class Employer(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(80), nullable=True)
    password = db.Column(db.String(80), nullable=False)
   
    mobile = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    
    
    


class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(12), nullable=True)


@app.route("/")
def home():
    posts=Posts.query.filter_by().all()
    last=math.ceil(len(posts)/int(params['no_of_posts']))
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page=1
    page=int(page)
    posts=posts[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+int(params['no_of_posts'])]
    if(page==1):
        prev="#"
        next = "/?page="+ str(page+1)
    elif(page==last):
        next="#"
        prev = "/?page="+ str(page-1)
    else:
        
        next = "/?page="+ str(page+1)
        prev = "/?page="+ str(page-1)

   


    return render_template('index.html', params=params, posts=posts,prev=prev,next=next)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)

@app.route("/about")
def about():
    return render_template('about.html', params=params)

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route("/delete/<string:sno>" , methods=['GET','POST'])
def delete(sno):
    
    if ('user' in session and session['user']==params['admin_user']):
        post=Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()

    
    return redirect('/dashboard')

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
        # mail.send_message('New message from ' + name,
        #                   sender=email,
        #                   recipients = [params['gmail-user']],
        #                   body = message + "\n" + phone
        #                   )
    return render_template('contact.html', params=params)


@app.route("/register",methods=['GET','POST'])
def register():
    if(request.method=='POST'):
        firstname = request.form.get('firstname')
        last= request.form.get('lastname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        
        skills = request.form.get('skills')
        password=request.form.get('password')
        entry = Register(firstname=firstname,lastname=last,email=email,phone = phone,skills=skills,password= password )
        db.session.add(entry)
        db.session.commit()
        # mail.send_message('New message from ' + name,
        #                   sender=email,
        #                   recipients = [params['gmail-user']],
        #                   body = message + "\n" + phone
        #                   )
        verify= Register.query.all()
        return redirect('/dashboard')
    return render_template('register.html', params=params)

@app.route("/comp_reg",methods=['GET','POST'])
def comp_reg():
    if(request.method=='POST'):
        company = request.form.get('company')
        
        email = request.form.get('email')
        phone = request.form.get('phone')
        
       
        password=request.form.get('password')
        entry = Employer(company=company,password= password,mobile = phone,email=email)
        db.session.add(entry)
        db.session.commit()
        # mail.send_message('New message from ' + name,
        #                   sender=email,
        #                   recipients = [params['gmail-user']],
        #                   body = message + "\n" + phone
        #                   )
        verify= Register.query.all()
        return redirect('/dashboard')
    return render_template('comp_reg.html', params=params)


@app.route("/dashboard",methods=['GET','POST'])
def dashboard():
    if ('user' in session and session['user']==params['admin_user']):
        posts = Posts.query.all()
        
        return render_template('dashboard.html',params=params,posts=posts)
    if (request.method=='POST'):
        username = request.form.get('uname')
        
        password = request.form.get('pass')
        verify= Register.query.filter_by(firstname=username).first()
        verify_comp= Employer.query.filter_by(company=username).first()
        if(verify != None):
            if(username==verify.firstname and password==verify.password):
                session['user']=username
                posts = Posts.query.all()
                return render_template('dashboard.html',params=params,posts=posts)
        elif(verify_comp != None):
            if(username==verify_comp.company and password==verify_comp.password):
                flag=1
                session['user']=username
                posts = Posts.query.all()
                return render_template('dashboard.html',params=params,posts=posts,verify_comp=verify_comp,flag=flag)
        else:

            return redirect('/dashboard')

    else:

        return render_template('login.html', params=params)


@app.route("/uploader",methods=['GET','POST'])
def uploader():
     if (request.method=='POST'):
        username=session['user']
        verify_comp= Employer.query.filter_by(company=username).first()

        if ('user' in session and session['user']==verify_comp.company):
        
                f=request.files['file1']
                f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
                return "upload succesfully"



@app.route("/edit/<string:sno>", methods = ['GET', 'POST'])
def edit(sno):
    
    if ('user' in session and session['user']==params['admin_user']):
        
        if(request.method=='POST'):
            box_title=request.form.get('title')
            tline=request.form.get('tagline')
            slug=request.form.get('slug')
            content=request.form.get('content')
            img_file=request.form.get('img_file')
            date= datetime.now()

            
            
            post=Posts.query.filter_by(sno=sno).first()
            post.title=box_title
            post.slug=slug
            post.content=content
            post.tagline=tline
            post.img_file=img_file
            post.date=date
            db.session.commit()
            return redirect('/edit/' +sno)
        
        post=Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html',params=params,post=post)


@app.route("/newpost/<string:sno>", methods = ['GET', 'POST'])
def newpost(sno):
    
    if ('user' in session and session['user']==params['admin_user']):
        
        if(request.method=='POST'):
            box_title=request.form.get('title')
            tline=request.form.get('tagline')
            slug=request.form.get('slug')
            content=request.form.get('content')
            img_file=request.form.get('img_file')
            date= datetime.now()

            
            
            post = Posts(title=box_title,slug = slug ,content=content, tagline=tline ,img_file=img_file,  date= date )
            db.session.add(post)
            db.session.commit()
            
            return redirect('/dashboard')
            
        return render_template('newpost.html',params=params,sno=sno)




app.run(debug=True)
