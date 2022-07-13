class Person:
    # 파이썬은 생성자 메서드에서 자기 자신을 인자로 넘겨준다.
    # 파이썬 클래스가 알아서 항상 넘겨줌.
    def __init__(self, param_name):
        print("i am created! ", self)
        self.name = param_name

    def talk(self):
        print("안녕하세요, 제 이름은 " + self.name + " 입니다.")

person_1 = Person("Kim")
print(person_1.name)
person_1.talk()
person_2 = Person("Lee")
print(person_2.name)
person_2.talk()
print(person_1, person_2)