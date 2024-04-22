from datetime import datetime

class GymClass:

    def __init__(self, title, duration):
        self.id = "".join(title.lower().split())
        self.title = title
        self.duration = duration
    
    def display_info(self):
        print(f"Class id: {self.id}")
        print(f"Title: {self.title}")
        print(f"Duration: {self.duration} hrs\n")
