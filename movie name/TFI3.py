import random
from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

movies_dict = {
    "mahesh babu": ["pokiri", "bharatanenenu", "srimanthudu", "maharshi", "athadu",
                    "dookudu", "seethammavakitlosirimallechettu", "khaleja", "onenenokkadine",
                    "murari", "nani", "sainikudu", "takkaridonga", "arjun", "bobby"],
    "pawan kalyan": ["gabbarsingh", "attarintikidaredi", "tholiprema", "jalsa", "khushi",
                     "badri", "panjaa", "vakeelsaab", "agnyaathavaasi", "balu", "johnny",
                     "thammudu", "suswagatham", "komarampuli", "gopalagopala"],
    "prabhas": ["bahubali", "mirchi", "varsham", "saaho", "chatrapathi", "billa", "darling",
                "mrperfect", "ekniranjan", "rebel", "radheshyam", "adipurush", "yogi",
                "pournami", "munna"],
    "jr ntr": ["yamadonga", "janathagarage", "temper", "aravindasametha", "simhadri",
               "brindavanam", "dhammu", "jailavakusa", "ashok", "studentno1", "nannakuprematho",
               "shakti", "oosaravelli", "rabhasa"],
    "ram charan": ["magadheera", "rangasthalam", "dhruva", "nayak", "orange",
                   "govindudu andarivadele", "brucelee", "vinayavidheyarama", "chirutha",
                   "yevadu", "zanjeer", "toofan", "gamechanger"],
    "allu arjun": ["pushpa", "alavaikunthapurramuloo", "dj", "julayi", "sarrainodu", "bunny",
                   "desamuduru", "arya", "arya2", "parugu", "vedam", "racegurram", "happy",
                   "iddarammayilatho", "varudu"],
    "nani": ["jersey", "shyamsingharoy", "nanisgangleader", "gentleman", "bhalebhalemagadivoy",
             "ninnukori", "mca", "krishnagadiveerapremagaadha", "pillazamindar", "antesundaraniki",
             "ashtachamma", "ride", "jandapaikapiraju", "paillaveshyam", "tenaliramakrishna"]
}

heroes = list(movies_dict.keys())

def create_question(movie):
    return ''.join([' ' if ch == ' ' else '*' for ch in movie])

def is_present(letter, movie):
    return movie.count(letter) > 0

def unlock(qn, movie, letter):
    return ''.join([letter if movie[i] == letter else qn[i] for i in range(len(movie))])

def play():
    print("🎬 Welcome to the Telugu Movie Guessing Game! 🎬")

    while True:
        try:
            num_players = int(input("Enter the number of players (1 or more): "))
            if num_players >= 1:
                break
            else:
                print("Please enter at least 1 player.")
        except ValueError:
            print("Please enter a valid number.")

    players = []
    scores = [0] * num_players

    for i in range(num_players):
        player_name = input(f"Enter name of player {i+1}: ").strip()
        players.append(player_name)

    while True:
        for current_player in range(num_players):
            print("\n🎭 Available Heroes:")
            for hero in heroes:
                print(f"👉 {hero}")

            chosen_hero = input(f"\n🎯 {players[current_player]}, choose a Telugu hero: ").strip().lower()
            while chosen_hero not in movies_dict:
                print("❌ Invalid hero! Try again.")
                chosen_hero = input(f"{players[current_player]}, choose a Telugu hero: ").strip().lower()

            picked_movie = random.choice(movies_dict[chosen_hero])
            qn = create_question(picked_movie)
            modified_qn = qn
            used_letters = set()
            hint_count = 0
            print(f"\n🔐 Movie: {qn}")
            print("📏 Letters (excluding spaces):", len(picked_movie.replace(" ", "")))

            while True:
                print("\n 1️⃣ Guess the movie")
                print(" 2️⃣ Unlock a letter (-10 points per hint)")
                print(" 3️⃣ Exit (reveal answer)")

                choice = input("Your choice: ").strip()
                if choice == "1":
                    guess = input("🎬 Your guess: ").strip().lower()
                    if guess == picked_movie.lower():
                        print(f"✅ Correct! Well done {players[current_player]} 🎉")
                        gained = 50 - (hint_count * 10)
                        scores[current_player] += max(0, gained)
                        break
                    else:
                        similarity_score = similarity(guess, picked_movie)
                        if similarity_score > 0.9:
                            print("🤏 Very close!")
                        elif similarity_score > 0.6:
                            print("👌 Somewhat close.")
                            scores[current_player] -= 5
                        else:
                            print("❌ Wrong guess.")
                            scores[current_player] -= 5

                elif choice == "2":
                    letter = input("🔤 Enter a letter to reveal: ").lower()
                    if len(letter) != 1 or not letter.isalpha():
                        print("⚠️ Enter a valid single alphabet letter.")
                        continue
                    if letter in used_letters:
                        print("⚠️ You already tried this letter.")
                        continue
                    used_letters.add(letter)
                    if is_present(letter, picked_movie):
                        modified_qn = unlock(modified_qn, picked_movie, letter)
                        print("🔓 Updated Movie:", modified_qn)
                        hint_count += 1
                    else:
                        print("❌ Letter not in movie.")
                        hint_count += 1

                elif choice == "3":
                    print(f"📢 The movie was: {picked_movie}")
                    break
                else:
                    print("⚠️ Invalid option. Try again.")

        # End of round
        print("\n============================")
        again = input("🔁 Do you want to play another round? (yes/no): ").strip().lower()
        if again != "yes":
            break
        print("============================")

        


    # Final results - displayed only when players exit
    print("\n🎉 GAME ENDED - FINAL RESULTS 🎉")
    sorted_scores = sorted(zip(scores, players), reverse=True)

    for score, name in sorted_scores:
        print(f"{name}: {score} points")

    if num_players == 1:
        print("\n🧑 Solo player mode. No winner declared.")
    elif num_players == 2:
        print(f"\n🏆 Winner: {sorted_scores[0][1]} with {sorted_scores[0][0]} points")
    else:
        print(f"\n🏆 Winner: {sorted_scores[0][1]} with {sorted_scores[0][0]} points")
        print(f"🥈 Runner-up: {sorted_scores[1][1]} with {sorted_scores[1][0]} points")

# Run the game
play()
