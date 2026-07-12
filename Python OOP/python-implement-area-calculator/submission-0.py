import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, *args:int) -> float:
        if len(args) == 2:
            return args[0] * args[1]
        elif len(args) == 1:
            return round(math.pi * (args[0]**2),2)
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
