class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]    ##Stack plus hash map, TC (O(n)), SC (stack + hashmap) (O(n))+ (O(1))
        pairs={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        
        for parentheses in s:
            if parentheses in pairs:
                if not stack or stack.pop() !=pairs[parentheses]:
                    return False
            else:
                stack.append(parentheses)
        return not stack