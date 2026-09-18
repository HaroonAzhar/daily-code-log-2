# 443. String Compression
class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0
        while(read < len(chars)):
            current = chars[read]
            c_count = 0
            while( read < len(chars) and chars[read] == current):
                c_count+=1
                read+=1
            chars[write] = current
            write+=1
            if c_count > 1:
                for c in str(c_count):
                    chars[write] = c
                    write +=1
        return write