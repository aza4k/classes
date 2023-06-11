from parallelogram import Parallel
from romb import Romb
from trapecia import Trapecia


shape_1 = Parallel(a=1,b=2,h=2)
print(f"Parallelogram \nP: {shape_1.perimetr()} \nS: {shape_1.square()}")


print("-------------------------------------------")


shape_2 = Romb(a=2,h=2)
print(f'Romb \nP: {shape_2.perimetr()} \nS: {shape_2.square()}')


print("-------------------------------------------")


shape_3 = Trapecia(a=2,b=2,c=3,d=2,h=2)
print(f'Trapecia \nP: {shape_3.perimetr()} \nS: {shape_3.square()}')
