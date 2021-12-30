# CodeForces_mySolutions
My Solutions for codeforces problems

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
