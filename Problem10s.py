# -*- coding: utf-8 -*-
class Problem11:
    def maxArea(self, h):
        maxA=0
        a=0
        b=len(h)-1
        """
        for i in range(len(h)):
            for j in range(i+1,len(h)):
                tp=min(h[i],h[j])*abs(i-j)
                if tp>maxA:
                    maxA=tp
                    a=i
                    b=j
        """
        while a<b:
            maxA=max(maxA,min(h[a],h[b])*abs(a-b))
            if h[a]>=h[b]:
                b=b-1
            else:
                a=a+1
        return maxA
    
#H=[1,3,1]
#T=Solution().maxArea(H)
#print(T)


class Problem12:
    
    def intToRoman(self,Num):
        s=['','I','II','III','IV','V','VI','VII','VIII','IX',
           '','X','XX','XXX','XL','L','LX','LXX','LXXX','XC',
           '','C','CC','CCC','CD','D','DC','DCC','DCCC','CM',
           '','M','MM','MMM','MMMM']
        return s[(Num//1000)+30]+s[(Num//100)%10+20]+s[(Num//10)%10+10]+s[Num%10]

#num=10
#t=Solution().intToRoman(num)
#print(t)# -*- coding: utf-8 -*-


class Problem13:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum = 0
        maxDigit = 1
        for i in range(len(s)-1, -1, -1):
            if digits[s[i]] >= maxDigit:
                maxDigit = digits[s[i]]
                sum += digits[s[i]]
            else:
                sum -= digits[s[i]]

        return sum
        
#s="IV"
#t=Solution().romanToInt(s)
#print(t)

class Problem14:
    def longestCommonPrefix(self, strs):
        if len(strs)==0: return ''
        if len(strs)==1: return strs[0]
        if len(strs)==2:
            t=-1
            for i in range(min(len(strs[0]),len(strs[1]))):
                if strs[0][i]==strs[1][i]:
                    t=i
                else: break
            if t==-1:return ''
            else: return strs[0][0:(t+1)]
        if len(strs)>2:
            st1=self.longestCommonPrefix(strs[:((len(strs))//2)])
            st2=self.longestCommonPrefix(strs[((len(strs))//2):])
            if st1=='' or st2=='': return ''
            else: return self.longestCommonPrefix([st1,st2])
            
#s=["flower","flow","flight"]
#t=Problem14().longestCommonPrefix(s)
#print(t)

class Problem15:
    def threeSum(self, nums):
        nums.sort()
        k=[]
        for i in range(len(nums)-2):
            if i==0 or nums[i]>nums[i-1]:
                left=i+1;right=len(nums)-1
                while left<right:
                    if nums[left]+nums[right]==-nums[i]:
                        k.append([nums[i],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:left +=1
                        while left<right and nums[right]==nums[right-1]:right -=1
                        left +=1;right -=1
                    elif nums[left]+nums[right]<-nums[i]:
                        left +=1
                    elif nums[left]+nums[right]>-nums[i]:
                        right -=1
        return k
    
#s=[-1,0,1,2,-1,-4]
#t=Problem15().threeSum(s)
#print(t)

class Problem16:
    def threeSumClosest(self, nums,target):
        nums.sort()
        close=nums[0]+nums[1]+nums[2]
        diff=abs(close-target)
        for i in range(len(nums)-2):
                left=i+1;right=len(nums)-1
                while left<right:
                    d=nums[left]+nums[right]+nums[i]
                    newdiff=abs(d-target)
                    if diff>newdiff:
                        diff=newdiff
                        close=d
                    if d<target: left +=1
                    else: right -=1
        return close
    
#s=[1,1,1,0]
#t=Problem16().threeSumClosest(s,-100)
#print(t)
        
class Problem17:
    def letterCombinations(self,digits):
        if digits=='':return []
        else:return self.Combine(digits)
    
    def Combine(self,str):
        s=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        k=[]
        if len(str)==1:
            for i in range(len(s[int(str[0])-2])):
                k.append(s[int(str[0])-2][i])
        else:
            t=self.Combine(str[1:])
            for i in range(len(s[int(str[0])-2])):
                for j in range(len(t)):
                    k.append(s[int(str[0])-2][i]+t[j])
        return k
    
#s='234'
#t=Problem17().letterCombinations(s)
#print(t)
        
class Problem18:
    def fourSum(self, nums, target):
        """核心思路：通过递归，每次考虑是否能够达到目标，同时调整对应的目标值
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        :
        """
        nums.sort()
        k=[]
        self.findNsum(nums, target, 4, [] ,k)
        return k
        
    def findNsum(self, nums,target, N, result, results):
        if len(nums)<N or N<2: return
        if N==2:
            l,r=0,len(nums)-1
            while l<r:
                if nums[l]+nums[r]==target:
                    results.append(result+[nums[l],nums[r]])
                    l +=1
                    r -=1
                    while l<r and nums[l]==nums[l-1]:
                        l +=1
                    while l<r and nums[r]==nums[r+1]:
                        r -=1
                elif nums[l]+nums[r]<target:
                    l +=1
                else:
                    r -=1
        else:
            for i in range(0, len(nums)-N+1):
                if target < nums[i]*N or target > nums[-1]*N:
                    break
                if i==0 or (i>0 and nums[i-1]!=nums[i]):
                    self.findNsum(nums[i+1:], target-nums[i], N-1,result+[nums[i]],results)       
        return
        
    
#nums=[-2,-1,0,0,1,2]
#target=0
#t=Problem18().fourSum(nums,target)
#print(t)
 
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
       
class Problem19:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre=head
        end=head
        for _ in range(n):
            end=end.next
        if end == None:
            return head.next
        while end.next != None:
            pre=pre.next
            end=end.next
        pre.next=pre.next.next
        return head
#
#head=ListNode(1)
#a=ListNode(2)
#b=ListNode(3)
#c=ListNode(4)
#d=ListNode(5)
#head.next=a
#a.next=b
#b.next=c
#c.next=d
#t=Problem19().removeNthFromEnd(head,2)
#while t !=None:
#    print(t.val)
#    t=t.next
    
class Problem20:
    def isValid(self,s):
        A='({['
        B=')}]'
        t=[]
        flag=0
        i=0
        for i in range(len(s)):
            a=s[i]
            if len(t)==0:
                t.append(s[i])
            else:
                if B.find(s[i]) <0:
                    t.append(s[i])
                elif A.find(t[len(t)-1])>0 and A.index(t[len(t)-1])==B.index(s[i]):
                    t.pop()
                else:
                    t.append(s[i])
            
            if len(t)>len(s)/2: 
                break
            
        if len(t)==0: flag=1
        return flag
    
#s='[([]])'
#m=Problem20().isValid(s)
#print(m)

#A='[{('
#B=['(']
#print(A.index(B[0]))
#print(A.find('['))
#B.remove('(')
#print(len(B))