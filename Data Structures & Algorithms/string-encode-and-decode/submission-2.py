class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            n = len(s)
            encoded_str += str(n)
            encoded_str += '#'
            encoded_str += s
        
        return encoded_str
        
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        s_size = len(s)

        i = 0
        while i < s_size:
            len_segm = s[i]
            
            while i + 1 < s_size and s[i + 1] != '#':
                len_segm += s[i + 1]
                i += 1
            
            int_len_segm = int(len_segm)
            segm = s[i + 2 : i + int_len_segm + 2]
            decoded_strs.append(segm)
            i += int_len_segm + 2

        return decoded_strs