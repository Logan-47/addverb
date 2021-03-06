from api import app

if __name__=='__main__':
	app.run(debug=True)


# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(200), nullable=False)
#     # password = db.Column(db.String(20), nullable = False)
#     name = db.Column(db.String(200), default="Sundaram Dubey")
#     course = db.Column(db.String(200), default="UG")
#     college = db.Column(db.String(200), default="HBTU")
#     #is_teacher = db.Column(db.Boolean(), default=False)
#     #isTeacher = db.Column(db.Boolean(), default=False)

#     def __repr__(self):
#         return "<task %r> " % self.id

# class Teacher(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(200), nullable=False)
#     password = db.Column(db.String(20), nullable = False)
#     name = db.Column(db.String(200), default="Sundaram")
#     college = db.Column(db.String(200), default="HBTU")
#     subject = db.Column(db.String(200), default="CG")
#     is_teacher = db.Column(db.Boolean(), default=True)

# @app.route('/student-register', methods=['GET', 'POST'])
# def register():
#     """Register Form"""
#     if request.method == 'POST':
#         new_user = Student(
#             email=request.form['email'],
#             password=request.form['password'])
#         db.session.add(new_user)
#         db.session.commit()
#         return render_template('student_login.html')
#     return render_template('student_register.html')

# @app.route('/student-login', methods=['GET', 'POST'])
# def StudenLogin():
# 	if request.method == 'GET':
# 		return render_template('student_login.html')
# 	else:
# 		email = request.form['email']
# 		passw = request.form['password']
# 		try:
# 			data = db.session.query(Student).filter_by(email=email, password=passw).first()
# 			#db.session.commit()
# 			if data is not None:
# 				session['logged_in'] = True
# 				session["teacher_logged_in"] = False
# 				return redirect(url_for('explore'))
# 			else:
# 				return 'Dont Login'
# 		except:
# 			return "Something Went wrong"

# @app.route('/', methods =['GET', 'POST'])
# def home():
#     return render_template("index.html")

# @app.route("/teacher-login", methods=["GET", "POST"])
# def TeacherLogin():
# 	if(request.method == "POST"):
# 		username = request.form["username"]
# 		password = request.form["password"]
# 		if(username == "teacher" and password=="teacher"):
# 			session["teacher_logged_in"] = True
# 			session["logged_in"] = False
# 			return redirect("/schedule")
# 		else:
# 			return "something went wrong"
# 	else:
# 		return render_template("teacher_login.html")

# @app.route("/all-students", methods=["GET", "POST"])
# def allStudents():
# 	allstudents = db.session.query(Student).all()
# 	db.session.commit()
# 	return render_template("allstudents.html", allstudents=allstudents)


# @app.route("/logout")
# def logout():
# 	session['logged_in'] = False
# 	session["teacher_logged_in"] = False
# 	return redirect(url_for('home'))

# # @app.route("/questions", methods =['GET', 'POST'])
# # def questions():
# # 	questions = question.query.all()
# #     return render_template("all_questions.html")

# @app.route("/explore", methods =['GET', 'POST'])
# def explore():
# 	return render_template("explore.html")

# @app.route("/e-learning", methods = ['GET', 'POST'])
# def elearning():
# 	return render_template("elearning.html")

# @app.route("/current-classes", methods = ["Get", "POST"])
# def currentClass():

# 	allclasses = db.session.query(MySchedule).all()
# 	upcoming_classes = []
# 	previous_classes = []
# 	for i in allclasses:
# 		t = i.time.split("T")
# 		x = str(datetime.utcnow()).split(" ")
# 		current_time_hour = x[1][0:2]
# 		current_time_min = x[1][3:5]
# 		current_time_date = x[0]
# 		class_time_hour = t[1][0:2]
# 		class_time_min = t[1][3:5]
# 		class_time_date = t[0]
# 		if(current_time_hour > class_time_hour or class_time_date < current_time_date):
# 			previous_classes.append(i)
# 		else:
# 			upcoming_classes.append(i)

# 	return render_template("todayclass.html", previous_classes = previous_classes, upcoming_classes = upcoming_classes)

# # @app.route("/active-assignment", methods = ["Get", "POST"])
# # def assignments():
# # 	return render_template()

