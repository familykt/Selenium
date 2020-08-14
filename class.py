#%%
class Fourcal:
    pass



# %%
a = Fourcal()
type(a)

# %%
class Fourcal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result



# %%
a = Fourcal()
a.setdata(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

# %%
a = Fourcal(4,2)
a.add()

# %%
class MoreFourCal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result


# %%
a = MoreFourCal(4,2)
a.add()

# %%
a.pow()

# %%
class SafeFourCal(Fourcal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

# %%
a = SafeFourCal(4,0)
a.div()

# %%
class 