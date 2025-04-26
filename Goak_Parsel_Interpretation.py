class Solution:
    def interpret(self, command: str) -> str:
        container=[]
        i=0
        for _ in range(len(command)):
            if command[i]=="G":
                container.append("G")
                i+=1
            elif command[i]=="(" and command[i+1]==")":
                container.append("o")
                i+=2
            elif command[i]=="(" and command[i+1]=="a":
                container.append("al")
                i+=4
            if i==len(command):
                break
        return ("".join(container))
        
