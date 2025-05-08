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
        "brindavanam", "dhammu", "jailavakusa", "ashok", 
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
    n = len(movie)
    temp = []
    for i in range(n):
        if movie[i] == ' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn = ''.join(temp)
    return qn

def is_present(letter, movie):
    c = movie.count(letter)
    return c != 0

def unlock(qn, movie, letter):
    qn_list = list(qn)
    for i in range(len(movie)):
        if movie[i] == letter:
            qn_list[i] = letter
    return ''.join(qn_list)

def play():
    print("Welcome to the Telugu Movie Guessing Game!")

    num_players = int(input("Enter the number of players: "))
    players = []
    scores = []

    for i in range(num_players):
        player_name = input(f"Enter the name of player {i+1}: ").strip()
        players.append(player_name)
        scores.append(50)  # Starting score for each player

    current_player = 0  # Player 1 starts the game
    while True:
        print("\nAvailable Heroes:")
        for hero in heroes:
            print(hero)

        chosen_hero = input(f"{players[current_player]}, choose your Telugu hero from the list: ").strip().lower()
        while chosen_hero not in movies_dict:
            print("Invalid choice! Please choose a hero from the list.")
            chosen_hero = input(f"{players[current_player]}, choose your Telugu hero from the list: ").strip().lower()

        picked_movie = random.choice(movies_dict[chosen_hero])
        qn = create_question(picked_movie)
        print("\nYour movie name:", qn)
        print("Number of letters in the movie (excluding spaces):", len(picked_movie.replace(" ", "")))

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
                    scores[current_player] -= 1  # Deduct 1 point for each letter unlock
                else:
                    print(letter, "not found!")

            elif d == "1":
                ans = input("Your answer: ").strip().lower()
                if ans == picked_movie.lower():
                    print(f"\n🎉 Correct! {players[current_player]}, you guessed it! 🎉")
                    not_said = False
                    scores[current_player] += 4  # Add 4 points for correct guess
                else:
                    similarity_score = similarity(ans, picked_movie)
                    if similarity_score > 0.9:
                        print("You're very close! No points deducted.")
                    elif similarity_score > 0.6:
                        print("You're somewhat close! Deducting 1 point.")
                        scores[current_player] -= 1
                    else:
                        print("Wrong answer! Deducting 1 point.")
                        scores[current_player] -= 1

            elif d == "3":
                print(f"\nYou chose to exit. The correct answer was: {picked_movie}")
                not_said = False  # No score deduction for exiting

            else:
                print("Invalid choice! Please enter 1, 2, or 3.")

            if scores[current_player] <= 0:
                print("\nYour score has reached 0! Too many attempts, better luck next time!")
                not_said = False

        print("\n--- GAME OVER ---")
        print(f"{players[current_player]} your final score: {scores[current_player]} 🏆")

        # Switch to the next player
        current_player = (current_player + 1) % num_players

        if all(score <= 0 for score in scores):
            print("All players have no points left. The game is over!")
            break

        # Ask if players want to play again
        play_again = input("Do you want to continue? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Have a great day! 😊")
            break

    # Display the results
    sorted_scores = sorted(zip(scores, players), reverse=True)
    print("\n--- FINAL RESULTS ---")
    print(f"Winner: {sorted_scores[0][1]} with {sorted_scores[0][0]} points 🏆");
    print(f"Runner-up: {sorted_scores[1][1]} with {sorted_scores[1][0]} points 🥈");

play()
