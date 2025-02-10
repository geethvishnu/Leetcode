class Solution:
    def clearDigits(self, s: str) -> str:
        sub_str=""
        for i in range(len(s)):
            if s[i].isdigit():
                sub_str=sub_str[:-1]
            else:
                sub_str+=s[i]
        return sub_str
        


        st=[]
        for i in range(len(s)):
            if s[i].isdigit():
                # s[i]=""
                st.pop()
                pass
            else:
                st.append(s[i])

            # sub_str+=s[i-1]
        return "".join(st)

        