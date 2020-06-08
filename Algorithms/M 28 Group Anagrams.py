"""
Group Anagrams
Anagrams: words that are made of same set of characters eg: [tac,cat]
"""


# O(w*n*log(n) + n*w*log(w)) time / O(wn) space
def groupAnagrams(words):
    if len(words) == 0:
        return []
    sortedWords = ["".join(sorted(w)) for w in words]
    indices = [i for i in range(len(words))]
    indices.sort(key=lambda x: sortedWords[x])

    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]
    for index in indices:
        word = words[index]
        sortedWord = sortedWords[index]
        if sortedWord == currentAnagram:
            currentAnagramGroup.append(word)
            continue
        result.append(currentAnagramGroup)
        currentAnagramGroup = [word]
        currentAnagram = sortedWord

    result.append(currentAnagramGroup)

    return result

# Faster solution
# O(w*n*log(n)) / O(wn) space
def groupAnagrams(words):
    anagrams={}
    for word in words:
        sortedWord="".join(sorted(word))
        anagrams[sortedWord]=anagrams.get(sortedWord,[])+[word]
    return list(anagrams.values())
