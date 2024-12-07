class Result:
    def __init__(self, phy, bio, cha, math):
        self.phy = phy
        self.bio = bio
        self.cha = cha
        self.math = math
    
    @property
    def avarage(self):
        return (self.phy + self.bio + self.cha + self.math) // 4

std1 = Result(90,98,95,99)
print(std1.avarage, "%")

#Now change a subject mark:
std1.phy = 80
print(std1.avarage, "%")