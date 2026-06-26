class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maching = { ")":"(","]":"[","}":"{"}
        for c in s:
            if c in "([{":
                stack.append(c)

            else:
                if not stack:
                    return False

                top = stack.pop()
                if top != maching[c]:
                    return False

        return len(stack)==0
             