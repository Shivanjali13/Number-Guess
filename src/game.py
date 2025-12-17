import random
import time

          
MIN_NUMBER = 1
MAX_NUMBER = 100

def choose_difficulty():
    print("Select difficulty level")
    print("1.Easy(10 attempts)")
    print("2.Medium(7 attempts)")
    print("3.Hard(3 attempts)")
    
    while True:
        choice = input("Enter your choice (1/2/3):")
        
        if choice == "1":
            return "easy",10
        elif choice == "2":
            return "medium",7
        elif choice == "3":
            return "hard",3
        else:
            print("Invalid choice! Select 1,2 or 3 \n")
            

def read_high_score():
    try:
        with open("src/high_score.txt","r")as file:
            data = file.read().strip()
            if not data:
                return None
            difficulty, attempts, time_taken = data.split(",")
            return difficulty, int(attempts), float(time_taken)
    except FileNotFoundError:
        return None
    
def write_high_score(difficulty, attempts, time_taken):
    with open("src/high_score.txt","w") as file:
        file.write(f"{difficulty},{attempts},{time_taken}")

def play_game():
    difficulty, max_attempts = choose_difficulty()
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    
    attempts_left = max_attempts
    attempts_used = 0
    
    print(f"Guess the number between {MIN_NUMBER} and {MAX_NUMBER}")
    print(f"You have {attempts_left} attempts.\n")
    
    start_time = time.time()
    
    while attempts_left > 0:
        try:
            guess=int(input("Enter your guess:"))
            
            if guess<MIN_NUMBER or guess>MAX_NUMBER:
                print(f"Invalid guess..enter number between {MIN_NUMBER} AND {MAX_NUMBER}")
                continue
            
            attempts_left=attempts_left-1
            attempts_used=attempts_used+1
            
            if guess==secret_number:
                end_time = time.time()
                time_taken = round(end_time - start_time, 2)
                
                print("\n Congratulations! Correct guess.")  
                print(f"Attempts used: {attempts_used}")                             
                print(f"Time taken: {time_taken} seconds")
                
                previous_score = read_high_score()
                
                if(previous_score is None or 
                        attempts_used < previous_score[1] or 
                        (attempts_used == previous_score[1] and time_taken < previous_score[2])):
                    write_high_score(difficulty, attempts_used, time_taken)
                    print("New High score!")
                    
                return
                
            elif guess<secret_number:
                print("Too low!")
            else:
                print("Too high!")
                
            print(f"Attempts left: {attempts_left}\n")
            
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
            
    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    
    print("Game over")
    print(f"Correct number was {secret_number}")
    print(f"Time taken: {time_taken} seconds")
            
 

   
if __name__=="__main__":
    play_game()