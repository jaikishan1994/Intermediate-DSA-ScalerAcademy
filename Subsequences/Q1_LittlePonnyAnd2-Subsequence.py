#
# Created on Wed Apr 20 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Little Ponny has been given a string A, and he wants to find out the lexicographically minimum subsequence
 from it of size >= 2. Can you help him?
A string a is lexicographically smaller than string b, if the first different letter in a and b is
 smaller in a. For example, "abc" is lexicographically smaller than "acc" because the first different
  letter is 'b' and 'c' which is smaller in "abc".
 
Problem Constraints
    1 <= |A| <= 105
    A only contains lowercase alphabets.

Input Format
    The first and the only argument of input contains the string, A.

Output Format
    Return a string representing the answer.

Example Input
Input 1:
    A = "abcdsfhjagj" 
Input 2:
    A = "ksdjgha" 

Example Output
Output 1:
    "aa" 
Output 2:
    "da" 

Example Explanation
Explanation 1:
     "aa" is the lexicographically minimum subsequence from A. 
Explanation 2:
     "da" is the lexicographically minimum subsequence from A. 
'''
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)

        #find the first minimum char in the input string; assign it to m1 and its index to m1_index
        m1 = 'z'
        m1_index = n
        for i in range(n):
            if(A[i] < m1):
                m1 = A[i]
                m1_index = i
        
        #find the second min char
            #1. from (m1_index to n-1] or 
            #2. from [0 to m1_index)

        m2 = 'z'
        m2_index = n
        if m1_index == n-1: #1. from (m1_index to n-1]
            for i in range(n-1):
                if(A[i] < m2):
                    m2 = A[i]
                    m2_index = i
        else: #2. from [0 to m1_index)
            for i in range(m1_index+1,n):
                if(A[i] < m2):
                    m2 = A[i]
                    m2_index = i
        
        #if the first element(m1) is found at index i < second element(m2) found at index j
            #then it can form a subseqence m1+m2 because i<j and m2+m1 subsequnce is not possible
        if(m2_index > m1_index):
            return m1+m2
        #otherwise it is m2 + m1
        else:
            #print("handle: ", A)
            #print(m1, m1_index, m2, m2_index)
            return m2+m1

s = Solution()
#test cases: 

A = "scsecugqsb" #cb
ans = s.solve(A)
assert ans == 'cb'

A = "yyjyyyrrjrjyyyxjyrxxryyryxjyyxxxjrrrrjyjyyjrjyyxxrxyrxxjryyxjrjrrxjyyyrrjxxjyryxxryxxjyyyxxyxxxyxxrrxyxrrrxjyyrxxjxjryjyjjxxxryjrjrjxyjrryxxxrjyjyjyjrxjyyjxxrxjyjrxrxyrjjjjxxxxxxxxyxjyryxxjjjjxyxrjxyjrryryxyyyjjjyjrxxjyxjyyrjjjyryjjyxyyjyjxrxrrjrxrjjjxxrjyrxryjrjrjyyjrrjyxyyjrxrrjrrxjxrxrxjxjjjyxjjrrrxyyrjxryyrjjjyxryxjjyyyjjxxjyjjjrjyxrjryrrrjyrjjyrrxjjxyyxyjrjjxjryjrjyyyjjrjxxjxjyrjyrjxjjrxrjrjxxyxjrxjyyjxyrxjrjrxjyyrrjjyyrjjxrxrrjrrrxrryrjrjxxyrxxrjryyxjryxjrrxjxxjyxjxyxrrxxjxjxrxjjjyjyyxjrxjxxyjyyyxxrrxyrxjjjyxryyxjjyjrxxxryjryxxjyxjxrjrryxryyrrryxjyxxyrxjjjryxyyjyrrxyxrxrjxrxxxjryxryxxrryjrryyyxrjrxrxjrjyxyjjrjyxxjxryxyjxyrryxjrrrrxjxjxxyjjrxyyxjyyxyyyrxxyyjxxrxyjyrrjjjrjjyjxjyxryyyrjyjjjxjjyxxryxxxxrjryrrrrjryyxjryryjyrxjryjxyxxxyxyjjyyjrrxjxyyrrjjxxrrxyjrrryjyjxxyxyyrjjxxxryjryjjxrjyxrrxyyyyyyyjyyxxxrrrjrrxxyyyyjyrjrxrjyxrrxxxyjryrryrxxxrjjjrryjrxyxrjjrjjrxxyjjryyjxjryxjyjjrryjxryyxyjyxrxyxjrryyyjrrjrjyjjrrxryyrxrrxryjxxjxjyxyjjyjxyjryjrjrxyjyjyxyyryyjjyrxyxxjrjxjyrryyjxyxjryrjxryjjxjyrryjyxxyjxxjxjjrjxjjrxrjjjjjrrrxjxrxryyyyjjjxxxryrrjxyryrryrrjrxjjjrryxxxjjyjjjyxyjyxyyjyjxrrjjyrxxyxxrxyxrjyrjryrrryyyxrrrjjjryrjjyjxxyxxyyyyjyjxrjjyyyyyxjyrxyyyjjyrxxjrrxjrrxxyrxxxjjyrryyxyxjxjyrxrxyyryxyjjrjjjrjjrryyjryrxjxjyrrrxjryryryxyrjyyyyjyxyrxjyrrryyjjyrrxrjrxjrrxjrjjjyrxryjyrryjjxrrxjrjxyyyryryxryyrrjxxxrjyyjjryxyxxxxrrxjxjyryjrrxxxrjrjxxxrxrjjyyyjjjyryjyyrjrjjrjxyrrjyrxjjyjrjrxxxrryjrjyyjjryyxxyrrrxrrjrjxrryjyrxyrxrxjryrxxyyyjryyrxrjrxryjjjyxxyryyryrxxjrxjrxjxyyyyjyxrxjxjxyyxyyyyxyyjyrryrryjxxyrrjjyjxryxjxrjjjyryxjjxjjyyyxyrrryyryyryyjxxjjyyyrjjyjjyjyxrjjjjjyryjrjxxyxyyjxyjxryjrrjyrxjryjyjjjjyyjyrjjjjrxyjrxryrxxjjxjyjjrrrjxrrjyyxyrxjxyxyrxjyrryryrrrxrrjyyxxyjxjjryrjxxyjrjyyjrxxrrjyjryyjjxxxrrxyyxyyrrryjyryxrxjxryrjyrrrrxjjjxyyjxjyrxxxyyryjyjjxjryjyrjxjrrjjyrxjjyyrrrrryjryxyjxyxxxyxxjrjrxyxyjrjjjxyrjxryjyjxryyjjjrryyjyyxyyjjjyyjjjjrxyxxxjjrxjyxryyjyrrrjjyxyrjxrxyrjjjjrrxrryxyrxxyrxrrrjyxyrjyxjxryxjryyjrrryyxjyryxjryjxrrxxxxjxxxyrrxyyyxrjxxrxyjjryrjyxjrjrxjjryryrryrjxyxyxjyjrjxrjrxrrxjjryrxxryrxxyryjyrjrrjyrjxjrryryxrjrryrjjjrrryryjxyryrrjxxjyxyxrjjyyyrrjjxxjjjyrjyyyyyryrjrxjjxxrrjxxryxxyyrxjxxjjyryjjjxxryjjrjyyxxxjxxxxyxjyjyyyyxxjjxxxjjrjyrjxxjjxyxjyyyyxjyrrjxyyjjxyjyyjjxxxjjrxrjxxxrjjrjrxxyyjxjrxjjrrryyjryyjjjxyxrjrrrryryxyjjryrxxjjyyxjryrxjyryjyyyyxxjyyyxxrjrrxyjjxyjrjjrryxryjxrrxxyxryjrxjyxxryxjyrxjxxxxrjjrrxxjryyryyryrrrjyjjjxjryrrrjxyyyryjjyyxrrrjyrrrjjjxxxyxjyyxjxjjyjxyrjyyxjrjxjrxyxyxryxxrjrryxrrjjrryrrjxrjrxryjxxjxxryxxxxyyxrxxjyjrrjjjrxyxryxjjxyjjjxrxxxyjryrrxxyxjxjyyjrrrjryyyyjjrxyjyrxrrxxrjyjrxjjyyjjryryrxyyjjjyyjjjyyrrjjjrrjrrxrxxyjrjyjjjyyyjyxrjxrryrryxjryxxyjyjyjjxyjyyjjrxrrjrryxxjjrrrjxjyyryjrxxyyxyjxxrrxjrxjrxxjrxrrjjxrxyxjjyxjxxrxxjryyryjxjrjxrxrrryjxrxyrrjyxrxxjyjrxjjxyjyxjjjjxjyjxjjjryjyjrxjjxxyxxryrxryrjxxjjyrjxxrxxrjrxxrryrjxxrjryrxjjxxrryrrjjxyjxrjrjryyrxxxyyryryxrrrxxxjyxjxjxyrjryrrrjjjyyxxjrxyyyryxxxyxyrxyrjryjxxjjyyryxxyjyryxxyyxyxyxrxxyjjjjrjjyjxyyyrjxjyyyrxrxxjxjrjjrxyyyjjxyrrxrjxjrjxyyjjjyxyxyyrrjjxrxrxryjyrjyyryyrxyxryryxryxjrjxxjryxjyjjyxrxyrxyjyxxxyyjjrxyxjryjyrxjryryyjxxyxxxjxxyrrrjjrxrjrxjjyrjjxxyyxyjyxxxjjyrjxrjxjjyxyyyjjxyryyryjryjjjjjxrxrrryjjjxyjxryxxjjyjrxyjyyrjxyjyrjyxyxxxxyrxyxryxjrxjrxxyjxxryjryyryxyrjjrxryjrjyxxxxjrjyxryryrxjyjjxjjryyyyxjxxxxrjyxrryrjrxrxyyrrxjyrxyyrrrxyjyxxryyjjrjxxxxrryxyryjjyjryxrrxjyxrjjyjjjjyxxjrjjxxyxxxryrjrjyjyyrjyryxjxryjjyyrxjyyrxrxjjjyryjjjjjrxrxjjyxyxyyyjjyjyrjrxxyjyrjyxyxyxjxjjrjyyxrrrjxryryxryyxrrrrxjxyrxjjrjxyrrjxxxxyrjjxrjxyjyjjyyrxrjxryyxyxxyyxxjxxrjryyxjjxjxyxyjyyrxjjryryrrjrjyyryjryjyxyrryrjyxrryjyxyxryxrxryrxrryjxjyrxxyyrjxxrxrjjxxrxxyxxjjjxyyyryrxjjxxxjrrrrjjjrrrrrjxyxyxjyjyxyryjyjjjryrxjxrrxrjyyrjrjyyyxxrryjxjryrrxyrjyryrrrxyryyyjyxryjjyjxxyjrjrrxrxrjyyjyxrrjxrrxxjyrxjrjxyyjyxyyjryyrjxryyxrjyrxjxyyxjxryrrjxyjjyjxxxyxrjyrjryjyyryyjxjyjxyyrxyrrjryxjjxxjjjjxyyxjxjrxxxyrjyyyjrrxyxyyjrxyjyxyyyryxrryyxryyxryrjyyxyjyyrxyyrxyxyyjjyryyyyjjxrjxrrxrrrxryyyyryryjxyjryxjyyyrxxxjyjjrjxrjyjrrjryyyjxjjrrjrxryrjrxyjyyrxjxyxyrxxjxyryrxryxjyrjxyjxrjxjxjjryyrryryryrxxyjyyrrrryxyxyjjrxxxyxjxjyxrjxyxjyjjjyxyjjxyrjyrjyryyjjjryjjjyyxrxyyjrrjxyjjjyyyxxryxyyyjxxjxyxyxryjryjxryxxxjrxyyrjryxyrrryrryyxrjxyryjyyxyrrxxjrrrryrxyxxyjrryyxxyyrjxrjxyyxrxryxxjjryrjrjyrrjjjjrjyrxxrjxjyyyrrxxxyjjxjjryyyxjyrjrrjjxjyyjyxjyrjxyyxryyyrrxxryyjrjjyjyyrrjjxryyxjyxxyxyyyxxxjxrryjxrxyrxrjjrjyjjrjjxjrrxyryyxxyrxjjjrxyjjyjyyjxrjxxxrrryyrxxjyrrxrryrryrjrxxxyrjrrrrxjyrjrrjyjrxryxjxxrryjxryyyyrxjxryryjjryjyyyjryyxxxryxxjyxjrxjrjyjjrjxyyxjxxjxrjjxjjryrxxxjyryyyyjyrjyyryyjyrjrjryyyjxryrrxyxjyyyyjyyyjryryyxjxrjrxrryyjjjxxxxrxjyryjyjxyjrrjjjxjxyrxryxrxxjxyyrrrjxxryrxjrxrxyxyyrjyjxyxjrjrrrxyrrjjjjrrxrjyyxjxjryjrryjjjxryrxxrjyrrjjyyjjyjjjyjrjyrxryxyyjjrjrjxrxxyxrjjrrrjxxyjryyxxxjxyjrxrxyyjxxjyyyjxxjyrrrjrryryxyxjrrrrjryxrjryxyrrrjjrrryxyyrjjrxryxyrrrxrjrrxjxryxyxxxjrjxjxrjryjxrrjjyyyjxjjjxxrrrxryrjxrxxyyryjrjrrxyrryyjrxxxrjyjryyjyyjxxjjxxjjyryjxyyyxyrxxyyjyrxrxjxrrrryxrrxrryjjjyyyjyjxrjrjjjrxjyxyjjjjjjrxxyxxjxrxyyjyjyyyjrrxxjyrrrrjyyrxxxrxxrxyxrxyxjyryrjxyyyxjrjryjjyryxjrxxjrrrrjyryjyryjjxjjxyjrxxrryyyjyyjjrxxyrxrrjyyjrxyyxyjjjjjjjyjrjrxxyjrrrrxyjrryjxrrjyxyjyrxrxyxxyxxyjjyyxyryryrrrxyxrjjyjjrjrxxxryjrrjjxyryrxjyxyryxyrjrxrxxjyxxxjxrrxjyrjjryrxxyyrjxrjxjjyrrjrjrrxjrxrxrjyjyxjxyjjxjjrryxyyjyyyrxrxjyxjyyrjryyyjxxxjrjrxyjrrxyjrjjjrjxjjyyryrryrrxjrryrrxjjxyxjyrxxjryyxxyjxyrrxxxxxxrjyxxyjrjxjxxxyrjxrjrxrjyyjrxrxxyxxxrxxrxyjyryxrjrjxxjyjyjxrxjyryjjrxjxyjrjjxxjjjjjyyyryyryxrxrryrjrjxyxxryjyrrxxyyxrjyxxrryyyjjrrjryryryyxxrxjxrryxyyrxxjjjjyxrjyjxxrjyxxyyyjxrxxxjxyrjjxjjxxyryjyrjrrjxxxjxrjxjryxjxyjrjrrrjjxrjrrjjyjrxyrjrjrrrrrxjjxjxxxxxjjxjyrjjyjrxyxyjxrryjyxrxxyjyyjxryyxyxrryyjrxxryjyxjrxxjxrjrrxxyrrryrrjjxrjjjyyjxxxjjxyrrxrjyyyyyrjxryrrrxrjjxyyjxxryxxjyrxjrrjjjjxxyxryyxjjxrxrjrjryrrxjxjyjxrxrrjryxrjyxjjryrjjyyyxyyjryyrjjxyyjxxxjyyxyrjrjyyrrxrxxjjyxjyyrjyrjyjjrrjjxjyjxrxxyjyjxyxjxjyyxjjyyjjjjyxyrrjjrrxrxxjjjyrjxxrrjjjxrryjjrxjyjxxjjxxxyryjjjyxrrxjyjjxyjyxyxxxjxyjjrjxxrjrjyxjjyjjxxjxrrrxyrxyjjyryxryrjyxxxxxyjjxxxjxyyxrryrjjxxrryrxrrjyryjrrxrryxjryyjryxxjrrjjyyjyjjxyyxxryjjrrxjyjyjryjxyxjxrrxxrrjrjjryyxyyrrxxxryxxjyxxxyxjjxyxjyrxxxyjjyrxxxyyxjxxryjyjjjxjyjjjxjxyrxyxyrrxyyryjjxyxrxrxxjyxrrrxxyjrrrjxyrjrrjyxjyyjjjyryyrxjyyrjjrrxxxyrjrrrjyryryjxjjyxxxrrrxyyyjjyxryrrrrxxxryxxrrrryrjjyryxxjjrjxjyjryyjryrjjyrjjxjjyxjryrxyyrxrrjyjrxxyyyxjxrrrjxxrrrrrxxyxjyyjyjxrryrjyjxjrrrrjjyyyrjrrjjrrxxrxjyxryryjyrrjxxjjjjryrxrjxrjjyyjjrryryyrjjjrrjxxjjxyryxyxyyxryyxxrrjyyjjjrryjyyrjryxxxjyxyrjyrxxryjrxyyjjxrrxxjjxrxrjxyyrjjjyrrxrjrrjrxryyrrxryrjjjjxrryyjyjjryxyyrxyrrxxyxyyjjyjxxryjrrjyxjxxrxryrjyyjryjjxxjrryjyrryxrjxryyxyyxxxjxxrrrxjrrryyxxryxxxjxxjrrjxyjxyyjjjxxrxyjxyjjxjyxryyjyryrryxyyyxryjyyrxxryyxxjjjrxjyyxrjrrxxyyrrrjjrjyxjjjxxrjyyrxyjjjrxjxryxyrrxrjryyrxyxyxryryyyjryrxyxjrrrryjjrjyyxjjjryrxxxxryyryjrjjyjryrjyxxrryjjrxxrryjyxyyxxxjjyjxjjxyryjyyyrxxyjjxxyryyxyjxrryyyjjryjyjxyjjrrjjrrxjyxrrjrrxjjrxyyjjjjyyjjxrrxjrxyjryyyxxxyyrrjxyyyrxjxyryryxjxrrrxjrxjrjjrjrxxryrjxxyrxryrjjxjjrxjryjrrjxjjyrjxjyyryrjyrrryxyxxjxyrjrjxxxyyxjjrxxjjxyjjjxyxjxyxxryjrrxjyjyjyjxyrjyxryxyrxxjyjyjrxyrrryxyxyryxyxyjryxjyyrjjrjrrrxjxjyyrjxjyxyxrryyrryrryjjjjyrrxrrryxjrjrrjjxyjyjrxryjyrrjjxrjryyrrxrxrxjjxyxrxxjrjjjjryjjyyrrjrjyyyxyxrrjxjrxxrxrxrjxyrjxrjyjrxjxxrxxxxryrxyyryjryyxjrxxxxjrryrxyjyjjxrrxxxxryjyxjjjjxxjjryxxjryxyryyrxyxjyyxyrrxyxrxrjrjjrjrjrjrjryyryrjxyjyjyyxjyjjjyxrxrjjjryyxryxryryjxjyrjrxjxxjxrrryryyxyyjxrxyryyjyjrryrrrjjjxrxxjxjryyxjjxrryyrrjxrxxxyrxyxxxjyjrxyxjjrjyxrrxxyrjyyyjjxjyjrxrryrrrrrjrrjjjxrxxjjyrxjxyyjryxxryjjyryyrryyjjjxyryjrxyyjxyrjyyyyxxyyyyxryrjrryrrxrxrjyxyjrjyryyyryryrjxrryxyyxrjxjyjxjxxryrryyxyxjrjjxjyyxrxxjxrxyjxxxrryxyyjyxxxxyxxxjyrxyjxjrrjyxryyyrjrxyxxrjyyrxjyjxxxyjjryjrxyrjxxjrrxyyrxyyrrjjyyrrxxjyxyxrxrxrxjrjxxxxyxxrrjxryxjjyyjrjryjryrxyxxyyyxryrrjryrjjyryjyyyxxryyyjjjxyrxyyxjrjxrjxrjyxxxxjxxxryjxryjjyjrxyxyrrxxjyxxjyrxrjyrjxxyyxrjyxyxjyrjyjrrjrxjyyjjrjjjxjyjyjjjxyjxjjxxjxyyxxyjyxyryjxrxryxyjxxrrjjrxxjxjxyxjjyjjyyrxyjjyrrjjyjyxjjrxjjrrxjyxyjxyrxxyxrrryrxxxyrryryryxjyyjjxjjryxrrxjryrjyrjyxjryyxxyxyyjxyyxxyjrjjyyxrxryyxxjryyyxrxrxjyjyxjryxxyryyxjjxyxyrrxxxjyjryxjjxyrxjryrjjjyxxrxyrrxjyyyrjxrxjrxyxyjrjrjjjjryyxxyyxjxxjjxxjjxrrjxyrxrjrrxryxxxxrrxyyyxxjxjyyyjyrrryyyyxrrrrrxjyrxyyyjyryxxjyxryyxjxrrxryxrjxryjrjxxjrxxrjrxrxrxrjxrrxyxryjyjxyyjrxyyryxyrxjxrrjrjjxrrxjjjyyxrxyxrjyjyxxrjrxyjxjrjyryxxjrjjjxjxrxjjxrjxrryyxjrxrrryjyyjrryxrryjxrjxrxyryrjjrrxjyxrxxyrjjyyrjjyyryxrjrryyjjjjrrjxxrjrryjrxyrjjjjxrjrxxyxxrjrrxjyyrryxrrrrxjjjjjjjyjjjjjxjrryryrrryyjrrrxjxjyyjyjxrjyxxryxxrrxrxrrrjyrrxyyjyrxjxjjxryjxxyjxjyjyyryjyjxxyjxjxxxyyjjrxrxjrxrxxyxrrxyyjrrjryryrrxyryjryrxyjrjrjrjjyxrjjrjrrjryryryyryjyyyrrjrjxjyryxjxjyxjyjjjyryrxryjryrxxyrjxjjyjjxjrrrryxjryjryjyrjyxyrjjxxyyxyrryyxjryrxxjrjxjryyxyyyjjyyjxyjjyrrjrrjxxxyrrjjjyjrxyxxxyxyjxrjjryryxrrjryxxyryrrxrxyyyyyrxxyrxryyyxjjrxxrrxyjjjxxjyxjryryyrrxrjjyyjrxxyjxxyjjxyyjyjxryjxjrjjxyrxyrjxxjrxxryyxxjxyjrrjjjjxrxrxxjxxrxrjryrxjrxxrrjrrxrxyyxjxjyyxyjjjyxrrxjjryyjryyxjxyjyjjyjyjxxyjyyrrxrrrjrxrxjyxryyrxjrrrjrjxjyxxyryjxyyryjxxrjyrjrxjrrrjxyxyjxrryrxjrjyrrrxjyjxyrxjxyrjjyxrrryxyyyjyrxrjrjxryrrrryryyxrrryjrrxjxxjrxjryjyyrjxxxjyxyxxyxrjjjjrjxxrxjjryryrrxxjyrxyrxyyryxxxxxjjrrrxxyjrxjxyxjjjxyrrxrjyjxjjxjyyjyxrjxrryyrjrjjxyyjxxyjjrxyrjyjjxxrrjrrxxjyxjryrrxjyjjyrrryxxxxrjxjxxxyxjrjxrjxxyjxrrjrjjyjyrjjrxyxrjjrjyxjrxyxjjjxjryyjxjxjryxyxrxrrxryxrjyxjxjxxyxrxjyyjjyjyjxrrxyxxxxrxjjyyyxryxryyxjxrryjyyyryjxjxyjyrjjryjyxjrxrjjyxxjyrjjyxrjxxxjxryrjjjxrjxrxjxxxyyxjyrjyxxrryyrxjxxryyryjxxxryrjjyrrxxxyjjjrjyyyyxxyyxjxyyjxyxrxyxyrrryyxjjxrrxxxjxyjyrrjxjrjyxrjyxyxrjxjjrjxrjxjryyjjxrxrxjxjjjrrxjxrrxrrxjjrrrxyrxxryyyjxyxyjyrjxrrjxyyrjxjyryjyjyyyyyyjyryxyyxyjyyyryjyyjxxyxxyyryxyryxrryxjrxyyjyrxyjxjrxyjxryyrryyxrjxyjxyjjyyxxrxjyyrjjxxjryyrjrjjjyjyjjyryjxyjyxxjyjryyxyrjxxyxjyjyyyxjxxxyxrrryyrryyxrrxxxyjyxjjjxxrjryjyxryxrxyjxrryxxjrjxjxjxjjjjyryjyjyxjxxjryxyxrrrrrrjyrjxjryxyxyyyyyyxjrxrxyxxxyyjjyjxxjjxjryyyrxxjyjyyxyyyxxjxryjrxjrrxrjjrryxjrxrrrrrrxjyxxjxyjxyjjyjrjrjyrrxyxryjyjyyxjryxrjyrrxjxrryrxjjyjyyjxyjyyjyxxrrxrxrxyyjyxyyjxxjxrryyxrjryxjxjryxxrxxyxjjyyrxryrjrxrjryyxyrxxyxxjyyrxxxjrjjrjryjyxrrjxjrxrryrrrxrjyrxjxb" #jb
ans = s.solve(A)
assert ans == 'jb'

A = "abcdsfhjagj" #aa
ans = s.solve(A)
assert ans == 'aa'

A = "ksdjgha" #da
ans = s.solve(A)
assert ans == 'da'

A = "djjhibvetj" #be
ans = s.solve(A)
assert ans == 'be'
