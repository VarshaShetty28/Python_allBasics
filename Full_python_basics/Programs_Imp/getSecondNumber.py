# Program to g=find second largest number 
# input -> pgm -> 2nd largest 
# we need a array with elements so we will find fidt largest and 
# need to find second largest which is larger than other ements and 
# smaller than the max elment
#we can do sort and find the second largest elemnet easily but some will tell dont use the sort 
def getLargestSecondNumberV1(num):
    F_Largest = S_Leargest = num[0]
    for val in num:
        if val > F_Largest:
            S_Leargest = F_Largest
            F_Largest = val
        elif val > S_Leargest and S_Leargest != F_Largest:
            S_Leargest = val
        elif F_Largest == S_Leargest and val < F_Largest:
            S_Leargest = val
    return S_Leargest

# simplest for by using fload('-inf) as thelowedt value in integer

def getLargestSecondNumberV2(num):
    F_Largest = S_Leargest = float('-inf')
    for val in num:
        if val > F_Largest:
            S_Leargest = F_Largest
            F_Largest = val
        elif val > S_Leargest:
            S_Leargest = val
    return S_Leargest

num1 = [-1,-2,-3,-4,-5]
num2 = [6,1,7,9,2,3,4,5,8]
res1 = getLargestSecondNumberV1(num1)
res2 = getLargestSecondNumberV1(num2)
res12 = getLargestSecondNumberV2(num1)
res22 = getLargestSecondNumberV2(num2)
print("Second Largest V1:", res1)
print("Second Largest V1:", res2)
print("Second Largest V2:", res12)
print("Second Largest V2:", res22)


# 3 6 2 5 4 1
# ans = 5
# fl = 3
# sl = 3
# i=6
# i > fl:
#     sl = fl
#     fl = i
#     i++
# if not t his condition here sl(second largest ) will be 3)
# i > f2 and f1!= f2:
#     f2 = i4
# | val | F\_Largest | S\_Leargest | Reason                                  |
# | --- | ---------- | ----------- | --------------------------------------- |
# | -1  | -1         | -1          | First value                             |
# | -2  | -1         | -2          | Third `elif`: F==S and -2 < -1 → S = -2 |
# | -3  | -1         | -2          | -3 < S → no update                      |
# | -4  | -1         | -2          | same                                    |
# | -5  | -1         | -2          | same                                    |
