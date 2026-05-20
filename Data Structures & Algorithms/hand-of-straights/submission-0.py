class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 1. Quick rejection: total cards must be divisible by groupSize
        if len(hand) % groupSize != 0: return False
        # 2. Frequency of each card value
        card_count = Counter(hand)

        # 3. Process card values in ascending order
        for card_value in sorted(hand):
            # If this card is already fully used in previous groups, skip
            if card_count[card_value] == 0: continue
            # Try to form a group starting at card_value
            for next_card in range(card_value, card_value+groupSize):
                # Not enough of this needed value → cannot form a straight
                if card_count[next_card] == 0: return False
                # Use one copy for this group
                card_count[next_card] -= 1
        # All cards successfully grouped
        return True