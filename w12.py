from typing import List
 
def lcs(str1: str, str2: str) -> str:
    subsequences1 = generate_subsequences(str1)
    subsequences2 = generate_subsequences(str2)
    lcs = ""
    for subsequence1 in subsequences1:
        for subsequence2 in subsequences2:
            if subsequence1 == subsequence2 and len(subsequence1) > len(lcs):
                lcs = subsequence1
    return lcs
 
def generate_subsequences(s: str) -> List[str]:
    subsequences = []
    generate_subsequences_helper(s, "", 0, subsequences)
    return subsequences
 
def generate_subsequences_helper(s: str, subsequence: str, index: int, subsequences: List[str]) -> None:
    if index == len(s):
        subsequences.append(subsequence)
        return
    generate_subsequences_helper(s, subsequence, index + 1, subsequences)
    generate_subsequences_helper(s, subsequence + s[index], index + 1, subsequences)

entries = []
for i in range(100):
    entry = input()
    if len(entry) == 0:
        break
    entry_parts = entry.split()
    if len(entry_parts) != 2:
        break
    entries.append((entry_parts[0], entry_parts[1]))
for entry in entries:
    len1 = len(lcs(entry[0], entry[1]))
    reversed_string = entry[1][::-1]
    print(reversed_string)
    len2 = len(lcs(entry[0], reversed_string))
    # print(len2)
    print(max(len1 , len2))
