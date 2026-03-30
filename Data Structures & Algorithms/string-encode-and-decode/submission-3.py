class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]: 
        print(s)
        if s == "":
            return []
        res = []
        i = 0
        while i < len(s):
            if s[i].isdecimal() and s[i+1] == '#':
                res.append(s[i+2:i+2+int(s[i])])
                i = i+2+int(s[i])
            elif s[i:i+2].isdecimal() and s[i+2] == '#':
                res.append(s[i+3:i+3+int(s[i:i+2])])
                i = i+3+int(s[i:i+2])
            elif s[i:i+3].isdecimal() and s[i+3] == '#':
                res.append(s[i+4:i+4+int(s[i:i+3])])
                i = i+4+int(s[i:i+3])               
            else:
                i += 1
        return res
