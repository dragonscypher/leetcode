class Solution:
    def repeatLimitedString(self, s: str, repearlimit: int) -> str:
        bucket=[s.count(chr(ord("z")-i)) for i in range(26)]#z:0 y:1...
        ans=""
        cur=0
        while cur<26:
            if bucket[cur]==0:
                cur+=1
            else:
                if repearlimit>=bucket[cur]:
                    ans+=chr(ord('z')-cur)*bucket[cur]
                    bucket[cur]=0
                    cur+=1
                else:
                    ans+=chr(ord('z')-cur)*repearlimit
                    bucket[cur]-=repearlimit
                    p=cur+1
                    while p<26:
                        if bucket[p]:
                            ans+=chr(ord('z')-p)   
                            bucket[p]-=1
                            break
                        p+=1
                    else:
                        return ans
        return ans
