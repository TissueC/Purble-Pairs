from string import split
class record:
    
    def __init__(self,difficulty):
        self.difficulty=difficulty
        self.filename=difficulty+" history record.txt" 
        File=open("record\\"+self.filename,"r")
        self.ranks=split(File.readline())
        File.close()

    def remain_first3(self,newdata):
        self.List=[eval(self.ranks[0]),eval(self.ranks[1]),eval(self.ranks[2]),newdata]
        self.List.sort()
        self.List.reverse()
        del self.List[3]
        
    def writefile(self):
        File=open("record\\"+self.filename,"w")
        File.write(str(self.List[0])+" "+str(self.List[1])+" "+str(self.List[2]))
        File.close()

    def readfile_1st(self):
        self.filename=self.difficulty+" history record.txt" 
        File=open("record\\"+self.filename,"r")
        ranks=split(File.readline())
        File.close()

        return "1st: "+ranks[0]

    def readfile_2nd(self):
        self.filename=self.difficulty+" history record.txt" 
        File=open("record\\"+self.filename,"r")
        ranks=split(File.readline())
        File.close()

        return "2nd: "+ranks[1]

    def readfile_3rd(self):
        self.filename=self.difficulty+" history record.txt" 
        File=open("record\\"+self.filename,"r")
        ranks=split(File.readline())
        File.close()

        return "3rd: "+ranks[2]

