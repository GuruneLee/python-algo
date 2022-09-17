# Palindrome Pairs
from typing import List
from collections import Counter

## Failed 01 - Time Limit Exceeded
class Solution_Failed_01:
    def __init__(self):
        self.palin_string = set()
    def isPalindrome(self, s):
        if s in self.palin_string:
            return True
        n = len(s)
        for i in range(n//2):
            if s[i]!=s[n-i-1]:
                return False
        self.palin_string.add(s)
        return True
    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        ans = []
        for i in range(n):
            for j in range(i+1,n):
                if self.isPalindrome(words[i]+words[j]):
                    ans.append([i,j])
                if self.isPalindrome(words[j]+words[i]):
                    ans.append([j,i])
        return ans

## Failed 02 - Time Limit Exceeded
class Solution_Failed_02:
    def isPalindrome(self, s):
        n = len(s)
        for i in range(n//2):
            if s[i]!=s[n-i-1]:
                return False
        return True
    
    def getAllFixWithPalinAccross(self, s):
        n = len(s)
        prefix = []
        suffix = []
        for i in range(n+1):
            if self.isPalindrome(s[i:]):
                prefix.append(s[:i])
            if self.isPalindrome(s[:i]):
                suffix.append(s[i:])
        return (prefix, suffix)
    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        word_idx = {}
        for i in range(n):
            word_idx[words[i]] = i
        
        ans = set()
        for i in range(n):
            pre, suf = self.getAllFixWithPalinAccross(words[i])
            for p in pre:
                if p[::-1] in word_idx and i!=word_idx[p[::-1]]:
                    ans.add((i, word_idx[p[::-1]]))
            for s in suf:
                if s[::-1] in word_idx and i!=word_idx[s[::-1]]:
                    ans.add((word_idx[s[::-1]], i))
        
        return ans

## Success
class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]
    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        word_idx = {}
        for i in range(n):
            word_idx[words[i]] = i
        
        ans = set()
        for i in range(n):
            word = words[i]
            for j in range(len(word)+1):
                pre = word[:j]
                suf = word[j:]
                if self.isPalindrome(pre):
                    re_suf = suf[::-1]
                    if re_suf in word_idx and i!=word_idx[re_suf]:
                        ans.add((word_idx[re_suf], i))
                if self.isPalindrome(suf):
                    re_pre = pre[::-1]
                    if re_pre in word_idx and i!=word_idx[re_pre]:
                        ans.add((i,word_idx[re_pre]))
        return ans