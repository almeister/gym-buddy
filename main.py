from gym_class import gymClass


yoga_class = gymClass(1, "Hot Yoga", 1.5, 5)
core_class = gymClass(2, "Shiny Abs", 0.75, 3)

def main_menu():
  print("Gym Buddy")
  print("Select an option\n")

  user_input = int(input("1: Show all classes\n"))

  if user_input == 1:
    show_classes()

def show_classes():
  print("All Classes:")
  yoga_class.show_info()
  core_class.show_info()

if __name__ == "__main__":
  main_menu()

  