
# def myfunc(*args):
#     lst=[]
#     for i in args:
#         if i%2==0:
#             lst.append(i)
#     return(lst)
# print(myfunc(1,2,3,4,5))
# lst=[]
# def myfunction(a):
    

# def myfunc(a):
#     result=""
#     b=range(0,len(a))
#     for i in b:
#         if i%2==0:
#             letter=a[i]
#             letter_upper=letter.upper()
#             result+=letter_upper
#         else:
#             letter=a[i]
#             result+=letter
#     return result
# print(myfunc("hello"))


# a="apple"
# b=a[0]

# print(b.upper())

# a="hello"
# result=""
# b=range(0,len(a))
# for i in b:
#     if i%2==0:
#         letter=a[i]
#         letter_upper=letter.upper()
#         result+=letter_upper
#     else:
#         letter=a[i]
#         result+=letter
# print(result)

#                       **warm UP***
# def lesser_of_two_evens(a,b):
#     if a%2==0 and b%2==0:
#         if a>=b:
#             return(b)
#         else:
#             return(a)
#     else:
#         if a>=b: 
#             return(a)
#         else:
#             return(b)
        
# print(lesser_of_two_evens(3,5))


# def animal_crackers(text):
#     b=text.split()
#     c=b[0][0]
#     d=b[1][0]
#     if c==d:
#         return True
#     else:
#         return False
    

# print(animal_crackers("this treat"))


# def makes_twenty(a,b):
#     if a+b==20:
#         return True
#     if a==20 or b==20:
#         return True
#     else: 
#         return False
# print(makes_twenty(1,20))


#                      LEVEL 1 PROBLEM= OLD MACDONALD 
# def old_macdonald(word):
#     result=""
#     r=range(0, len(word))
#     for i in r:
#         if i==0:
#             c=word[i]
#             result+=c.upper()
#         elif i==3:
#             a=word[i]
#             result+=a.upper()
#         else:
#             f=word[i]
#             result+=f
#     return result
# print(old_macdonald("neymar"))

# def yoda(word):
#     b=word.split()
#     b.reverse()
#     return " ".join(b)
# print(yoda("okay bye now"))

# def almost_there(a):
#     if a>=90 and a<=110:
#         return True
#     elif a>=190 and a<=210:
#         return True 
#     else:
#         return False
# print(almost_there(189))
# ***************         LEVEL 2 PROBLEMS
# def find(a):
#     lst=[]
#     for i in a:
#         b=str(i)
#         lst.append(b)
#     return "33" in "".join(lst)
    
# print(find([1,2,3,34,5,6,3]))


# def doll(a):
#     lst=[]
#     for i in a:
#         lst.append(i*3)
#     return "".join(lst)
# print(doll("Mississippi"))


# def black(a,b,c):
#     lst=[a,b,c]
#     fsum=a+b+c
#     if fsum <= 21:
#         return fsum
#     elif fsum > 21:
#         if 11 in lst:
#             ffsum=fsum-10
#             if ffsum>21:
#                 return "bust"
#             else:
#                 return ffsum
#         else:
#             return "bust"
# print(black(11,11,11))

# def summer(a):
#     lst_i=[]
#     lst_s=[]
#     index_6=a.index(6)
#     index_9=a.index(9)
#     num=0
#     for i in a:
#         b=a.index(i)
#         print(b)
#         if index_6<= b and index_9>=b:
#             lst_i.append(i)
#         else:
#             lst_s.append(i)
#             c=a.pop(i)
#             print(c)
#     for e in lst_s:
#         num+=e
#     print(lst_i)
#     return num
        
# print(summer([1,2,3,6,8,3,2,9,11]))


# def spy(a):
#     index_seven=a.index(7)
#     index_zero=a.index(0)

# print(spy([1,2,3,0,2,0,1,7]))

# def spy(a):
#     lst=[]
#     for i in a:
#         if i==0 or i==7:
#             s=str(i)
#             lst.append(s)
#     lst1="".join(lst)
#     if "007" in lst1:
#         return True
#     else:
#         return False

# print(spy([1,2,3,2,1,0,7,0,1,7]))

# def prime(a):
#     for i in a:
    


# print(a(range(1,100)))
# lst=[]
# lst2=[]
# for i in range(2,101):
#     if i%2!=0:
#         lst.append(i)
#         if i%3!=0:
#             lst2.append(i)
# print(lst)

