inp=input('Please enter a string \n')
alphabet=set(inp) 
#converting the string to a set to get the alphabets 
out_put={} 
#creating an empty dictionay to save the output
c=0 
#using a counter to count occurance

for _ in alphabet:
    for i in inp:
        
        if i==_:  
        #using if condition to check in the element in the given string is same as that is the output set.
            c=c+1 
            #if the condition is true the counter increments
    out_put[_]=c  
    #the value of the counter after traversing the entire input string is saved as a value for the key value pair where key if the alphabet
    c=0 
    #the counter becomes zero so the previous value would not be considered for the next iteration
print(out_put) #the output is printed

