class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        # If endWord is not even in the dictionary, there is no valid transformation
        if endWord not in wordSet:
            return 0

        # BFS queue: (current word, steps so far)
        q = deque()
        q.append((beginWord, 1))

        while q:
            word, steps = q.popleft()

            # If we've reached the target word, return the path length
            if word == endWord:
                return steps

            # Try all one-letter transformations
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[i]:
                        continue

                    newWord = word[:i] + ch + word[i + 1:]

                    # If newWord is a valid next word, visit it
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        q.append((newWord, steps + 1))

        # No transformation sequence found
        return 0