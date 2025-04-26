class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic={}
        for index,word in enumerate(list2):
            dic[word]=index
        smaller=float('inf')
        result=[]
        for index,word in enumerate(list1):
            if word in dic:
                total=index + dic[word]
                if total < smaller:
                    result = [word]
                    smaller=total
                elif total == smaller:
                    result.append(word)
        return result
