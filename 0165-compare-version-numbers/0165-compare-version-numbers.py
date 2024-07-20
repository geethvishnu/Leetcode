class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # s1, s2 = '',''
        # if version1[0]==0:
        #     s1 = int('0')
        # else:
        #     for i in version1:
        #         if (i=='0' and i.index()+1=="1" or i=='.':
        #             pass
        #         else:
        #             s1+=i
        #     print(s1)
        # if version2[0]==0:
        #     s2 = int('0')
        # else:
        #     for i in version2:
        #         if i=='0' or i=='.':
        #             pass
        #         else:
        #             s2+=i
        #     print(s2)
        # if s1<s2:
        #     return -1
        # elif s1>s2:
        #     return 1
        # return 0
        
        m, n = len(version1), len(version2)
        v1 = version1.split('.')
        v2 = version2.split('.')
        while m<n:
            v1.append(0)
            m+=1
        while m>n:
            v2.append(0)
            n+=1

        for i, j in zip(v1, v2):
            if int(i) < int(j):
                return -1
            elif int(i) > int(j):
                return 1

        
        return 0
