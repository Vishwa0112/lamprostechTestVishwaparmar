def binary_search(sub,num):
    l,r=0,len(sub) -1
    while l<r:
        mid=(l+r)//2
        if sub[mid]<num:
            l = mid + 1
        else:
            r=mid
    return l

def longest_subseq(arr):
    if not arr:
        return []
    # stores elements of lis
    sub=[]
    for num in arr:
        if not sub or num>sub[-1]:
            # appends if element is larger
            sub.append(num)
        else:
            idx=binary_search(sub,num)
            sub[idx]=num
    return sub

arr=[10,22,9,33,5,44]
print(longest_subseq(arr))