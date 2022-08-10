class Calc():

    def percentage(self, val1, val2):
        return str((val1 / val2) * 100) + "%"

    def divide(self, val1, val2):
        return val1 / val2

    def multiply(self, val1, val2):
        return val1 * val2

    def calc_DoB(self, year, age):
        return year - age

    def cm_m(self, cm):
        return cm/100

