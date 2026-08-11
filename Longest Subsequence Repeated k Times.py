from collections import Counter

        count = Counter(s)

        # Characters that can appear at least once
        chars = []

        for ch in count:
            if count[ch] >= k:
                chars.append(ch)

        # Try larger characters first
        chars.sort(reverse=True)

        # Maximum possible length of answer
        max_len = 0

        for ch in chars:
            max_len += count[ch] // k

        ans = ""

        def check(sub):
            target = sub * k
            j = 0

            for ch in s:
                if j < len(target) and ch == target[j]:
                    j += 1

            return j == len(target)

        def dfs(cur):
            nonlocal ans

            # Update answer
            if len(cur) > len(ans):
                ans = cur
            elif len(cur) == len(ans) and cur > ans:
                ans = cur

            if len(cur) == max_len:
                return

            for ch in chars:
                # We cannot use this character more than count[ch] // k
                if cur.count(ch) < count[ch] // k:
                    new_cur = cur + ch

                    if check(new_cur):
                        dfs(new_cur)

        dfs("")

        return ans
