#Function to sum of all numbers in list
def sum_of_numbers(numbers):    
    total = 0  
    for num in numbers:
        total += num
    return total

#Function to count vowels in strings
def count_vowels(text):
    text = text.lower()   
    vowel_count = 0
    for ch in text:
        if ch in "aeiou":
            vowel_count += 1
    return vowel_count

#Function to check whether the number is positive, negative or zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
    
#main function
if __name__ == "__main__":
    nums = [2,4,6,8,10]
    name = "Shruti Chauhan"
    digit = 54

    print(f"Sum of all numbers in list is {sum_of_numbers(nums)}")
    print(f"Vowel count in {name} is {count_vowels(name)}")
    print(f"{digit} is {check_number(digit)}")

