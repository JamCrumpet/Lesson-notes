# rather than breaking out of a loop entirely without executing the rest of its code, you can use the ...
# ... continue statement to return to the beginning of the loop based on the results of the conditional tests

# for example consider a loop that counts from 1 to 10 but prints only the odd numbers in that range:

current_number = 0 # set current number to 0
while current_number < 10: # because current number is less than 10 while loop is executed
    current_number += 1 # +! is added to current number
    if current_number % 2 == 0: # if modulo is 0 the means current number is divisible by 2
        continue # continue tells python to ingnore the rest of the loop  and return to the beginning
# if the current number is not dicisible by 2 the rest of the loop is executed and prints the current number
    print(current_number)