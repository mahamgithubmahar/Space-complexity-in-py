#these activities are not for an actual output and are only used for understanding purposes

def recur(n):
    if (n<=0):
        return #returns nothing
    print("Codingal") #to do else, u dont necessarily have to write "else" if u just indent outside of if statements, python will automatically understand that its an else statement
    recur(n/2)
    recur(n/2)

recur(10)