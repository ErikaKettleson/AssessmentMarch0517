"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
    1. OO allows for unique reuse of components: "polymorphism". This means 
        that different implementations of the same function return different 
        things. In classes, this allows subclasses to modify parent's methods.
    2. OO hides unneccesary abstract implementation details, for example
        I don't need to know how datetime.now works to be able to use it. This
        is called "abstraction".
    3. "Encapsulation" allows for particular units of data/function storage,
        for example, a class has data only accessible to its internal functions

2. What is a class?
    A class is a prototype for an object with a set of attributes
    - methods & variables - characterizing instances of the class.

3. What is an instance attribute?
    Unlike Class attributes that will be shared by all instances of
    the class, instance attributes are unique to instances.

4. What is a method?
    Methods are functions defined for a class. Methods have parameters
    - at least self - and can call each other like non-class-specific functions

5. What is an instance in object orientation?
    An instance is each specific instatiated object created while running a
    program. Each melon is a specific instance of "melon" (you can't buy
    the general idea of 'melon', but you can buy an instance of a particular
    melon.)

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
    Class attributes are class-wide. They are the essence of the category. You
    just aren't a mammal if you are cold-blooded and lay eggs. Similarly, you
    cannot be a car with no motor. Instance attributes are particular to
    each instance. They share their class attributes but have specific
    inheritances instatiated with each new instance.

    For example: Within the parent class of "Coffee" the class attribute
    shared by all instances is the inclusion of coffee beans. Instance
    attributes are unique to each coffee instance. They might include price,
    place aquired, temperature of coffee, etc. These qualities vary so they
    shouldn't be class-wide. Perhaps there is enough Iced Coffee attributes for
    it to become parent of Coffee's grandchild lil' Cold Brew.



"""

# Part 2-5

class Student(object):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.score = 0

class Question(object):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        print self.question
        answer = raw_input("answer here > ")
        if answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
        self.questions.append(Question(question, correct_answer))

    def administer(self):
        score = 0.0
        for question in self.questions:
            if question.ask_and_evaluate():
                score = score + 1.0
        return float(score/len(self.questions))

# I am unsure about part 5.

# class Quiz(Exam):
#     def administer(self):
#         score = 0.0
#         for question in self.questions:
#             if question.ask_and_evaluate():
#                 score = score + 1.0
#         return float(score/len(self.questions))
#         if score >= 0.5:
#             return True
#         else:
#             return False


def take_test(exam, student):
    student.score = exam.administer()
    print student.score

def example():
    midterm = Exam("midterm")
    midterm.add_question("WHY???", "because")
    midterm.add_question("WHO???", "me, mario")
    midterm.add_question("1 + 1", "2")
    erika = Student("Erika", "Kettleson", "2623 Mission St")
    take_test(midterm, erika)

example()
