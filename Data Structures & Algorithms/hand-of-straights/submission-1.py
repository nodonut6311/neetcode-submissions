class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()

        while hand:
            current = hand.pop(0)
            count = 1

            while count < groupSize:
                target = current + 1

                found = False
                for i in range(len(hand)):
                    if hand[i] == target:
                        hand.pop(i)
                        current = target
                        count += 1
                        found = True
                        break

                if not found:
                    return False

        return True