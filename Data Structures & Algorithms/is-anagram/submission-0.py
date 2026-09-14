class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp_one = sorted(s)
        temp_two = sorted(t)

        if temp_one == temp_two:
            return True
        else:
            return False
        