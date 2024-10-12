# 파이썬에서의 `__init__`

파이썬의 `__init__` 메서드는 **클래스의 객체를 초기화하는 데 사용된다.**
**생성자**라고도 한다.
`C++` 및 `Java`의 **기본 생성자**와 같다. 
클래스의 객체가 생성될 때 클래스의 데이터 멤버에 값을 초기화(할당)하는 역할을 한다.
### 예시
```Python
class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is ', self.name)

    p = Person('Ubukki')
    p.say_hi()
```
> 결과: Hello, my name is Ubukki

먼저 `Ubukki`라는 `Person`이 생성된다. 그 다음 `"Ubukki"`가 `__init__` 메서드에 인수로 전달되고 객체를 초기화 한다.

`self`라는 키워드는 클래스의 인스턴스를 나타내고, 주어진 인수로 속성을 바인딩한다.

또 다른 예시를 살펴보자.

```Python
class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is ', self.name)

p1 = Person('Ubukki')
p2 = person('Eun Been Kang')
p3 = Person('우북이')

p1.say_hi()
p2.say_hi()
p3.say_hi()
```
> 결과:
> Hello, my name is Ubukki
> Hello, my name is Eun Been Kang
> Hello, my name is 우북이

---

참고: <https://www.geeksforgeeks.org/__init__-in-python/>
