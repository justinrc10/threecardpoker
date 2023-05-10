# threecardpoker
Three card poker simulator

Rules:
- Player places ante and/or pair-plus bet to buy into the game
- Dealer deals 3 face-down cards each to the player and himself
- Player looks at cards and decides if he wishes to play his hand
- If the player wants to play, he must put down his ante again, otherwise, he folds and forfeits his buy-in
- The dealer reveals his cards and the payouts are determined

After playing this game enough times, the player will eventually realize that the only decisions to be made is determining what bet you should place, and whether or not you wish to play the hand you are given. It naturally follows to consider what the optimal strategy is. One can show that in a session with many rounds, to maximize the profit, you should play your hand if you get a Q-10-4 or higher, and fold otherwise.
