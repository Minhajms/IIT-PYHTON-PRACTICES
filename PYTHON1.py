from datetime import datetime,time
import pytz
import math
ist_timezone = pytz.timezone("Asia/Kolkata")
paneer_tikka=int(250)
butter_chicken=int(240)
masala_dosa=int(200)
print('which food did you eat')
option1=int(input("paneer_tikka: "))
option2=int(input("butter_chicken: "))
option3=int(input("masala_dosa: "))

current_time = datetime.now(ist_timezone)
print(current_time)
total_amount=(option1*paneer_tikka)+(option2*butter_chicken)+(option3*masala_dosa)
apply_coupon = input('Do you have a coupon? (yes/no): ').strip().lower()
if apply_coupon == 'yes':
  total_amount=(total_amount*0.90)
else:
  total_amount=total_amount
if time(13, 0, 0) <= current_time.time() <= time(14, 0, 0):
  total_amount=(total_amount*0.85)
else:
  total_amount=total_amount
payment=input('card or cash')
if payment == ('card'):
  print(total_amount+(total_amount*0.05))
else:
  print(f"Total amount: ₹{total_amount:.2f}")


#my first projct to calculate hotel bill


<<<<<<< HEAD
=======
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def matforz():
  return M[0]+[M[1][1]]+M[2]

print(matforz())
def matforo():
   return M[0]+[M[1][2]]+M[-1][::-1]+[M[1][0]]
print(matforo()) 
>>>>>>> 28c128f (Your commit message)
