#Function to analyze marks from given dictionary.
def analyze_marks(marks_dict):
    values = list(marks_dict.values())

    highest_marks = values[0]
    lowest_marks = values[0]
    total = 0

    for value in values:
        if value > highest_marks:
            highest_marks = value
        if value < lowest_marks:
            lowest_marks = value
        total += value

    average_marks = total / len(marks_dict)
    return highest_marks, lowest_marks, average_marks

#Function to count the frequency of word in sentence.
def word_frequency(sentence):
    frequency = {}
    words = sentence.lower().split()

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


if __name__ == "__main__":
    students = {
        "Riya": 85,
        "Aman": 72,
        "Neha": 48,
        "Vikram": 95,
        "Sara": 67,
        "Karan": 43,
        "Pooja": 88,
        "Ramesh": 59,
        "Tina": 49,
        "Ali": 78
    }

    sentence = "Maharashtra is a state in India"
    print(f"For given dictionary of student highest marks, lowest marks and average marks are {analyze_marks(students)} respectively.")
    print(word_frequency(sentence))
