"""
This is the problem for Python Analyze Reviews

You're part of the data analytics team for a new app company. 
User feedback is essential for your company's success, 
and your task is to analyze user reviews to find trends and areas for improvement.

Each user review is represented as a dictionary with keys: id (unique identifier), 
rating (integer from 1 to 5), review (string), and date (string in the format "YYYY-MM-DD").

Given a list of these reviews, your task is to:

1. Calculate the average rating.

2. Identify the most common words in the reviews. Exclude any punctuation from the
reviews when identifying common words, and transform all words to lowercase for consistency.

3. Find the month with the most reviews submitted.

The current implementation has errors and inefficiencies. 
Correct the code to perform the tasks accurately.

Note: For this challenge, consider words to be any sequence of characters separated by spaces.
You can assume all words in reviews are in lowercase.

Example Input:

[
{"id": 1, "rating": 5, "review": "Great app. Love the features. The design is outstanding.",
"date": "2023-01-15"},
{"id": 2, "rating": 4, "review": "Very useful. It's become a daily tool for me.", 
"date": "2023-01-17"},
{"id": 3, "rating": 3, "review": "Decent, but some features don't work well.",
"date": "2023-02-05"},
{"id": 4, "rating": 2, "review": "I experienced some bugs. Needs fixing.",
"date": "2023-02-11"},
{"id": 5, "rating": 5, "review": "Outstanding! Everything I wanted in an app.", 
"date": "2023-02-14"},
{"id": 6, "rating": 4, "review": "Good app overall, just some minor issues.", 
"date": "2023-02-20"},
{"id": 7, "rating": 3, "review": "Average, but the user experience could be better.", 
"date": "2023-03-05"}
]

Example Output:

Average Rating: 3.7
Most Common Words: ['app']
Month with Most Reviews: February


This is the code that it has given

import string

def analyze_reviews(reviews):
  total_rating = 0
  word_count = {}
  monthly_reviews = {}
  STOPWORDS = set(["the", "and", "a", "to", "of", "in", "but", "some", "is",
  "it", "i", "for", "on", "with", "was"])

  for review in reviews:
    words = review["review"].lower().split()

    for word in words:
      if word not in STOPWORDS:
        word_count[word] = word_count.get(word, 0) + 1

    month = review["date"]
    monthly_reviews[month] = monthly_reviews.get(month, 0) + 1
  
  max_word_count = max(word_count.values())
  most_common_words = sorted([word for word, count in word_count.items() 
  if count == max_word_count - 1])
  month_name = {"01": "January", "02": "February", "03": "March", "04": "April", "06": "June"}
  most_reviews_month = month_name[max(monthly_reviews, key=monthly_reviews.get)]

  print(f"Average Rating: {total_rating}")
  print(f"Most Common Words: {most_common_words}")
  print(f"Month with Most Reviews: {most_reviews_month}")
  
# test the function below
reviews = [
  {"id": 1, "rating": 5, "review": "The coffee was fantastic.", "date": "2022-05-01"},
  {"id": 2, "rating": 4, "review": "Excellent atmosphere. Love the modern design!",
  "date": "2022-05-15"},
  {"id": 3, "rating": 3, "review": "The menu was limited.", "date": "2022-05-20"},
  {"id": 4, "rating": 4, "review": "Highly recommend the caramel latte.", "date": "2022-05-22"},
  {"id": 5, "rating": 4, "review": "The seating outside is a nice touch.", "date": "2022-06-01"},
  {"id": 6, "rating": 5, "review": "It's my go-to coffee place!", "date": "2022-06-07"},
  {"id": 7, "rating": 3, "review": "I found the Wi-Fi to be quite slow.", "date": "2022-06-10"},
  {"id": 8, "rating": 3, "review": "Menu could use more vegan options.", "date": "2022-06-15"},
  {"id": 9, "rating": 4, "review": "Service was slow but the coffee was worth the wait.",
  "date": "2022-06-20"},
  {"id": 10, "rating": 5, "review": "Their pastries are the best.", "date": "2022-06-28"},
  {"id": 11, "rating": 2, "review": "Very noisy during the weekends.", "date": "2022-07-05"},
  {"id": 12, "rating": 5, "review": "Baristas are friendly and skilled.", "date": "2022-07-12"},
  {"id": 13, "rating": 3, "review": "It's a bit pricier than other places in the area.", 
  "date": "2022-07-18"},
  {"id": 14, "rating": 4, "review": "Love their rewards program.", "date": "2022-07-25"},
]

analyze_reviews(reviews)

"""

