# Make out word
# def make_word(out, word):
#     lt_inserted=out[:2],word,out[2:]
#     return "".join(lt_inserted)
# print(make_word("<<>>","hello"))
# --------------------------------------------
# Extra End
# def extra_end(str):
#     h_=str[::-1]
#     h__=h_[:2:]
#     return h__[::-1]*3
# print(extra_end("nothing"))
# ---------------------------------------------
# First two
# def first_two(str):
#     return str[:2:]
# print(first_two("h"))
# -----------------------------------------------
# first_half
# def first_half(str):
#     lenstr=len(str)
#     len_str=lenstr/2
#     return str[:len_str:]
# print(first_half('HelloThere'))
# -------------------------------------------------
#                   Without string
# def without_end(str):
#     str_1=str[1::]
#     str_2=str_1[::-1]
#     str_3=str_2[1::]
#     return str_3[::-1]
# print(without_end("hello"))
# 
# -----------------------------------------------------
#                     Combo_string
# def combo_string(a, b):
#     if len(a)<len(b):
#         string=a,b,a
#         return "".join(string)
#     else:
#         string=b,a,b
#         return "".join(string)
# print(combo_string("hi",""))
# -----------------------------------------------------
#                       Non-start
# def non_start(a, b):
#     string=a[1::],b[1::]
#     return "".join(string)
# print(non_start("hello","there"))
# -----------------------------------------------------
#                           Left 2
# def left2(str):
#     first=str[:2:]
#     second=str[2::]
#     string=second,first
#     return "".join(string)
# print(left2("hello"))
#-----------------------------------------------
#                       first_last6
# def first_last6(nums):
#     return nums[0]==6 or nums[-1]==6
    # if nums[0]==6 or nums[-1]==6:
    #     return True
    # else:
    #     return False
# print(first_last6([1,2,3,4,6]))
# -------------------------------------------------------------
#                   same_first_last
# def func(nums):
#     return len(nums)>=1 and nums[0]==nums[-1]
# print(func([1,2,3,4,1]))
# -------------------------------------------------------------
#                       Make_pi
# def func():
    # return [3,1,4]
    #     OR
    # pi=[3,1,4]
    # return pi
# print(func())
# -------------------------------------------------------------------
#                       common_end
# def func(a,b):
#     return a[1]==b[1] or a[-1]==b[-1]
# print(func([1,2,3],[2,3,4]))
# --------------------------------------------------------------------
#                   Sum 3
# def func(nums):
#     return sum(nums)
# print(func([1,2,3]))
# ---------------------------------------------------------------------
#                   rotate_left3
# def func(nums):
#     a=(nums[1],nums[-1],nums[0])
#     return list(a)
# print(func([1,2,3]))
# ---------------------------------------------------------------
#                               Reverse3
# def func(nums):
#     return nums[::-1]
# print(func([1,2,3]))
# ---------------------------------------------------------------
#                               max_end3
# def func(nums):
#     boolean=nums[0]>nums[-1]
#     if boolean==False:
#         return [nums[-1]]*3
#     else:
#         return [nums[0]]*3
# print(func([4,2,3]))
# ---------------------------------------------------------------
#                               Sum2
# def f(nums):
#     if len(nums)>=1:
#         return nums[0]
#     else:
#         return nums[0]+nums[1]
# print(f([5]))
# ---------------------------------------------------------------
#                               Sum2
# def f(a, b):
#     num=a[1],b[1]
#     return list(num)
# print(f([1,2,3],[1,3,2]))
# # ---------------------------------------------------------------
#                               make_ends
# def f(nums):
#     num=nums[0],nums[-1]
#     return list(num)
# print(f([1,2,3])) 
# ---------------------------------------------------------------
#                               Has23
# def f(nums):
#     return 2 in nums or 3 in nums
# print(f([1]))
# ---------------------------------------------------------------
#                               Logic
#                           cigar_party
# def cigar_party(cigar_party, is_weekend):
    # if is_weekend==False:
    #     return cigar_party>=40 and cigar_party<=60
    # if is_weekend==True:
    #     return cigar_party>=40
# print(cigar_party(39,True))
# ---------------------------------------------------------------
# #                           Date_Fashion
# def f(you, date):
    # if you<=2 or date<=2:
    #     return 0
    # if you>=8 or date>=8:
    #     return 2
    # else:
    #     return 1
# print(f(7,5))
# --------------------------------------------------------------
#                           Squirrel_play
# def f(temp, is_summer):
    # if is_summer and 60<=temp<=100:
    #     return True
    # if 60<=temp<=90:
    #     return True
    # else:
    #     return False
# print(f(99,False))
# --------------------------------------------------------------
#                           caught_speeding
# def f(speed, is_birthday):
    # if is_birthday:
    #     if speed<=65:
    #         return 0
    #     if 66<=speed<=85:
    #         return 1
    #     else:
    #         return 2
    # else:
    #     if speed<=60:
    #         return 0
    #     if 61<=speed<=80:
    #         return 1
    #     else:
    #         return 2
