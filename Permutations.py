# https://leetcode.com/problems/word-search/
board =[
  ['I','F','L','E'],
  ['I','V','K','U'],
  ['O','V','D','E']
]
class Solution():
    def exist(self, board, word):
        array =[]
        notInWord = True
        for a in board:
            for b in a:
                array.append(b)
        for i in word:
            if i in array:
                array.remove(i)
            else:
                notInWord = False



        return notInWord


g =  Solution()
c = g.exist(board,'IION')
print(c)