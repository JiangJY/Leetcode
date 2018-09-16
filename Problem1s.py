# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 00:10:24 2018

@author: Jiang
"""

class Problem1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums=nums
        self.target=target
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]
                
"""
2. Add Two Numbers
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Problem2:        
    def List2Num(self,l1):
        num=0
        curr=1
        while l1!=None:
            num=num+l1.val*curr;
            curr=curr*10
            l1=l1.next
        return num
    
    def Num2List(self,num):
        l=ListNode(-1)
        first=l
        if(num<10):
            l.val=num
        else:
            while num//10!=0:
                t=num%10
                p=ListNode(t)
                if l.next==None and l.val==-1:
                    l.val=p.val
                else:
                    l.next=p
                    l=l.next
                num=num//10
            l.next=ListNode(num)
        return first
    
    def addTwoNumbers(self, l1, l2):
        a=self.List2Num(l1)+self.List2Num(l2)
        b=self.Num2List(a)
        return b

#l1=ListNode(2)
#l1.next=ListNode(4)
#l1.next.next=ListNode(3)
#l2=ListNode(5)
#l2.next=ListNode(6)
#l2.next.next=ListNode(4)
#l=Solution().addTwoNumbers(l1,l2)
#print(l.val)
#print(l.next.val)
#print(l.next.next.val)

# -*- coding: utf-8 -*-

class Problem3:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max=0
        flag=0
        for i in range(len(s)):
            if max==0:
                max=1
            if flag==0:
                flag=1
                tp=s[i]
            for j in range(i+1,len(s)):
                if tp.find(s[j])==-1:
                    tp=tp+s[j]
                    flag=flag+1
                    if flag>max:
                        max=flag
                else:
                    flag=0
                    break
        return max

#s='pwwkew'
#print(Solution().lengthOfLongestSubstring(s))
        
