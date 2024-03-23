#name the various events and caputre them as an input
swimming=int(input("What was the swimming timing in minutes?"))
cycling=int(input("What was the cycling timing in minutes?"))
running=int(input("What was the running timing in mimutes?"))
#add all the event together to get the final timing.
final_timing=swimming+cycling+running

if final_timing>=0 and final_timing<=100:
  print(f"Your final time is {final_timing}, you have won Provencial colors")
  #now let add all other conditions to get the final result
elif final_timing>=101 and final_timing<=105:
  print(f"Your final timing is {final_timing}, you have won Provencail Half colors ")
elif final_timing>=106 and final_timing<=110:
  print(f"Your final timing is {final_timing}, you have won Provencial scroll")
 #for result other than mentioned above we have the else statement 
else:
  print(f"Your final timing is {final_timing}")
