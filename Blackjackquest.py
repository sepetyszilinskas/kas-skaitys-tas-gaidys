import random
import game_engine as game

playa = game.Game_engine()
dealer = game.Game_engine()

kalade = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
              "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
              "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
              "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]



def check_if_bust():
    if playa.total > 21:
        playa.bust = True
    if dealer.total > 21:
        dealer.bust = True


def check_score():
    if playa.bust and dealer.bust:
      print("DRAW")
    else:
      if playa.total > dealer.total:
        print("Playa wins")
      elif dealer.total > playa.total:
        print("Dealer wins")
      else:
        print("DRAW")


def draw(player):
    korta = random.choice(kalade)
    player.hand.append(korta)
    kalade.remove(korta)

    if korta in ["J", "Q", "K"]:
        player.total += 10
    elif korta == "A":
        if player.total < 11:
            player.total += 11
        else:
            player.total += 1
    else:
        player.total += korta

def run_game():
    turn_counter = 1
    while turn_counter < 10:
        if turn_counter % 2 == 0 and playa.is_hitting and not playa.bust:
            action = int(input("Input 2 for stand, input 1 for hit : "))
            if action == 1:
                draw(playa)
                print("u drew", playa.hand[-1])
            else:
                playa.is_hitting = False
            print(playa.hand)
            check_if_bust()

        else:
            if dealer.total < 17:
                draw(dealer)
                print("dealer", dealer.hand)
                check_if_bust()
            else:
                dealer.is_hitting = False
                if playa.bust or playa.is_hitting == False:
                    check_score()
                    break
        turn_counter += 1