# # @app.route("/all-assignments", methods = ["Get", "POST"])
# # def posts():
# # 	return render_template()


# @app.route('/all-questions', methods=['GET', 'POST'])
# def allQuestions():
# 	if request.method == "POST":
# 		title = request.form["title"]
# 		task_content = request.form['content']
# 		complete_in = request.form["completetime"]
# 		subject = request.form["subject"]
# 		email= request.form["email"]
# 		name = request.form["std_name"]
# 		tags = request.form["tags"]
# 		new_task = Todo(title=title,content=task_content,subject=subject,complete_in=complete_in,email=email, name=name, tags=tags)
# 		try:
# 			db.session.add(new_task)
# 			db.session.commit()
# 			return redirect('/all-questions')
# 		except:
# 			return "there was an error in adding your task"

# 	else:
# 		tasks = Todo.query.order_by(Todo.date_create).all()
# 		new_tasks = []
# 		previous_tasks = []
# 		for i in tasks:
# 			if i.date_create + timedelta(days=i.complete_in) >  datetime.utcnow():
# 				new_tasks.append(i)
# 			else:
# 				previous_tasks.append(i)

# 		return render_template('allquestions.html', tasks=new_tasks, previous_tasks = previous_tasks)

# @app.route('/detail/<int:id>', methods=['GET', 'POST'])
# def detail(id):
# #detalle = db.info.find_one({"_id": ObjectId(id)})
# 	if(request.method == "POST"):
# 		content = request.form["content"]
# 		email = request.form["email"]
# 		name = request.form["name"]
# 		answer = Answer(name=name, email=email, content=content, answer_id = id)
# 		try:
# 			db.session.add(answer)
# 			db.session.commit()
# 		except:
# 			return "something went wrong"
# 	questions = db.session.query(Todo).get(id)
# 	answers = db.session.query(Answer).filter_by(answer_id=id).all()
# 	db.session.commit()
# 	return render_template("answer.html", questions = questions, answers = answers)

# @app.route("/addpoints/<int:id>", methods=['GET', 'POST'])
# def Addpoints(id):
# 	if(request.method == "POST"):
# 		try:
# 			question = db.session.query(Todo).filter_by(id=id).first()
# 			points = request.form["points"]
# 			question.points = points
# 			db.session.commit()
# 			return redirect("/all-questions")
# 		except:
# 			return "something went wrong"
# 	else:
# 		return render_template("addpoints.html", id = id)

# @app.route("/deletequestion/<int:id>", methods=["GET", "POST"])
# def deleteQuestion(id):
# 	if(request.method == "POST"):
# 		try:
# 			db.session.query(Todo).filter_by(id=id).delete()
# 			db.session.commit()
# 			return redirect("/all-questions")
# 		except:
# 			return "error occured"
# 	elif(request.method == "GET"):
# 		return redirect("/all-questions")

# @app.route('/progress/<int:id>', methods=['GET', 'Method'])
# def progress(id):
# 	student_email = db.session.query(Student).filter_by(id=id).first()
# 	answer_count = db.session.query(Answer).filter_by(email=student_email.email).count()
# 	question_count = db.session.query(Todo).count()
# 	return render_template("progress.html", answer_count=answer_count, question_count=question_count)



# @app.route("/schedule", methods=["GET", "POST"])
# def setSchedule():
# 	if(request.method=="POST"):
# 		subject = request.form["subject"]
# 		topic = request.form["topic"]
# 		time = request.form["time"]
# 		url = request.form["meetingurl"]
# 		new_schedule = MySchedule(subject=subject, topic=topic, time=time, url = url)
# 		try:
# 			db.session.add(new_schedule)
# 			db.session.commit()
# 			return redirect("/schedule")
# 		except:
# 			return "something went wrong"
# 	else:
# 		current_time = datetime.utcnow
# 		subjectclasses = db.session.query(MySchedule).filter_by(subject="DMS").all()
# 		db.session.commit()
# 		allclasses = db.session.query(MySchedule).all()
# 		db.session.commit()
# 		return render_template("schedule.html", allclasses=allclasses, subjectclasses = subjectclasses)


# I AM IRON-MAN
