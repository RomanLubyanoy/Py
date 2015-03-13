class Student(object):
    s_name = None
    lab_list = []
    exam = 0
    exam_max = None
    lab_max = None
    k = None

    def __init__(self, name, conf):
        self.s_name = name
        self.lab_list = [0 for x in range(conf['lab_num'])]
        self.exam_max = conf['exam_max']
        self.lab_max = conf['lab_max']
        self.k = conf['k']

    def make_lab(self, lab_point=0, lab_number=None):
        if lab_point < 0:
            return self
        if lab_point > self.lab_max:
            lab_point = self.lab_max
        if lab_number is not None and len(self.lab_list)-1 >= lab_number >= 0:
            self.lab_list[lab_number] = lab_point
        else:
            for index, item in enumerate(self.lab_list):
                if item == 0:
                    self.lab_list[index] = lab_point
                    break
        return self

    def make_exam(self, exam_point=0):
        if exam_point < 0:
            return self
        if exam_point > self.exam_max:
            exam_point = self.exam_max
        self.exam = exam_point
        return self

    def is_certified(self):
        if (sum(self.lab_list) + self.exam)/100.0 >= self.k:
            return sum(self.lab_list) + self.exam, True
        else:
            return sum(self.lab_list) + self.exam, False




conf1 = {
    'exam_max': 20,
    'lab_max': 40,
    'lab_num': 2,
    'k': 0.75,
}


o3 = Student('Oleg', conf1)

o3.make_lab(10).make_lab(10).make_exam(15)
print o3.lab_list, o3.exam
print o3.is_certified()
o3.make_lab(20,1).make_lab(20,0)
print o3.lab_list, o3.exam
print o3.is_certified()
o3.make_lab(50,2)
print o3.is_certified()
o3.make_lab(40,1)
print o3.is_certified()




conf_check = {
    'exam_max': 30,
    'lab_max': 7,
    'lab_num': 10,
    'k': 0.61,
}

oleg = Student('Oleja', conf_check)

print oleg.s_name, oleg.lab_list, oleg.exam
oleg.make_lab(1)
print oleg.s_name, oleg.lab_list, oleg.exam
oleg.make_lab(8,0)
print oleg.s_name, oleg.lab_list, oleg.exam
oleg.make_lab(1)
print oleg.s_name, oleg.lab_list, oleg.exam
oleg.make_lab(10,7)
print oleg.s_name, oleg.lab_list, oleg.exam
oleg.make_lab(4, 1)
print oleg.s_name, oleg.lab_list, oleg.exam
oleg.make_lab(5)
print oleg.s_name, oleg.lab_list, oleg.exam
oleg.make_lab(6.5)
print oleg.s_name, oleg.lab_list, oleg.exam
oleg.make_exam(31)
print oleg.s_name, oleg.lab_list, oleg.exam
print oleg.is_certified()
oleg.make_lab(7,1)
print oleg.s_name, oleg.lab_list, oleg.exam
print oleg.is_certified()
