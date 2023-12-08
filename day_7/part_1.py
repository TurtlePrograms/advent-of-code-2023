import pprint


def getinput():
    input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
    """
    32T3K 765 # one pair
    T55J5 684 # tree of a kind
    KK677 28  # two pair
    KTJJT 220 # two pair
    QQQJA 483 #three of a kind
"""
    return input.strip()


def replace_card(hand):
    for i in hand:
        if i == "T":
            hand[hand.index(i)] = "10"
        elif i == "J":
            hand[hand.index(i)] = "11"
        elif i == "Q":
            hand[hand.index(i)] = "12"
        elif i == "K":
            hand[hand.index(i)] = "13"
        elif i == "A":
            hand[hand.index(i)] = "14"
    return hand


"""
    Five of a kind, where all five cards have the same label: AAAAA
    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    High card, where all cards' labels are distinct: 23456
"""


def count_cards(hand):
    card_count = {}
    for i in hand:
        if i in card_count:
            card_count[i] += 1
        else:
            card_count[i] = 1
    return card_count


def determine_type(line):
    hand = line[0]
    hand = replace_card(hand)
    hand = sorted(hand)
    card_count = count_cards(hand)
    card_count = sorted(card_count.values())
    hand = {"cards": hand, "card_count": card_count, "typerank": None}
    if card_count == [5]:
        print("Five of a kind")
        hand["typerank"] = 7
    elif card_count == [1, 4]:
        print("Four of a kind")
        hand["typerank"] = 6
    elif card_count == [2, 3]:
        print("Full house")
        hand["typerank"] = 5
    elif card_count == [1, 1, 3]:
        print("Three of a kind")
        hand["typerank"] = 4
    elif card_count == [1, 2, 2]:
        print("Two pair")
        hand["typerank"] = 3
    elif card_count == [1, 1, 1, 2]:
        print("One pair")
        hand["typerank"] = 2
    elif card_count == [1, 1, 1, 1, 1]:
        print("High card")
        hand["typerank"] = 1
    return hand


def sortinrank(ranklist):
    if len(ranklist) > 0:
        for j, card in enumerate(ranklist):
            print(card, j)
            cardvalues = 0
            for i in card["cards"]:
                cardvalues += int(i)
            card["cardvalues"] = cardvalues
        ranklist = sorted(ranklist, key=lambda k: k["cardvalues"], reverse=True)
    return ranklist


def calculate_total(lines):
    try:
        lines.sort(key=lambda x: x["cardvalues"], reverse=True)
    except Exception:
        print("no valuerank")
        pprint.pprint(lines)
        pass
    try:
        lines.sort(key=lambda x: x["typerank"], reverse=True)
    except Exception as e:
        print("no typerank")
        pass

    total = 0
    for i in range(len(lines), 0, -1):
        lines[i - 1]["value"] = int(lines[i - 1][1]) * (int(i) - 1)
        print(
            lines[i - 1]["value"], lines[i - 1][1], int(i) - 1, lines[i - 1]["typerank"]
        )
        total += int(lines[i - 1]["value"])

    return total


def main(input=None):
    if input is None:
        input = getinput()

    lines = input.splitlines()
    for line in lines:
        index = lines.index(line)
        line = line.split(" ")

        line[0] = list(line[0])
        line[0] = determine_type(line)
        lines[index] = line[0]
        lines[index][1] = line[1]
    # sort by type rank
    lines = sorted(lines, key=lambda k: k["typerank"], reverse=True)

    # if type rank is the same, sort by card rank
    rank1 = []
    rank2 = []
    rank3 = []
    rank4 = []
    rank5 = []
    rank6 = []
    rank7 = []

    for line in lines:
        if line["typerank"] == 1:
            rank1.append(line)
        elif line["typerank"] == 2:
            rank2.append(line)
        elif line["typerank"] == 3:
            rank3.append(line)
        elif line["typerank"] == 4:
            rank4.append(line)
        elif line["typerank"] == 5:
            rank5.append(line)
        elif line["typerank"] == 6:
            rank6.append(line)
        elif line["typerank"] == 7:
            rank7.append(line)
    rank1 = sortinrank(rank1)
    rank2 = sortinrank(rank2)
    rank3 = sortinrank(rank3)
    rank4 = sortinrank(rank4)
    rank5 = sortinrank(rank5)
    rank6 = sortinrank(rank6)
    rank7 = sortinrank(rank7)
    lines = rank7 + rank6 + rank5 + rank4 + rank3 + rank2 + rank1
    total = calculate_total(lines)
    print(total)

    return 0


custom_input = """TTTTT 123
TTTT3 123
TTT32 123
TTT22 123
TT352 123
T2352 123
T2345 123"""

"""
TTTTT 123 # Five of a kind
TTTT3 123 # Four of a kind
TTT32 123 # three of a kind
TTT22 123 # full house
TT322 123 # two pair
T2352 123 # one pair
T2345 123 # high card
"""
main()
