class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        graph = {}
        for word in wordList:
            graph[word] = []

        graph[beginWord] = []

        def isDifferByOneLetter(wordOne, wordTwo):
            check = False
            for i, c in enumerate(wordOne):
                if c == wordTwo[i]:
                    continue
                if check:
                    return False
                check = True
            return True

        def createGraph(wordList):
            for i, wordOne in enumerate(wordList):
                for wordTwo in wordList[i+1:]:
                    if not isDifferByOneLetter(wordOne, wordTwo):
                        continue

                    if wordTwo not in graph[wordOne]:
                        graph[wordOne].append(wordTwo)

                    if wordOne not in graph[wordTwo]:
                        graph[wordTwo].append(wordOne)

                if isDifferByOneLetter(wordOne, beginWord):
                    if wordOne not in graph[beginWord]:
                        graph[wordOne].append(beginWord)

        createGraph(wordList)
        # for k in graph:
        #     print(k, graph[k])

        if len(graph[endWord]) == 0 or len(graph[endWord])

        q = [(beginWord, 0)]
        while q:
            s, length = q.pop(0)
            if s == endWord:
                return length
            if
        return 0