class Problem4:
    def findKth(self, num1,num2,k):
        l1=len(num1)
        l2=len(num2)
        if l1>l2:
            return self.findKth(num2,num1,k)
        if l1==0:
            return num2[k-1]
        if k==1:
            return min(num1[0],num2[0])
        pa=min(k//2,l1)
        pb=k-pa
        if num1[pa-1]<=num2[pb-1]:
            return self.findKth(num1[pa:],num2,pb)
        else:
            return self.findKth(num1,num2[pb:],pa)
            
        
    def findMedianSortedArrays(self, nums1, nums2):
        a=len(nums1)+len(nums2)
        if a%2==1:
            return self.findKth(nums1,nums2,(a+1)//2)
        else:
            return (self.findKth(nums1,nums2,a//2+1)+self.findKth(nums1,nums2,a//2))/2
                    
#a=[1]
#b=[]
#t=Solution().findMedianSortedArrays(a,b)
#print(t)
            
        
# -*- coding: utf-8 -*-

class Problem5:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=len(s)
        M=[[0 for col in range(l)] for row in range(l)] 
        a=0
        b=0
        maxN=0
        for leng in range(l):
            for i in range(l):
                if leng==0:
                    M[i][i]=1
                    if maxN<1:
                        a=i
                        b=i
                        maxN=1
                elif leng==1:
                    if i+leng<l:
                        if s[i]==s[i+1]:
                            M[i][i+1]=1
                            if maxN<2:
                                a=i
                                b=i+leng
                                maxN=2                        
                        else:
                            M[i][i+1]=0
                else:
                    if i+leng<l:
                        if s[i]==s[i+leng]:
                            M[i][i+leng]=M[i+1][i+leng-1]&1
                            if M[i][i+leng]==1:
                                if maxN<leng+1:
                                    a=i
                                    b=i+leng
                                    maxN=leng+1
                        else:
                            M[i][i+leng]=0
                    else:
                        break
        return s[a:(b+1)]

#s='cbbd'
#print(Solution().longestPalindrome(s))
 


# -*- coding1: utf-8 -*-
class Problem6:
    def convert(self,S, k):
        l=len(S)
        if l==0: return ""
        if l==1 or k==1 or l<=k: return S
        recu=l//(2*k-2)
        b=l-recu*(2*k-2)
        r=0
        if b==0:
            r=(k-1)*recu
        elif b>0 and b<=k:
            r=(k-1)*recu+1
        else:
            r=(k-1)*recu+1+b-k
        M=[[0 for col in range(k)] for row in range(r)]
        for j in range(recu):
            for t in range(k):
                M[(k-1)*j][t]=1+j*(2*k-2)+t
            for t in range(k,2*k-2):
                M[(k-1)*j+t-k+1][2*k-t-2]=j*(2*k-2)+t+1
        if b>0 and b<=k:
            for t in range(b):
                M[(k-1)*recu][t]=1+recu*(2*k-2)+t
        if b>k:
            for t in range(k):
                M[(k-1)*recu][t]=1+recu*(2*k-2)+t
            for t in range(k,b):
                M[(k-1)*recu+t-k+1][2*k-t-2]=recu*(2*k-2)+t+1
        N=self.transpose(M)
        newString=''
        for i in range(len(N)):
            for j in range(len(N[0])):
                if N[i][j]!=0:
                    newString=newString+S[N[i][j]-1]
        return newString
    
    def transpose(self, M):
        r=len(M)
        c=len(M[0])
        N=[[0 for col in range(r)] for row in range(c)]
        for i in range(c):
            for j in range(r):
                N[i][j]=M[j][i]
        return N

#s='abcde'
#k=4
#t=Solution().convert(s,k)
#print(t)
        
# -*- coding: utf-8 -*-
"""
数值在2**32-1和-2**32/2之间
"""
class Problem7:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0: return 0
        elif x<0:
            return -1*self.trans(-x)
        else:
            return self.trans(x)
        
    def trans(self, x):
        if x>2**31-1: return 0
        if x%10==0:
            return self.trans(x//10)
        else:
            s=[]
            while x//10!=0:
                tp=x%10
                s.append(tp)
                x=x//10
            s.append(x)
            p=0
            for i in range(len(s)):
                p=p*10+s[i]
            if p>2**31-1: return 0
            else:return p

#x=1563847412
#t=Solution().reverse(x)
#print(t)
#print(math.pow(2,31))
            

# -*- coding: utf-8 -*-
class Problem8:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str)==0: return 0
        while str[0]==' ':
            if len(str)>1:
                str=str[1:]
            else:
                return 0
        ind=0
        flag=0
        if str[0]=='-':
            if len(str)>1:
                ind=-1
                str=str[1:]
                flag=flag+1
            else:
                return 0
        if str[0]=='+':
            if len(str)>1:
                ind=1
                str=str[1:]
                flag=flag+1
            else:
                return 0
        if flag>=2:return 0
        p=0
        i=0
        while str[0]=='0':
            if ind!=0:
                return 0
            else:
                str=str[1:]
        while i<len(str):
            if str[i]>='0' and str[i]<='9':
                p=p*10+int(str[i])
            else:
                break
            i=i+1
        if ind==0:ind=1
        if ind==1 and p>2147483647: return 2147483647
        elif ind==-1 and p>2147483648: return -1*2147483648
        else: return ind*p
        
#010--->10
#   +0 123--->0
#   +004500--->4500
#123  456->123
        
#str="123 456"
#t=Solution().myAtoi(str)
#print(t)
        
        
# -*- coding: utf-8 -*-
class Problem9:
    def isPalindrome(self,s):
        """
        :type x: int
        :rtype: bool
        """
        if s<0:
            return False
        elif s>=0 and s<9:
            return True
        else:
            if s%10==0:
                return False
            else:
                l=1
                a=s
                while a//10!=0:
                    l=l+1
                    a=a//10
                a=s
                b=0
                t=0
                while (abs(a-b*10)>10 or a!=b) and t<l//2:
                    b=b*10+a%10
                    a=a//10
                    t=t+1
                if l%2==0 and a==b: return True
                elif l%2==1 and abs(a-b*10)<=9 and abs(a-b*10)>=0:
                    if a//10==b:
                        return True
                    else:
                        return False
                else: return False

#t=101
#p=Solution().isPalindrome(t)
#print(p)
                
                
class Problem10:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """  
        sLen = len(s)
        pLen = len(p)
        if (pLen == 0):
            return sLen == 0
        if (pLen == 1):
            if (p == s) or ((p == '.') and (len(s) == 1)):
                return True
            else:
                return False
        #p的最后一个字符不是'*'也不是'.'且不出现在s里，p跟s肯定不匹配  
        if (p[-1] != '*') and (p[-1] != '.') and (p[-1] not in s):
            return False
        if (p[1] != '*'):
            if (len(s) > 0) and ((p[0]==s[0]) or (p[0]=='.')):
                return self.isMatch(s[1:],p[1:])
            return False
        else:  
            while (len(s) > 0) and ((p[0]==s[0]) or (p[0]=='.')):
                if (self.isMatch(s,p[2:])):return True#牛逼的操作
                s = s[1:]  
            return self.isMatch(s,p[2:])  


"""
mississippi//mis*is*p*.||abcd//d*||abcd//d*||aaba//ab*a*c*a
aaa//a*a||aa//a*||aaa//ab*a*c*a||aab//c*a*b
"""
#s='aaa'
#p='a*a'
#tt=Solution().isMatch(s,p)
#print(tt)
