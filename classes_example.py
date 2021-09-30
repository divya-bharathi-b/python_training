class employee:
    def __init__(self,empid,ename,esalary,edept):
        self.empid = empid
        self.ename = ename
        self.esalary = esalary
        self.edept = edept

    def display(self):
        print(self.empid, self.ename  ,)
