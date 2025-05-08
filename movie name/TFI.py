import random
from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

movies_dict = {
   "mahesh babu": [
        "pokiri", "bharatanenenu", "srimanthudu", "maharshi", "athadu",
        "dookudu", "seethammavakitlosirimallechettu", "khaleja", "onenenokkadine", 
        "murari", "nani", "sainikudu", "takkaridonga", "arjun", "bobby"
    ],
    "pawan kalyan": [
        "gabbarsingh", "attarintikidaredi", "tholiprema", "jalsa", "khushi",
        "badri", "panjaa", "vakeelsaab", "agnyaathavaasi", "balu", "johnny", 
        "thammudu", "suswagatham", "komarampuli", "gopalagopala"
    ],
    "prabhas": [
        "bahubali", "mirchi", "varsham", "saaho", "chatrapathi",
        "billa", "darling", "mrperfect", "ekniranjan", "rebel", "radheshyam", 
        "adipurush", "yogi", "pournami", "munna"
    ],
    "jr ntr": [
        "yamadonga", "janathagarage", "temper", "aravindasametha", "simhadri",
        "brindavanam", "nandamurikathanayakudu", "dhammu", "jailavakusa", "ashok", 
        "studentno1", "nannakuprematho", "shakti", "oosaravelli", "rabhasa"
    ],
    "ram charan": [
        "magadheera", "rangasthalam", "dhruva", "nayak", "orange",
        "govindudu andarivadele", "brucelee", "vinayavidheyarama", "chirutha", 
        "yevadu", "zanjeer",  "toofan", "gamechanger"
    ],
    "allu arjun": [
        "pushpa", "alavaikunthapurramuloo", "dj", "julayi", "sarrainodu",
        "bunny", "desamuduru", "arya", "arya2", "parugu", "vedam", 
        "racegurram", "happy", "iddarammayilatho", "varudu"
    ],
    "nani": [
        "jersey", "shyamsingharoy", "nani’sgangleader", "gentleman", "bhalebhalemagadivoy",
        "ninnukori", "mca", "krishnagadiveerapremagaadha", "pillazamindar", "antesundaraniki",
        "ashtachamma", "ride", "jandapaikapiraju", "paillaveshyam", "tenaliramakrishna"
    ]
}

heroes = list(movies_dict.keys())

def create_question(movie):
     n=len(movie)
     temp=[]
     for i in range(n):
         if movie[i]==' ':
             temp.append(' ')
         else:
             temp.append('*')
     qn=''.join(temp)
     return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True

def unlock(qn, movie, letter):
    qn_list = list(qn)
    for i in range(len(movie)):
        if movie[i] == letter:
            qn_list[i] = letter
    return ''.join(qn_list)

def play():
    print("Welcome to the Telugu Movie Guessing Game!")

    p1name = input("\nPlayer! Please enter your name: ").strip()
    
    while True:
        print("\nAvailable Heroes:")
        for hero in heroes:
            print(hero)

        while True:
            chosen_hero = input(f"{p1name}, choose your Telugu hero from the list: ").strip().lower()
            if chosen_hero in movies_dict:
                break
            print("Invalid choice! Please choose a hero from the list.")

        picked_movie = random.choice(movies_dict[chosen_hero])
        qn = create_question(picked_movie)
        print("\nYour movie name:", qn)
        print("Number of letters in the movie (excluding spaces):", len(picked_movie.replace(" ", "")))

        score = 50
        modified_qn = qn
        not_said = True

        while not_said:
            print("\nPress 1 to guess the movie")
            print("Press 2 to unlock another letter ")
            print("Press 3 to exit and reveal the answer")

            d = input("Enter your choice: ").strip()

            if d == "2":
                letter = input("Your letter: ").lower()
                if is_present(letter, picked_movie):
                    modified_qn = unlock(modified_qn, picked_movie, letter)
                    print("Updated Movie Name:", modified_qn)
                    score -= 5  # Deduct 5 points for each letter unlock
                else:
                    print(letter, "not found!")

            elif d == "1":
            
                ans = input("Your answer: ").strip().lower()
                if ans == picked_movie.lower():
                    print("\n🎉 Correct! ", p1name, "you guessed it! 🎉")
                    not_said = False
                else:
                    similarity_score = similarity(ans, picked_movie)
                    if similarity_score > 0.7:
                        print("You're very close! Try again.")
                    elif similarity_score > 0.4:
                        print("You're somewhat close! Keep guessing.")
                    else:
                        print("Wrong answer! Try again.")
                    score -= 10  # Deduct 10 points for wrong guesses

            elif d == "3":
                print(f"\nYou chose to exit. The correct answer was: {picked_movie}")
                not_said = False  # No score deduction for exiting

            else:
                print("Invalid choice! Please enter 1, 2, or 3.")

            if score <= 0:
                print("\nYour score has reached 0! Too many attempts, better luck next time!")
                not_said = False

        print("\n--- GAME OVER ---")
        print(p1name, "your final score:", score if d != "3" else "N/A (Exited)", "🏆")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Have a great day! 😊")
            break

play()

