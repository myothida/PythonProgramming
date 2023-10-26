"""
1) Write a Python program to create a dictionary that count the frequency of words in the string given in Q1.txt. 
Find the most frequent occured word.
"""

#step 1: read content from Q1.txt into list
filepath1 = r"D:\00_University_Faculty\01_Project\08_Python\Parami_Fall_2023\Mid-Term_Exam_Submission\Q1.txt"

with open(filepath1, "r") as file1:
    text = file1.read()

# Step 2: Tokenize the text into words
words = text.split()

# Step 3: Create a dictionary to store word frequencies
word_freq = {}

# Step 4: Iterate through the words and update the dictionary
for word in words:
    # Remove punctuation and convert to lowercase to ensure accurate word counts
    word = word.strip(".,!?\"'()[]{}:;")
    word = word.lower()
    
    # Update the word frequency dictionary
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Print the word frequencies
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
    
most_frequent_response = max(word_freq, key=word_freq.get, default=None)
count = word_freq[most_frequent_response] if most_frequent_response is not None else 0

print(("The most frequent occured word: {} and the no. of times it appeared: {}").format(most_frequent_response, count))

print("--------------------------------")

"""
2) Write a Python program to read the name from Q2.txt and create email using domain 'parami.edu.mm' and save the results as dictionary : {'name': 'name@parami.edu.mm'}. 
   Please take note that your email should not include space or any special characters and all charcters should be in lowercase.
"""
#step 1: read Q2. txt into the list

filepath2 = r"D:\00_University_Faculty\01_Project\08_Python\Parami_Fall_2023\Mid-Term_Exam_Submission\Q2.txt"
with open(filepath2, 'r') as file2:
   header = file2.readline()
   namelist = file2.readlines()
    
   # Define the domain
   domain = 'parami.edu.mm'

   # Initialize an empty dictionary to store the results
   email_dict = {}
   for line in namelist:
       # Remove leading and trailing whitespace, and convert to lowercase
       name = line.strip().lower()

       # Remove spaces and special characters from the name
       name = ''.join(c for c in name if c.isalnum())

       # Create the email using the domain
       email = f'{name}@{domain}'

       # Add the result to the dictionary
       email_dict[name] = email

   # Print the resulting dictionary
   print(email_dict)




