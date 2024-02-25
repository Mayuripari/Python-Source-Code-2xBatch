# HW
# Automation Tester Blueprint system
# Class - Student, Courses, Payment
# Object -
# Student - name, Id, age, gender
# Courses - PyATB, MTB, ATBJ, APIAT
# Payment - razorpay, stripe, instamojo

class Payment:
    razorpay = None
    stripe = None
    instamojo = None

    def option1(self):
        print("Pay thr razorpay")

    def option2(self):
        print("Pay thr stripe")

    def option3(self):
        print("Pay thr instamojo")


Mayuri = Payment()
Vina = Payment()
Vinod = Payment()
