# threecardpoker
Three card poker simulator

Rules:
- Player places ante and/or pair-plus bet to buy into the game
- Dealer deals 3 face-down cards each to the player and himself
- Player looks at cards and decides if he wishes to play his hand
- If the player wants to play, he must put down his ante again, otherwise, he folds and forfeits his buy-in
- Dealer reveals his cards and the payouts are determined

Hand rankings:
- Straight flush - Same suit in an unbroken sequence (ex. 4H, 5H, 6H)
- Straight - Unbroken sequence (ex. 3H, 4S, 5H)
- Three of a kind - Three of the same rank (ex. 7H, 7C, 7D)
- Flush - Same suit (ex. 3D, 10D, KD)
- Pair - Two of the same rank (ex. 4S, AH, 4C)
- High - Highest card (ex. QH, 10D, 4S)
- Ties are determined by the rank and suit of the highest cards

After playing this game enough times, the player will eventually realize that the only decisions to be made is determining what bet you should place, and whether or not you wish to play the hand you are given. It naturally follows to consider what the optimal strategy is. One can show that in a session with many rounds, to maximize the profit, you should play your hand if you get a Q-10-4 or higher, and fold otherwise. This program allows you to experiment with how much you wish to put into the ante and how much to bet on the pair-plus. Given the intial funds, settle amount, ideal ante bet, ideal pair-plus bet, and number of simulations, the program will run that number of sessions and list the frequency of busts and settles.
