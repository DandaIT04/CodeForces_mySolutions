# CodeForces_mySolutions
My Solutions for codeforces problems. Hopefully to be ranked in codeforces one day.

Codeforces Profile
(https://codeforces.com/profile/dandarohanibusiness)

# 4A - Watermelon
Solved in 30 minutes. Was not used to how submission for codeforces solutions worked.

# 71A - Way Too Long Words
Solved in 45 minutes. Still not used to code format for submission in code forces using python.

# 231A - Team
Solved in 30 minutes. First input is number of "problem" inputs given. Solution was to convert input into string and use var.count("1") to count number of "1"s in variable and if more than one, means the solution is solvable, where number to return + 1

# 158A - Next Round
Took an hour and a half. Seven submissions. This is because i didn't understand the problem statement. Kth place is the score, means theList[K - 1] is the score. I initially thought score == k. Which was mostly the issue, the rest were small error correction for example, only positive scores count, if score is 0, should not count. I also forgot that i could've used the and operator rather than separating checking if value is zero in an if statement.

Also, i learned that i could use map() function to map inputs as int in the list, while spltting them. theList = list(map(int,input().split()))

# 50A - Domino Pilling
Easiest A category code i have attempted so far. Only required to run once and figure out pattern in input and output.

# 282A - Bit++
startValue = 0. Every x++ is startValue +1 and every x-- is startvalue -1. Simply removed x by using text.replace("x","") then use function if "++" in value, startValue + 1

# 263A - Beautiful Matrix
From 218ms to 92ms, refactored code twice. Mine spans many lines because i thought of putting the puzzles together piece by piece. I could have actually "started" the solution after each input, making it faster, rather than giving my solutions after receiving all the inputs into a matrix.

# 112A - Petya and Strings
I still don't understand what i was supposed to get from this. Changing letters to numbers based on ascii did not pass the 5th test case. I actually had to look at solutions online to find out why i was wrong but they only provided solutions but never clearly stated why mine wouldn't work.

# 339A - Helpful Maths
From Programmiz:
join elements of text with space
print(' '.join(text))

Could have replaced ' ' with '+'. I didn't know i could just join strings this way rather than "1" + "+" + "2" etc

# 281A - Word Capitalization
Could have just done print(word[0].capitalize() + word[1:]). Well learnt something new this problem

# 266A - Stones on the table
The problem felt familiar and immediately the TwoSum solution from leetcode i learned came into my mind and i applied it.

# 236A - Boy Or Girl
Learned to remove duplicates in list by converting list to dict using elements in list as keys. As keys cannot have duplicate values, duplicated values wont be included.

# 791A - Bear and Big Brother
Multiple given inputs twice and thrice respectively. Simple problem with no need of explanation.

# 546A - Soldier And Bananas
Each banana cost banana cost * amount of bananas. Calculate how the amount of money soldier has to borrow from his friend if he has
x value in his wallet.

# 617A - Elephant
Made a few mistakes for example i printed the input rather than the int value 1 and not using math.floor() for input/5 as the
division can return the value as a float value, which affects test case #5

# 59A - Word
Resubmitted my code to make it much faster by removing unnecessary assignment of new list variable

# 977A - Wrong Subtraction
Changed my code back to while loops. By fixing some bugs i have where i decrement and increment values unnecessarily, it works now. From 61ms to 46ms. Much more efficient

# 116A - Tram
Probably be my last submission for now to focus on personal projects
