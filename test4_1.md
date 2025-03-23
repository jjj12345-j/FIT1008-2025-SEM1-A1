### State at the beginning
- **Current color: GREEN Current label: TWO**
- Player Alice has 2 cards: [(RED ZERO),(YELLOW FIVE)]
- Player Bob has 2 cards: [(BLUE FIVE),(YELLOW REVERSE)]
- Player Charlie has 2 cards: [(RED REVERSE),(BLUE SKIP)]
- Player David has 2 cards: [(RED NINE),(GREEN NINE)]
### Round 1
- **Current player**: Alice
- **Current color: GREEN Current label: TWO**
- **Action**: Alice draws a card into their hand.
- **State after the round**
	- Player Bob has 2 cards: [(BLUE FIVE),(YELLOW REVERSE)]
	- Player Charlie has 2 cards: [(RED REVERSE),(BLUE SKIP)]
	- Player David has 2 cards: [(RED NINE),(GREEN NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]

### Round 2
- **Current player**: Bob
- **Current color: GREEN Current label: TWO**
- **Action**: Bob draws a card into their hand.
- **State after the round**
	- Player Charlie has 2 cards: [(RED REVERSE),(BLUE SKIP)]
	- Player David has 2 cards: [(RED NINE),(GREEN NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 3 cards: [(BLUE ONE),(BLUE FIVE),(YELLOW REVERSE)]

### Round 3
- **Current player**: Charlie
- **Current color: GREEN Current label: TWO**
- **Action**: Charlie draws a card into their hand.
- **State after the round**
	- Player David has 2 cards: [(RED NINE),(GREEN NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 3 cards: [(BLUE ONE),(BLUE FIVE),(YELLOW REVERSE)]
	- Player Charlie has 3 cards: [(RED REVERSE),(BLUE SKIP),(YELLOW ZERO)]

### Round 4
- **Current player**: David
- **Current color: GREEN Current label: TWO**
- **Action**: David plays GREEN NINE
- **State after the round**
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 3 cards: [(BLUE ONE),(BLUE FIVE),(YELLOW REVERSE)]
	- Player Charlie has 3 cards: [(RED REVERSE),(BLUE SKIP),(YELLOW ZERO)]
	- Player David has 1 card: [(RED NINE)]

### Round 5
- **Current player**: Alice
- **Current color: GREEN Current label: NINE**
- **Action**: Alice draws a card GREEN SEVEN and plays it.
- **State after the round**
	- Player Bob has 3 cards: [(BLUE ONE),(BLUE FIVE),(YELLOW REVERSE)]
	- Player Charlie has 3 cards: [(RED REVERSE),(BLUE SKIP),(YELLOW ZERO)]
	- Player David has 1 card: [(RED NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]

### Round 6
- **Current player**: Bob
- **Current color: GREEN Current label: SEVEN**
- **Action**: Bob draws a card RED SEVEN and plays it.
- **State after the round**
	- Player Charlie has 3 cards: [(RED REVERSE),(BLUE SKIP),(YELLOW ZERO)]
	- Player David has 1 card: [(RED NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 3 cards: [(BLUE ONE),(BLUE FIVE),(YELLOW REVERSE)]

### Round 7
- **Current player**: Charlie
- **Current color: RED Current label: SEVEN**
- **Action**: Charlie plays RED REVERSE
- **State after the round**
	- Player Bob has 3 cards: [(BLUE ONE),(BLUE FIVE),(YELLOW REVERSE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player David has 1 card: [(RED NINE)]
	- Player Charlie has 2 cards: [(BLUE SKIP),(YELLOW ZERO)]

### Round 8
- **Current player**: Bob
- **Current color: RED Current label: REVERSE**
- **Action**: Bob plays YELLOW REVERSE
- **State after the round**
	- Player Charlie has 2 cards: [(BLUE SKIP),(YELLOW ZERO)]
	- Player David has 1 card: [(RED NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 2 cards: [(BLUE ONE),(BLUE FIVE)]

### Round 9
- **Current player**: Charlie
- **Current color: YELLOW Current label: REVERSE**
- **Action**: Charlie plays YELLOW ZERO
- **State after the round**
	- Player David has 1 card: [(RED NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 2 cards: [(BLUE ONE),(BLUE FIVE)]
	- Player Charlie has 1 card: [(BLUE SKIP)]

### Round 10
- **Current player**: David
- **Current color: YELLOW Current label: ZERO**
- **Action**: David draws a card YELLOW SKIP and plays it.
- **State after the round**
	- Player Bob has 2 cards: [(BLUE ONE),(BLUE FIVE)]
	- Player Charlie has 1 card: [(BLUE SKIP)]
	- Player David has 1 card: [(RED NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]

### Round 11
- **Current player**: Bob
- **Current color: YELLOW Current label: SKIP**
- **Action**: Bob draws a card into their hand.
- **State after the round**
	- Player Charlie has 1 card: [(BLUE SKIP)]
	- Player David has 1 card: [(RED NINE)]
	- Player Alice has 3 cards: [(RED ZERO),(YELLOW FIVE),(YELLOW SEVEN)]
	- Player Bob has 3 cards: [(BLUE ONE),(BLUE FIVE),(GREEN FOUR)]

### Round 12
- **Current player**: Charlie
- **Current color: YELLOW Current label: SKIP**
- **Action**: Charlie plays BLUE SKIP
## End of Game, winner: Charlie
