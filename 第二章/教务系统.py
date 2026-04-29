class Student:
    def __init__(self, name, china_score,math_score,english_score):
        self.name = name
        self.china_score = china_score
        self.math_score = math_score
        self.english_score = english_score

    def __str__(self):
        return f"姓名:{self.name} 语文:{self.china_score} 数学:{self.math_score} 英语{self.english_score} 总分:{self.china_score + self.math_score + self.english_score}"


    def update_score(self,china_score=None,math_score=None,english_score=None):
        if china_score  is not  None:
            self.china_score = china_score
        if math_score is not None:
            self.math_score = math_score
        if english_score is not None:
            self.english_score = english_score


class EducationStudent():
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []


    def add_student(self):
        name = input("请输入学生姓名:")
        for s in self.student_list:
            if s.name == name:
                print("学生已经存在添加失败")
                return
        chinese = int(input("请输入学生语文成绩:"))
        math=int(input("请输入学生数学成绩:"))
        english =int(input("请输入学生英语成绩:"))
        if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("添加成功")
        else:
            print("添加失败,成绩只能在0-100之间")


    def update_student(self):
        name = input("请输入要修改的学生姓名")
        for s in self.student_list:
            if s.name == name:
                print(f"{s}")
                chinese = int(input("请输入学生修改后语文成绩:"))
                math = int(input("请输入学生修改后数学成绩:"))
                english = int(input("请输入学生修改后英语成绩:"))
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese,math,english)
                    print("修改成功")
                    return
                else:
                    print("添加失败,成绩只能在0-100之间")
                    return
        print("未找到该学生")

    def delete_student(self):
        name = input("请输入删除学生的姓名")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("删除成功")
                return
        print("未找到该学生,删除失败")

    def query_student(self):
        name = input("请输入要查询的学生姓名")
        for s in self.student_list:
            if s.name == name:
                print(f"学生的信息是:{s}")
            else:
                print("没有该学生")
    def list_student(self):
        for s in self.student_list:
            print(s)

    def run(self):
        print("欢迎使用教务系统")

        while True:
            print()
            print("#################################################################")
            print("1.添加学生 2.修改学生 3.删除学生 4.查询指定学生 5.查询所有学生 6.退出系统 ")
            print("#################################################################")
            print()
            choice = input("请选择要执行的操作，输入1-6:")

            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.update_student()
                case "3":
                    self.delete_student()
                case "4":
                    self.query_student()
                case "5":
                    self.list_student()
                case "6":
                    break
                    print("退出成功")
                case _:
                    print("输入错误")



if __name__ == '__main__':
    s = EducationStudent()
    s.run()
