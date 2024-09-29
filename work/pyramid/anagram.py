s1=input("enter the string:")
s2=input("enter the string:")
def anagram(s1,s2):
    if len(s1)!=len(s2):
        return "not anagram"
    elif(sorted(s1)==sorted(s2)):
        return"are anagram"
    else:
        return"not anagram"
print(anagram(s1,s2))            


    
