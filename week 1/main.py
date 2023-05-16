from info import *

class Student:
    def __init__(self, id, name, age, major, grade):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__major = major
        self.__grade = grade

    def __str__(self):
        return self.__name
    
    def __str__(self):
        return self.__major

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_major(self):
        return self.__major
    
    def get_grade(self):
        return self.__grade
    
    def set_id(self):
        return self.__id
    
    def set_name(self):
        return self.__name
    
    def set_age(self):
        return self.__age
    
    def set_major(self):
        return self.__major
    
    def set_grade(self):
        return self.__grade
    

def main():
    student_manager_service = StudentManageImpl()

    while True:
        print("===============")
        print("1. 학생 추가")
        print("2. 전체 학생 조회")
        print("3. 학생 조회")
        print("4. 학생 제거")
        print("5. 학생 수정")
        print("6. 학점 순 학생 출력")
        print("7. 종료")
        print("===============")

        choice = int(input("번호를 입력하세요 >> "))

        if choice == 1:
            id = input("학번 : ")
            name = input("이름 : ")
            age = input("나이 : ")
            major = input("전공 : ")
            grade = input("학점 : ")
            student = Student(id, name, age, major, grade)
            student_manager_service.add_student(student)
            print("성공적으로 추가되었습니다.")
        elif choice == 2:
            students = student_manager_service.list_student()
            if students:
                for student in students:
                    print("학번 : ", student._Student__id)
                    print("이름 : ", student._Student__name)
                    print("전공 : ", student._Student__major)
                    print("나이 : ", student._Student__age)
                    print("학점 : ", student._Student__grade)
                    print(" ")
            else:
                print("학생이 존재하지 않습니다.")
        elif choice == 3:
            name = input("이름 : ")
            student = student_manager_service.search_student(name)
            if student is not None:
                print("학번 : ", student._Student__id)
                print("전공 : ", student._Student__major)
                print("나이 : ", student._Student__age)
                print("학점 : ", student._Student__grade)
            else:
                print("정보가 존재하지 않습니다.")
        elif choice == 4:
            name = input("이름 : ")
            if student_manager_service.delete_student(name):
                print("성공적으로 삭제되었습니다.")
            else:
                print("정보가 존재하지 않습니다")
        elif choice == 5:
            name = input("이름 : ")
            student = student_manager_service.search_student(name)
            if student:
                print("정보를 입력하세요")
                id = input("학번 : ")
                major = input("전공: ")
                age = input("나이 :")
                grade = input("학점 : ")
                update_student = Student(id, name, age, major, grade)
                student_manager_service.update_student(name, update_student)
                print("수정되었습니다.")
            else:
                print("정보가 존재하지 않습니다.")
        elif choice == 6:
            students = student_manager_service.sort_students_by_grade()
            if students:
                for student in students:
                    print("이름 : ",student._Student__name, "학점 : ", student._Student__grade)
            else:
                print("정보가 존재하지 않습니다.")
        elif choice == 7:
            break
        else:
            print("번호를 다시 입력하세요")

if __name__ == "__main__":
    manager = StudentManagerService()
    main()