import string
from collections import Counter, defaultdict
from statistics import mean

STOPWORDS = set(["the", "and", "a", "to", "of", "in", "but", "some", "is", "it", "i", "for", "on", "with", "was"])

MONTH_NAMES = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December"
}

def clean_text(text):
    return text.lower().translate(str.maketrans("", "", string.punctuation)).split()

def process_reviews(reviews):
    total_rating = []
    word_count = Counter()
    monthly_reviews = defaultdict(int)
    
    for review in reviews:
        total_rating.append(review["rating"])
        words = clean_text(review["review"])
        
        for word in words:
            if word not in STOPWORDS:
                word_count[word] += 1
        
        month = review["date"][:7]
        monthly_reviews[month] += 1
    
    return total_rating, word_count, monthly_reviews

def calculate_average_rating(ratings):
    return mean(ratings)

def find_most_common_words(word_count):
    max_word_count = max(word_count.values())
    return [word for word, count in word_count.items() if count == max_word_count]

def find_most_reviews_month(monthly_reviews):
    most_reviews_month = max(monthly_reviews, key=monthly_reviews.get)
    year, month = most_reviews_month.split("-")
    return f"{MONTH_NAMES[month]} {year}"

def analyze_reviews(reviews):
    total_rating, word_count, monthly_reviews = process_reviews(reviews)
    
    avg_rating = calculate_average_rating(total_rating)
    most_common_words = find_most_common_words(word_count)
    most_reviews_month = find_most_reviews_month(monthly_reviews)
    
    print(f"Average Rating: {avg_rating:.1f}")
    print(f"Most Common Words: {most_common_words}")
    print(f"Month with Most Reviews: {most_reviews_month}")

# Test cases for the function
reviews = [
  {"id": 1, "rating": 5, "review": "The coffee was fantastic.", "date": "2022-05-01"},
  {"id": 2, "rating": 4, "review": "Excellent atmosphere. Love the modern design!", "date": "2022-05-15"},
  {"id": 3, "rating": 3, "review": "The menu was limited.", "date": "2022-05-20"},
  {"id": 4, "rating": 4, "review": "Highly recommend the caramel latte.", "date": "2022-05-22"},
  {"id": 5, "rating": 4, "review": "The seating outside is a nice touch.", "date": "2022-06-01"},
  {"id": 6, "rating": 5, "review": "It's my go-to coffee place!", "date": "2022-06-07"},
  {"id": 7, "rating": 3, "review": "I found the Wi-Fi to be quite slow.", "date": "2022-06-10"},
  {"id": 8, "rating": 3, "review": "Menu could use more vegan options.", "date": "2022-06-15"},
  {"id": 9, "rating": 4, "review": "Service was slow but the coffee was worth the wait.", "date": "2022-06-20"},
  {"id": 10, "rating": 5, "review": "Their pastries are the best.", "date": "2022-06-28"},
  {"id": 11, "rating": 2, "review": "Very noisy during the weekends.", "date": "2022-07-05"},
  {"id": 12, "rating": 5, "review": "Baristas are friendly and skilled.", "date": "2022-07-12"},
  {"id": 13, "rating": 3, "review": "It's a bit pricier than other places in the area.", "date": "2022-07-18"},
  {"id": 14, "rating": 4, "review": "Love their rewards program.", "date": "2022-07-25"},
]

analyze_reviews(reviews)
