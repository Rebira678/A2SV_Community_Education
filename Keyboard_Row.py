class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row='qwertyuiop'
        second_row='asdfghjkl'
        thrid_row='zxcvbnm'
        container=[]
        for i in words:
            count=0
            l=0
            s=0
            for j in i:
                if j.lower() in first_row:
                    count+=1
                    if count==len(i):
                        container.append(i)
                elif j.lower() in second_row:
                    l+=1
                    if l==len(i):
                        container.append(i)
                elif j.lower() in thrid_row:
                    s+=1
                    if s==len(i):
                        container.append(i)
        return container
 
