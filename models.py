from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class EmployeeModel(db.Model):
    __tablename__ = "table"
 
    id = db.Column(db.Integer, primary_key=True)
    Employee_id = db.Column(db.Integer(),unique = True)
    First_name = db.Column(db.Integer(),unique = True)
    Last_name = db.Column(db.String())
    Screen_name = db.Column(db.String())
    Date_of_birth = db.Column(db.String())
    Gender = db.Column(db.String())
    Country = db.Column(db.String())
    Email = db.Column(db.String())
    Phone = db.Column(db.Integer())
    Password = db.Column(db.String())
    Confirm_password = db.Column(db.String())

 
    def __init__(self,Employee_id,First_name,Last_name,Screen_name,Date_of_birth,Gender,Country,Email,Phone,Password,Confirm_password):
        self.Employee_id = Employee_id
    # def __init__(self,First_name):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Screen_name = Screen_name
        self.Date_of_birth = Date_of_birth
        self.Gender = Gender
        self.Country = Country
        self.Email = Email
        self.Phone = Phone
        self.Password = Password
        self.Confirm_password = Confirm_password
 
    def __repr__(self):
        return f"{self.First_name}:{self.id}"

       