# print(lst2)

# def prime(num):
#     if num<2:
#         return 0
#     primes=[2]
#     x=3
#     while x<=num:
#         for y in range(3,x,2):
#             if x%y==0:
#                 x+=2
#                 break
#         else:
#             primes.append(x)
#             x+=2
#     print(primes)
#     return len(primes)

# print(prime(100))

# def lesser(a,b):
#     if a%2==0 and b%2==0:
#         return min(a,b)
#     else:
#         return max(a,b)

# print(lesser(2,3))

# def word(a):
#     words=a.lower().split()
#     return words[0][0]==words[1][0]
# print(word("hello hat"))

# def num(a,b):
#     return (a+b)==20 or a==20 or b==20
# print(num(20,0))
###########
###########
# def stringt(a,b):
#     return a*b
# print(stringt("hi", 2))

# def front(a, b):
#     return a[0:3]*b

# print(front("he", 2))

# def string(a):
#     return str[0::2]
# print(string("hello"))

# def expo(a):
#     b=range(1,len(a)+1)
#     c=""
#     for i in b:
#         c+=a[0:i] 
#     return(c)
# print(expo("hello"))

# https://codingbat.com/prob/p145834


# def count(a):
#     lst1=[]
#     for i in a:
#         strlst=str(i)
#         lst1.append(strlst)
#     return "123" in "".join(lst1)
# print(count([1,2,4,3,4,9,7,8,1,2,7,3,5]))

# lst=[1,2,3,4,5,6,7]
# lst1=[]
# for i in lst:
#     strlst=str(i)
#     lst1.append(strlst)
# print("".join(lst1))

# def array(a):
#     for i in range(0, len(a)-2):
#         if a[i]==1 and a[i+1]==2 and a[i+2]==3:
#             return True
# print(array([1,2,3,4,5,6]))
            

# def word(a):
#     first=a[0]
#     second=a[1:3]
#     fourth=a[3]
#     rest=a[4:]
#     return first.upper()+second+fourth.upper()+rest

# print(word("mcdo"))

# def num(a):
#     n=10
#     return a>=(100-n) and a<=(100+n) or a<=(200+n) and a>=(200-n)

# print(num(109))



# def num(a):
#     r=range(0,len(a))
#     for i in r:
#         if a[i]==3:
#             if a[i+1]==3:
#                 return True
#             else:
#                 continue
#         else:
#             return False
        



# print(num([1,3,34,3,]))

# lst=[1,2,3,3,4,5,6]
# print(lst.count(3))

# def r(a):
#     lst=[]
#     for i in a:
#         lst.append(str(i))
#     return "123" in "".join(lst)

# print(r([1,2,3,4,1,2]))
# def string(a,b):
#     r1=range(0, len(a)-1)
#     num=0
#     lst=[]
#     lst2=[]
#     for i in r1:
#         lst.append(a[i])
#         lst.append(a[i+1])
#         # print(lst)
#         if "".join(lst) in b:
#             num+=1
#             if "".join(lst) in "".join(lst2) and num>1:
#                 num=num-1
#             lst2.append(a[i])
#             lst2.append(a[i+1])
#             # print(num)
#             del lst[0:]
#             # print(lst2)
#         else:
#             del lst[0:]
#     return num
# print(string("aabbccdd","abbbxxd"))

# def string_match(a, b):
#   # Figure which string is shorter.
#   shorter = min(len(a), len(b))
#   count = 0
#   # Loop i over every substring starting spot.
#   # Use length-1 here, so can use char str[i+1] in the loop
#   for i in range(shorter-1):
#     a_sub = a[i:i+2]
#     b_sub = b[i:i+2]
#     if a_sub == b_sub:
#       count = count + 1
#   return count
# print(string_match("aabbccdd","abbbxxd"))

# def word(a):
#     return "hello {b}".format(b=a)
# print(word("bob"))


# def word(a,b):
#     return a+b+b+a
# print(word("hi", "bye"))




#############
# lst=["a","b","c","d"]
# for i in range(0,len(lst)):
#     print(lst[i])
# k=len(lst)
# while k>0:
#     print(str(len(lst)) + " - " + str(k) + "=" + str(len(lst) - k ) )
#     print(lst[len(lst) - k ])
#     k-=1
    # k+=1
    #########################


