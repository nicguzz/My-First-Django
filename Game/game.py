import random
a = "198"

def gen_random(length):
    length += 1 #Number max of digits
    num_to_guess = "" 
    for attempt in range(1, length): #For 4 attempts:
        digit = str(random.randint(1,9)) #digit generator from 1 to 9.
        while digit in num_to_guess: #If the new number generated is in the num_to_guess list:
            digit = str(random.randint(1,9)) #create digit generator from 1 to 9 again.
        num_to_guess += digit #Here it adds the digit to num_to_guess list
    return num_to_guess

a = gen_random(4)

print(a)

def validate(num):
    if "0" in num:
        return False
    else:
        to_validate = [num for num in num]
        for digit in to_validate:
            to_validate.remove(digit)
        if digit in to_validate:
            return False
        else:
            return True


def check(num_to_guess):
    M = 0 
    E = 0
    for i, num in enumerate(user):
        if num in num_to_guess:
             if user[i] == num_to_guess[i]:
                E +=1
             else: 
                M +=1
    return (M, E)

user = 0
count = 0
if __name__ == '__main__':


    while user != "0":
        M = 0
        E = 0
        user = input("Your guess: ")

        if validate(user):
            for i, digit in enumerate(user):
                if digit in a:
                    if digit in a[i]:
                        E += 1
                    else: 
                        M += 1


                
            print(f"M: {M}, E: {E}")
            count += 1
            print(f"Attempts: {count}")
            if E == 4:
                print(f"Congrats! You have guessed the right number in {count} attempts.")
                break