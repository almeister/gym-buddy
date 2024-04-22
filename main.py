from gymclass import GymClass

yoga_class = GymClass("Extreme Yoga", 1.5)
all_classes = [yoga_class]

def main_menu():
    print("Main Menu:\n")
    print("1: Show classes")
    print("2: Add a class")
    print("0: Quit\n")
    user_input = input("Select an option by number:")
    return user_input
    
def show_all_classes():
    print("All Classes:\n")
    for gc in all_classes:
        gc.display_info()
    
def add_class():
    title = input("Class Title:")
    duration = input("Class Duration:")
    new_class = GymClass(title, duration)
    all_classes.append(new_class)
    
def quit():
    print("Keep it in your shell!")

if __name__ == "__main__":
    print("Gym Buddy\n")
    
    user_input = -1
    while (user_input != 0):
        user_input = int(main_menu())
    
        if user_input == 1:
            show_all_classes()
        elif user_input == 2:
            add_class()
        elif user_input == 0:
            quit()   
    
    
        
        