class Solution:
    def nearestPalindromic(self, n: str):
        len_n = len(n)
        even = (len_n % 2 == 0)

        i = (len_n // 2) - 1 if even else len_n // 2

        possibilities = []
        # Ensure `create_palindrome` is correctly implemented
        possibilities.append(self.create_palindrome(n[:i], even))
        possibilities.append(self.create_palindrome(n[:i - 1], even))
        possibilities.append(self.create_palindrome(n[:i + 1], even))

        closest = ""
        closestLength = float("inf")
        for pos in possibilities:
            if pos == "":
                continue
            intPos = int(pos)
            difference = abs(intPos - int(n))

            if difference < closestLength:
                closest = pos
                closestLength = difference

        if closest == n:
            return str(int(closest) - 1)
        return closest

    def create_palindrome(self, first_half: str, even: bool) -> str:
        """
        Create a palindrome by mirroring the first half.
        """
        if even:
            return first_half + first_half[::-1]
        else:
            return first_half + first_half[-2::-1]



if __name__ == '__main__':
    x = "1"
    test = Solution()
    print(test.nearestPalindromic(x))

