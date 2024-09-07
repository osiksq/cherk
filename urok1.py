class Student:

    def __init__(self, name, age=15):
        self.age = age
        self.name = name
        print('Hi!')
        Student.count_of_student += 1

        def __str__(self):
            return f'Я {self.name}, Мне {self.age} лет'

        def __del__(self):
            print(f'Я {self.name}, я пошел')
            Student.count_of_student -= 1


        #def info(self):
            #print(f'Я {self.name}, Мне {self.age}, лет')





        def grow(self, delta=1):
            if self.age + delta > 100:
                print('Error Age')
                return
            self.age += delta





print(Student.count_of_student)

Anton = Student(name='Anton')
print(Anton.age)
Anton.grow()
Kirill = Student(name='Kirill', age=17)
print(Kirill.age)

print(Student.count_of_student)

print(Kirill)
print(Anton)

