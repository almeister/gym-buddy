
class gymClass:

  def __init__(self, id, title, duration, rating):
    self.id = id
    self.title = title
    self.duration = duration
    self.rating = rating

  def show_info(self):
    print(f"Class id: {self.id}")
    print(f"Title: {self.title}")
    print(f"Duration: {self.duration}")
    print(f"Rating: {self.rating}")