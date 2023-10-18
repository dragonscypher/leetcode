class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        c=set()

        for email in emails:
            a=email.split('@')
            a[0]=a[0].replace(".",'')
            a[0] = a[0].split('+')[0]
            if a[1].count('.') >= 1:
                c.add(str(a))
        return len(c)
