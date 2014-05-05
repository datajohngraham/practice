from random import randint
#import module for random integer
top=20
samples=[0] * top
#create a list that includes twenty zeros
for _ in range (1000):
#repeat a loop 1000 times
    samples[round((randint(0, top-1) + randint(0, top-1) + randint(0, top-1))/3)] += 1
#get two random integer between 0 and 19 and take the average.  By the central limit theorem the mean of two random variables is normally distributed.  access the list at that index number and add 1 to the number so it's a count of the number of times that number came up
for num in range(top-1):
#iterate over each index number
    print(num,' ','*' * (samples[num]//10))
#print the index number a space and a star.  repeat the star the number of times that number came up in the list by accessing it by index and divide by ten to read on one line
