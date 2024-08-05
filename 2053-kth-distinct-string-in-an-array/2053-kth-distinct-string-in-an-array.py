class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        n=len(arr)
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        print(d)
        lst=[]
        for i,j in d.items():
            if j==1:
                lst.append(i)
        print(lst)
        m=len(lst)
        if m<k:
            return ""
        if n==m:
            return arr[k-1]
        else:
            return lst[k-1]

        