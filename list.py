"""Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list."""

if __name__ == '__main__':
    N = int(input())
    result=[]
    for i in range (N):
        x=input().split()
        if x[0]=="insert":
            result.insert(int(x[1]),int(x[2]))
        elif x[0]=="append":
            result.append(int(x[1]))
        elif x[0]=="remove":
            result.remove(int(x[1]))
        elif x[0]=="print":
            print(result)
        elif x[0]=="sort":
            result.sort()
        elif x[0]=="pop":
            result.pop()
        else:
            result.reverse()
