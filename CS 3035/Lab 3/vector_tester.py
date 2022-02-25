# Student Name: Ayush Singh
# CIN: 306692040
# Course: CS 3035-01
# Video Link: https://calstatela.instructuremedia.com/embed/49d9d2f1-9c48-4acb-9e80-4cbe381b7a32

from vector import Vector


def main():
    v1 = Vector(1, 10, 20)
    v2 = Vector(1, 10, 20)
    v3 = Vector(1, 10, 21)

    print("v1: " + str(v1))
    print("v2: " + str(v2))
    print("v3: " + str(v3))

    print("------------------------------------------------------")

    print("v1: __str__(): " + str(v1.__str__()))
    print("v1: __repr__(): " + str(v1.__repr__()))
    print("v1: magnitude(): " + str(v1.magnitude()))

    print("------------------------------------------------------")

    print("== Operator Overloading")
    print("v1 == v2: " + str(v1 == v2))
    print("v1 == v3: " + str(v1 == v3))

    print("------------------------------------------------------")

    print("+, += Operator Overloading")
    print(str(v1) + " + " + str(v2) + " = " + str(v1 + v2))
    v1_copy = Vector(1, 10, 20)
    v1_copy += v2
    print(str(v1) + " += " + str(v2) + " = " + str(v1_copy))

    print("------------------------------------------------------")

    print("-, -= Operator Overloading")
    print(str(v1) + " - " + str(v3) + " = " + str(v1 - v3))
    v1_copy2 = Vector(1, 10, 20)
    v1_copy2 -= v3
    print(str(v1) + " -= " + str(v3) + " = " + str(v1_copy2))

    print("------------------------------------------------------")

    print("*, *= Operator Overloading")
    multiplier = 5
    print("Dot Product: " + str(v1) + " * " + str(v2) + " = " + str(v1 * v2))
    print("Vector Scalar Multiplication (Vector First): " + str(v1) + " * " + str(multiplier) + " = " + str(v1 * multiplier))
    print("Vector Scalar Multiplication (Integer First): " + str(v1) + " * " + str(multiplier) + " = " + str(multiplier * v1))
    v1_copy3 = Vector(1, 10, 20)
    v1_copy3 *= multiplier
    print("Vector Scalar Multiplication: " + str(v1) + " *= " + str(multiplier) + " = " + str(v1_copy3))

    print("------------------------------------------------------")

    print("% Operator Overloading")
    print("Cross Product: " + str(v1) + " % " + str(v3) + " = " + str(v1 % v3))

    print("------------------------------------------------------")
    print("[] Operator Overloading")
    print(v1)
    print("v1 (a Value): " + str(v1[0]))
    print("v1 (b Value): " + str(v1[1]))
    print("v1 (c Value): " + str(v1[2]))
    print("Change b Value Of " + str(v1) + " to 100:")
    v1[1] = 100
    print(str(v1))


if __name__ == '__main__':
    main()
