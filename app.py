
from flask import Flask,render_template,request,redirect
from models import db,EmployeeModel

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db5.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

 
@app.before_first_request
def create_table():
    db.create_all()

@app.route('/data/add' , methods = ['GET','POST'])
def add():
    if request.method == 'GET':
        return render_template('createpage.html')

    if request.method == 'POST':
        print (request)    
        Employee_id = request.form['Employee_id']
        First_name = request.form['First_name']
        print(First_name)
        Last_name = request.form['Last_name']
        Screen_name = request.form['Screen_name']
        Date_of_birth = request.form['Date_of_birth']
        Gender = request.form['Gender']
        Country = request.form['Country']
        Email = request.form['Email']
        Phone = request.form['Phone']
        Password = request.form['Password']
        Confirm_password = request.form['Confirm_password']
        employee = EmployeeModel(Employee_id=Employee_id,First_name=First_name, Last_name=Last_name, Screen_name= Screen_name, Date_of_birth=Date_of_birth, Gender=Gender, Country=Country, Email=Email, Phone=Phone, Password=Password, Confirm_password=Confirm_password)
        print (employee,"abcd")
        db.session.add(employee)
        print ("xyz--")
        db.session.commit()
        print ("success")
        # return "data addedd"
        return redirect('/data')
        # return render_template('createpage.html')

# @app.route('/data/create' , methods = ['POST'])
# def createds():
#         print(request.form)
    #     employee = EmployeeModel(First_name=)
    #     print (employee,"abcd")
    #     db.session.add(employee)
    #     print ("xyz--")
    #     db.session.commit()
    #     print ("success")
    #     return "data added"
    #     return redirect('/data')
    # if request.method == 'GET':
    #     return render_template('createpage.html')
 
    # if request.method == 'POST':
    #     print ("abc")
    #     print (request)

        # Employee_id = request.form['employee_id']
        # First_name = request.form['First_name']
        # print(First_name)
        # Last_name = request.form['Last_name']
        # Screen_name = request.form['Screen_name']
        # Date_of_birth = request.form['Date_of_birth']
        # Gender = request.form['Gender']
        # Country = request.form['Country']
        # Email = request.form['Email']
        # Phone = request.form['Phone']
        # Password = request.form['Password']
        # Confirm_password = request.form['Confirm_password']
        # employee = EmployeeModel(Employee_id=Employee_id,First_name=First_name, Last_name=Last_name, Screen_name= Screen_name, Date_of_birth=Date_of_birth, Gender=Gender, Country=Country, Email=Email, Phone=Phone, Password=Password, Confirm_password=Confirm_password)
        # # employee = EmployeeModel(First_name=First_name)
        # print (employee,"abcd")
        # db.session.add(employee)
        # print ("xyz--")
        # db.session.commit()
        # print ("success")
        # # return "data addedd"
        # return redirect('/data')
@app.route('/data')
def RetrieveDataList():
    employees = EmployeeModel.query.all()
    return render_template('datalist.html',employees = employees)

@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    employee = EmployeeModel.query.filter_by(Employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
 
            First_name = request.form['First_name']
            Last_name = request.form['Last_name']
            Screen_name = request.form['Screen_name']
            Date_of_birth = request.form['Date_of_birth']
            Gender = request.form['Gender']
            Country = request.form['Country']
            Email = request.form['Email']
            Phone = request.form['Phone']
            Password = request.form['Password']
            Confirm_password = request.form['Confirm_password']
            employee = EmployeeModel(Employee_id=id, First_name=First_name, Last_name=Last_name, Screen_name = Screen_name, Date_of_birth=Date_of_birth, Gender=Gender, Country=Country, Email=Email, Phone=Phone, Password=Password)
 
            db.session.add(employee)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Employee with id = {id} Does not exist"
 
    return render_template('update.html', employee = employee)

@app.route('/data/<int:id>')
def RetrieveSingleEmployee(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if employee:
        return render_template('data.html', employee = employee)
    return f"Employee with id ={id} Does not exist"

@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    employee = EmployeeModel.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')    

app.run(host='localhost', port=5000)
