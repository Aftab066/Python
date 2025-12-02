
#Class Is A like a form or a template of the program 
#Objects Is Variable or a method for class

class College:
    exam = "Sem V"
    applicant = "Aftab"
    etype = "Regular"
    def info(self):
        print(f"Examination : {self.exam} \n Applicant : {self.applicant} \n Exam Type : {self.etype}")

a = College()
a.exam = "Sem I"
a.applicant = "Omkar"
a.etype =  "Backlog"

a.info()