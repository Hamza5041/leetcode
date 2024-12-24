class Solution:
    def nearestPalindromic(self, n: str):
        len_n = len(n)

        if 0 < len_n < 2:
            return str(int(n) - 1)

        even = (len_n % 2 == 0)

        i = len_n // 2 if even else len_n // 2 + 1
        firstHalf = n[:i]

        possibilities = []
        incremented = str(int(firstHalf) + 1)
        decremented = str(int(firstHalf) - 1)
        possibilities.append(self.create_palindrome(firstHalf, even))
        possibilities.append(self.create_palindrome(incremented, even))
        possibilities.append(self.create_palindrome(decremented, even))

        possibilities.append(str(10 ** (len_n - 1) - 1))
        possibilities.append(str(10 ** len_n + 1))

        closest = ""
        closestLength = float("inf")
        print(possibilities)
        for pos in possibilities:
            if pos == "":
                continue
            intPos = int(pos)
            difference = abs(intPos - int(n))

            if closestLength > difference > 0:
                closest = pos
                closestLength = difference
            elif difference == closestLength:
                closest = pos if intPos < int(closest) else closest


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
    x = "1001"
    test = Solution()
    print(test.nearestPalindromic(x))