# print(f(64,True))
# --------------------------------------------------------------
#                           Sorta_sum
# def f(a, b):
#     if 10<=a+b<=19:
#         return 20
#     else:
#         return a+b
# print(f(10,9))
# --------------------------------------------------------------
#                           alarm_clock
# def f(day, vacation):
#     if vacation:
#         if 1<=day<=5:
#             return '10:00'
#         else:
#             return 'off'
#     else:
#         if 1<=day<=5:
#             return '7:00'
#         else:
#             return '10:00'
# print(f(1, False))
# --------------------------------------------------------------
#                           Love6
# def f(a, b):
#     if a+b==6 or abs(a-b)==6 or 6 in (a,b):
#         return True
#     else:
#         return False
# print(f(1,7))
# --------------------------------------------------------------
#                           in1to10
# def f(n, outside_mode):
#     if outside_mode:
#         return not 1<n<10
#     else:
#         return 1<=n<=10
    
# print(f(1,False))
# --------------------------------------------------------------
#                              Near_ten
# def f(num):
#     a=num%10
#     return 0<=a<=2 or 8<=a<=10
# print(f(3))
# --------------------------------------------------------------
#                       String-2
#                     Double_Char
# def f(str):
#     string=[]
#     for i in str:
#         string.append(i*2)
#     stringf="".join(string)
#     return stringf
# print(f("hello-there"))
#                   OR
# def f(str):
#     string=""
#     for i in str:
#         string+=i*2
#     return string
# print(f("hello-there"))
# ------------------------------------------------------------
#                           Count_hi
# def f(s):
#     s+=" "
#     num=0
#     for i in range(0, len(s)):
#         if s[i]=="h" and s[i+1]=="i":
#             num+=1
#     return num
# print(f("hksjkdhi, hello hi hihi"))
#                   Or
# def f(s):
#     num=0
#     for i in range(len(s)-1):
#         if s[i:i+2]=="hi":
#         # if s[i]+s[i+1]=="hi":
#             num+=1
#     return num
# print(f("hksjkdhi, hello hi hihi"))
# ------------------------------------------------------------
#                           Cat_Dog
# def f(str_1):
#     cat_num=0
#     dog_num=0
#     for i in range(len(str_1)-2):
#         if str_1[i:i+3]=="cat":
#             cat_num+=1
#         if str_1[i:i+3]=="dog":
#             dog_num+=1
#     return cat_num==dog_num
# print(f('catdog'))
# ------------------------------------------------------------
#                           Count_code
# def f(str_1):
#     num=0
#     for i in range(len(str_1)-3):
#         if str_1[i:i+2]=="co" and str_1[i+3]=="e":
#             num+=1
#     return num
# print(f("helliicoie"))
# ------------------------------------------------------------
#                               end_other
# def f(a,b):
#     for i in range(len(a)):
#         if a[i+(len(a)-len(b)):i+(len(a))].lower()==b.lower():
#             return True
#     for i in range(len(b)):
#         if b[i+(len(b)-len(a)):i+(len(b))].lower()==a.lower():
#             return True
#     else:
#         return False
# print(f("dkjlabc",'abc'))
# l="hello"
# print(l[3:1])
# -------------------------------------------------------------
#                           xyz_there
# def f(s):
#     for i in range(0,len(s)):
#         if s[i:i+3]=="xyz" and s[i-1]!=".":
#             return True
#     else:
#             return False
# print(f("asdsdjkxyz"))
# -------------------------------------------------------------
#                        List-2
#                      Count evens
# def f(nums):
#     num=0
#     for i in nums:
#         if i%2==0:
#             num+=1
#     return num
# print(f([1,2,3,4,5]))
# -------------------------------------------------------------
#                       Bif_diff
# def f(nums):
#     small_num=nums[0]
#     big_num=0
#     for i in nums:
#         if i>big_num:
#             big_num=i
#         if i<small_num:
#             small_num=i
#     return big_num-small_num
# print(f([1,2,3,4,5,6]))
# -------------------------------------------------------------
#                  Centered_average
# def f(nums):
#     max_number=max(nums)
#     min_number=min(nums)
#     return (sum(nums)-max_number-min_number)/(len(nums)-2)
# print(f([1,2,3,4,5,6,7]))
#                   Or
# def f(nums):
#     max_number=nums[0]
#     min_number=nums[0]
#     for i in nums:
#         if i>max_number:
#             max_number=i
#         if i<min_number:
#             min_number=i
#     return (sum(nums)-max_number-min_number)/(len(nums)-2)
# print(f([1,2,3,4,5,6,7]))
# -------------------------------------------------------------
#                       sums 13
# def f(nums):
#     index_number=len(nums)
#     lst=[]
#     for i in range(len(nums)):
#         if nums[i]==13:
#             index_number=i
#             continue
#         if index_number+1==i:
#             continue
#         else:
#             lst.append(nums[i])
#     return sum(lst)
# print(f([1,13,1,2,3,4,5]))
# -------------------------------------------------------------
#                       sum67
# def f(nums):
#     six_index=0
#     seven_index=0
#     key=True
#     lst=[]
#     for i in range(len(nums)):  
#         if nums[i]==6:
#             six_index=i
#             key=False
#         if nums[i-1]==7:
#             seven_index=i
#             if six_index<seven_index:
#                 key=True
#         if key==True:
#             lst.append(nums[i])
#     return sum(lst)
# print(f([1,2,3,5,6,5,7,7]))

