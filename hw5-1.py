# author: LM (AMDG) 10/22/21
import random
# Question 1
print(random.randrange(31, 50))
# Question 2
print(random.randrange(2, 75, 2))
# Question 3
print(random.randint(20, 30))
# Question 4
print(random.randrange(1, 13))
# Question 5
print(random.randrange(1, 21))
# Question 6
print(random.choice(['cat', 'dog', 'sheep', 'cow', 'chicken', 'pig']))
# Question 7
print(random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=1))
# Question 8
print(random.choices([1, 2, 3, 4, 5], k=5))
# question 9
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,52] 
random.shuffle(cards)
print(cards)
# question 10
random.seed(1942)
print(random.randrange(1, 1001))