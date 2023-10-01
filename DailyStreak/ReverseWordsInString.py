def reverseWords(s: str) -> str:
    return " ".join(map(lambda word: word[::-1], s.split()))

print(reverseWords(s="Let's take LeetCode contest"))
print(reverseWords(s="God Ding"))