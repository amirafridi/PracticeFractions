# Amir Afridi
# U01470999
# PracticeFractions.py
# CIS4930 Final Project

# imports
import easygui
from fractions import Fraction
import operator
from random import randint

# Function for main menu.  it is immediately called, and called whenever the
# return to main menu button is hit.


def main():
    mode = easygui.buttonbox('Welcome to Fractions.',
                             'practiceFractions', ('Solver', 'Quizzer', 'Quit'))
    if(mode == 'Solver'):
        solver()
    elif(mode == 'Quizzer'):
        quizzer()


def solver():
    input = easygui.enterbox("Enter Fraction Expression?")
    if (input):
        try:
            F = Fraction(input)
            msg = 'Fraction ' + input + ' = ' + str(F)
            action = easygui.buttonbox(
                msg, 'Solver', ('Solve Another', 'Return to Main Window'))
            if(action == 'Solve Another'):
                solver()
            else:
                main()
        except:
            action = easygui.buttonbox(
                'Invalid Fraction', 'Error', ('Try Again', 'Return to Main Window'))
            if(action == 'Try Again'):
                solver()
            else:
                main()
    else:
        action = easygui.buttonbox(
            'Invalid Fraction', 'Error', ('Try Again', 'Return to Main Window'))
        if(action == 'Try Again'):
            solver()
        else:
            main()


def quizzer():
    # Choose what operation (add, sub, mult)
    op = easygui.buttonbox('Choose Operator.', 'Quizzer', ('+', '-', '*'))
    # Setup the fractions
    N1 = randint(-15, 15)
    D1 = randint(1, 15)
    F1 = Fraction(str(N1) + '/' + str(D1))
    N2 = randint(-15, 15)
    D2 = randint(1, 15)
    F2 = Fraction(str(N2) + '/' + str(D2))

    # find the solution
    if op == '+':
        R = operator.add(F1, F2)
    elif op == '-':
        R = operator.sub(F1, F2)
    else:
        R = operator.mul(F1, F2)

    msg = '(' + str(F1) + ')' + op + '(' + str(F2) + ') = '
    # user enters solution
    answer = easygui.enterbox(msg)

    try:
        F = Fraction(answer)
        if(answer == str(R)):
            msg = 'Correct Answer! ' + msg + ' ' + str(R)
        elif str(F) == str(R):
            msg = 'Almost Correct, Not Reduced. ' + msg + ' ' + str(R)
        else:
            msg = 'Incorrect Answer. ' + msg + ' ' + str(R)

        action = easygui.buttonbox(
            msg, 'Quizzer', ('Another Quiz', 'Return to Main Menu'))
        if(action == 'Another Quiz'):
            quizzer()
        else:
            main()

    except:
        action = easygui.buttonbox(
            'Invalid Fraction', 'Error', ('Try Again', 'Return to Main Menu'))
        if(action == 'Try Again'):
            quizzer()
        else:
            main()


if __name__ == "__main__":
    # Call the main function
    main()