# -------------------------------------------------------------
#                               has 22
# def f(nums):
#     for i in range(len(nums)-1):
#         if nums[i]==2 and nums[i+1]==2:
#             return True
#     return False
# print(f([1,2,1,2,1,2,3,4,1,]))
# -----------------------------------------------------------
#                           LOGIC 2
#                       Make Bricks
# def make_bricks(small, big, goal):
#     if goal>(big*5)+(small):
#         return False
#     if goal%5>small:
#         return False
#     else:
#         return True
# print(make_bricks(8, 4, 23))
    

# -------------------------------------------------------------
#                           Lone sum
# def lone_sum(a,b,c):
#     lst=[a,b,c]
#     if a!=b!=c and a!=c!=b:
#         return a+b+c
#     if a==b==c:
#         return 0
#     else:
#         a_count=lst.count(a)
#         b_count=lst.count(b)
#         if a_count>b_count:
#             return b
#         if a_count==b_count:
#             return c
#         else:
#             return a
# print(lone_sum(3,3,3))

#                       OR

# def lone_sum(a,b,c):
#     num=0
#     if a!=b and a!=c:
#         num+=a
#     if b!=a and b!=c:
#         num+=b
#     if c!=b and c!=a:
#         num+=c
#     return num
# print(lone_sum(1,2,2))
# --------------------------------------------------------
#                   Lucky sum
# def luckey_sum(a,b,c):
#     if a==13:
#         return 0
#     if b==13:
#         return a
#     if c==13:
#         return a+b
#     else:
#         return a+b+c
# print(luckey_sum(1,13,3))
# --------------------------------------------------
#               no_teen_sum
# def no_teen_sum(a,b,c):
#     lst=[a,b,c]
#     num=0
#     for i in lst:
#         if i<13 or 19<i or i==15 or i==16:
#             num+=i
#         if 13<=i<=14 or 17<=i<=19:
#             pass
#     return num
# print(no_teen_sum(1,14,3))

#               OR

# def fix_teen(n):
#     if 13<=n<=14 or 17<=n<=19:
#         return 0
#     else:
#         return n
# def no_teen_sum(a,b,c):
#     return fix_teen(a)+fix_teen(b)+fix_teen(c)
# print(no_teen_sum(1,2,14))
# -----------------------------------------------------
#              Round sum
# def round_sum(a, b ,c):
#     num=0
#     numa=a%10
#     if numa>=5:
#         missing_a=10-numa
#         final_a=a+missing_a
#         num+=final_a
#     else:
#         final_a=a-numa
#         num+=final_a
#     numb=b%10
#     if numb>=5:
#         missing_b=10-numb
#         final_b=b+missing_b
#         num+=final_b
#     else:
#         final_b=b-numb
#         num+=final_b
#     numc=c%10
#     if numc>=5:
#         missing_c=10-numc
#         final_c=c+missing_c
#         num+=final_c
#     else:
#         final_c=c-numc
#         num+=final_c
#     return num
# print(round_sum(7,2,3))


#               Or


# def num10(num):
#     mod=num%10
#     numf=num-mod
#     if mod>=5:
#         numf=numf+10
#     return numf
# def round_sum(a, b, c):
#     return num10(a)+num10(b)+num10(c)
# print(round_sum(14,16,12))
# -----------------------------------------------------
#                       Close Far
# def close_far(a, b, c):
#     ab=a-b
#     ac=a-c
#     bc=b-c
#     if abs(ab)<=1 and abs(ac)>1 and abs(bc)>1:
#         return True
#     if abs(ac)<=1 and abs(ab)>1 and abs(bc)>1:
#         return True
#     else:
#         return False
# print(close_far(1,2,10))
# ----------------------------------------------------
#                           Make Chocolate
# def make_chocolate(small, big, goal):
#     if goal>(big*5)+small:
#         return -1
#     if goal%5>small:
#         return -1
#     else:
#         if (goal)-(big*5)>4:
#             return (goal)-(big*5)
#         else:
#             return goal%5
# print(make_chocolate(6,1,10))


