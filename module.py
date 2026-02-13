class Robot:
    def __init__(self, name, color):
# initialize properties code here
        pass
        self.name = name
        self.color = color
        self.battery = 100
        self.durability = 100
        self.productivity = 0

    def charge(self, amount):
        amount = int(amount)
        self.battery += amount
        if self.battery < 100:
            self.battery = self.battery + amount
        return f"{self.name} charged by {amount} "
    
    def repair(self,amount):
        self.repair += int(amount)
        return self.repair
    
    def work(self, amount):
        hours = int(hours)
        self.work += int(amount)
        return self.work 
        
    def status(self):
        return f"({self.name}| Color: {self.color}| Durability: {self.durability})"
        
    def recolor():
        
        def shutdown(self, amount):
            pass