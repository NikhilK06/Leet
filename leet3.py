class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    Nik = 0
    count = Counter()

    l = 0
    for r, c in enumerate(s):
      count[c] += 1
      while count[c] > 1:
        count[s[l]] -= 1
        l += 1
      Nik = max(Nik, r - l + 1)

    return Nik
