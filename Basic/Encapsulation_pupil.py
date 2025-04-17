class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        elif 80 <= score <= 89:
            return ("B")
        elif 70 <= score <= 79:
            return "C"
        elif 60 <= score <= 69:
            return "D"
        else:
            return "F"

    def add_course(self, course_name, score):
        self.course_name = course_name
        self.score = score
        letter_grade = self.calculate_letter_grade(score)
        self.__courses[course_name] = letter_grade

    def get_courses(self):
        return self.__courses