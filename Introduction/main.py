#------------------Introduction-----------------
class MyList(list):
    def __init__(self):
        super().__init__()
        self.mylen = 0

    def append(self, value):
        super().append(value)
        self.mylen += 1

l = MyList()

l.append("Manish")
l.append("Vikas")
l.append("Avinash")

# print(l.mylen)

my_string = "philippines"
nb_occurence = {letter: 0 for letter in my_string}
# print(nb_occurence)
# print(range(5))

# def myIterator():
#     for i in range(10):
#         yield i

# for i in myIterator():
#     print(i)

# import fractions
# f = fractions.Fraction(3,2)
# print(str(f))

# from tryalgo import arithm
# print(help(arithm))

# from collections import Counter

# c = Counter()
# c["a"] += 1
# M = [[0]*4]*4
# M[0][-1] = 5
# print(M)

