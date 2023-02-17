from flask import Flask, request, jsonify
from flask_cors import CORS
from config import db, SECRET_KEY
from os import path, getcwd, environ
from dotenv import load_dotenv
from models.user import User
from models.projects import Projects
from models.experiences import Experiences
from models.certificates import Certificates
from models.skills import Skills
from models.personalDetails import PersonalDetails
from models.educations import Educations

load_dotenv(path.join(getcwd(),'.env'))

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    app.secret_key = SECRET_KEY

    db.init_app(app)
    print("DB Initialized Successfully")

    with app.app_context():
        @app.route("/signup",methods=['POST'])
        def signup():
            data = request.form.to_dict(flat=True)
            new_user = User(
                username = data['username']
            )

            db.session.add(new_user)
            db.session.commit()
            return jsonify(msg = "user added successfully")

        @app.route("/add_personal_details", methods=['POST'])
        def add_personal_details():
            recv_username= request.args.get('username')
            user= User.query.filter_by(username=recv_username).first()

            data= request.get_json()

            new_personal_details= PersonalDetails(
                name= data['name'],
                email= data['email'],
                phone= data['phone'],
                address= data['address'],
                linkedin_url= data['linkedin_link'],
                user_id= user.id
            )
            
            db.session.add(new_personal_details)
            db.session.commit()
            return jsonify(msg = "Personal details updated successfully")

        @app.route("/add_project", methods=['POST'])
        def add_project():
            recv_username= request.args.get('username')
            user= User.query.filter_by(username=recv_username).first()

            project_data= request.get_json()
            for data in project_data["data"]:
                new_project= Projects(
                    name= data['name'],
                    desc= data['description'],
                    start_date= data['start_date'],
                    end_date= data['end_date'],
                    user_id= user.id
            )
            
            db.session.add(new_project)
            db.session.commit()
            return jsonify(msg = "Project added successfully")

        @app.route("/add_skills", methods=['POST'])
        def add_skills():
            recv_username= request.args.get('username')
            user= User.query.filter_by(username=recv_username).first()

            skills_data= request.get_json()
            for data in skills_data["data"]:
                new_skills= Skills(
                    name= data['name'],
                    desc= data['description'],
                    start_date= data['start_date'],
                    end_date= data['end_date'],
                    user_id= user.id
            )
            
            db.session.add(new_skills)
            db.session.commit()
            return jsonify(msg = "Skills added successfully")

        @app.route("/experiences", methods=['POST'])
        def experience():
            recv_username= request.args.get('username')
            user= User.query.filter_by(username=recv_username).first()

            experiences_data= request.get_json()
            for data in experiences_data["data"]:
                new_experiences= Experiences(
                    company_name= data['name'],
                    role_desc= data['description'],
                    start_date= data['start_date'],
                    end_date= data['end_date'],
                    user_id= user.id
            )
            
            db.session.add(new_experiences)
            db.session.commit()
            return jsonify(msg = "Experience added successfully")

        #db.drop_all()
        db.create_all()
        db.session.commit()

        return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)