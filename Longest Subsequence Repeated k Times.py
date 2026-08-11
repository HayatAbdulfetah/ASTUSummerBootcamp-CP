class Solution:
    def longestSubsequenceRepeatedK(self, s, k):
        count = Counter(s)

        chars = []
        for ch in count:
            if count[ch] >= k:
                chars.append(ch)

        chars.sort(reverse=True)

        ans = ""

        def valid(word):
            target = word * k
            j = 0

            for ch in s:
                if j < len(target) and ch == target[j]:
                    j += 1

            return j == len(target)

        def dfs(word):
            nonlocal ans

            if len(word) > len(ans):
                ans = word

            for ch in chars:
                if word.count(ch) < count[ch] // k:
                    new_word = word + ch

                    if valid(new_word):
                        dfs(new_word)

        dfs("")

        return ans
