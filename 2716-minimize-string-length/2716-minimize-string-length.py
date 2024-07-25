class Solution:
    def minimizedStringLength(self, s: str) -> int:
        st=set()
        for i in s:
            if i not in st:
                st.add(i)
        return len(st)
        