from abc import ABC, abstractmethod
from typing import Self


class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def get_info(self) -> str:
        return f"{self.full_name}, {self.age} лет"


class ScholarshipCalculator(ABC):
    @abstractmethod
    def calculate_scholarship(self, average_grade: float) -> int:
        pass


class StudentScholarship(ScholarshipCalculator):
    def calculate_scholarship(self, average_grade: float) -> int:
        if average_grade == 5:
            return 6000
        elif average_grade >= 4:
            return 4000
        return 0


class GraduateStudentScholarship(ScholarshipCalculator):
    def calculate_scholarship(self, average_grade: float) -> int:
        if average_grade == 5:
            return 8000
        elif average_grade >= 4:
            return 6000
        return 0


class BaseStudent(Person):
    def __init__(self, first_name: str, last_name: str, age: int, 
                 group_number: str, average_grade: float,
                 scholarship_calculator: ScholarshipCalculator):
        super().__init__(first_name, last_name, age)
        self.group_number = group_number
        self.average_grade = average_grade
        self._scholarship_calculator = scholarship_calculator
    
    def get_scholarship(self) -> int:
        return self._scholarship_calculator.calculate_scholarship(self.average_grade)
    
    def scholarship_greater_than(self, other: Self) -> bool:
        return self.get_scholarship() > other.get_scholarship()
    
    def get_detailed_info(self) -> str:
        return (f"{self.get_info()}, группа {self.group_number}, "
                f"средний балл {self.average_grade}, стипендия {self.get_scholarship()}р")


class Student(BaseStudent):
    def __init__(self, first_name: str, last_name: str, age: int, 
                 group_number: str, average_grade: float):
        super().__init__(first_name, last_name, age, group_number, average_grade,
                        StudentScholarship())
    
    def __str__(self) -> str:
        return f"Студент: {self.get_detailed_info()}"


class GraduateStudent(BaseStudent):
    def __init__(self, first_name: str, last_name: str, age: int,
                 group_number: str, average_grade: float, research_topic: str):
        super().__init__(first_name, last_name, age, group_number, average_grade,
                        GraduateStudentScholarship())
        self.research_topic = research_topic
    
    def get_detailed_info(self) -> str:
        return (f"{super().get_detailed_info()}, "
                f"научная работа: '{self.research_topic}'")
    
    def __str__(self) -> str:
        return f"Аспирант: {self.get_detailed_info()}"


def main():
    # Демонстрация работы
    graduate = GraduateStudent("Иван", "Петров", 25, "5132704/100001", 4.86, "Исследование алгоритмов")
    student = Student("Мария", "Мащалкина", 19, "5132704/30801", 4.71)
    
    people = [student, graduate]
    
    print("\n  ИНФОРМАЦИЯ ОБ УЧАЩИХСЯ ")
    for person in people:
        print(person)
    
    print("\n СРАВНЕНИЕ СТИПЕНДИЙ ")
    if graduate.scholarship_greater_than(student):
        print(f"{graduate.first_name} получает стипендию больше, чем {student.first_name}")
    else:
        print(f"{student.first_name} получает стипендию больше, чем {graduate.first_name}")


if __name__ == "__main__":
    main()