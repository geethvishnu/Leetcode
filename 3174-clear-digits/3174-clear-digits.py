class Solution:
    def clearDigits(self, s: str) -> str:
        # sub_str=""
        # if len(s)<=1:
        #     return s
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

        