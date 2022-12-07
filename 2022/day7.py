import MyTools

puzzle = MyTools.AoC(7)

class myfile:
    def __init__(self,name,parentdir):
        self.name=name
        self.size=None
        self.parentdir=parentdir
        self.children={}
        self.files={}

    def addFile(self,name,size):
        self.files[name]=int(size)
    
    def addDir(self,name):
        self.children[name]=myfile(name,self)
    
    def changeDir(self,newDir):
        if newDir == "..":
            return self.parentdir
        else:
            return self.children[newDir]

    def getSize(self):
        s = sum(self.files.values())
        for d in self.children.values():
            s+=d.getSize()
        self.size=s
        return s

    def puzzleA(self):
        s=0
        for d in self.children.values():
            s+=d.puzzleA()
        if self.getSize() < 100000:
            return self.size + s
        else:
            return s

    def puzzleB(self,freespaceneeded):
        s = [float("inf")]
        if self.size > freespaceneeded:
            s.append(self.size)
            for d in self.children.values():
                s.append(d.puzzleB(freespaceneeded))
        return min(s)

root=myfile("/",None)
currentDir=root
lines=puzzle.readLines()
i = 1
while i < len(lines): 
    line = lines[i].split()
    match line[1]:
        case "ls":
            while i+1<len(lines) and lines[i+1].split()[0] != "$":
                i+=1
                line = lines[i].split()
                if line[0]=="dir":
                    currentDir.addDir(line[1])
                else:
                    currentDir.addFile(line[1],line[0])
        case "cd":
            currentDir = currentDir.changeDir(line[2])
    i+=1

puzzle.solution(root.puzzleA())
puzzle.solution(root.puzzleB(30000000-(70000000-root.size)))