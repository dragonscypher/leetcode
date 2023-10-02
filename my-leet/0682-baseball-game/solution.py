class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = []

        for i in operations:
            if i == 'C':
                x.pop()
            elif i == 'D':
                a = x[-1]
                x.append(a * 2)
            elif i == '+':
                a = x[-1]
                x.append(x[-2] + a)
            else:
                x.append(int(i))

        return sum(x)



