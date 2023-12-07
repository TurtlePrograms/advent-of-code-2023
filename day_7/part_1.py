valueOrder = list("AKQJT98765432")
valueValue = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def count_cards(hand: list) -> dict:
    """
    Counts the number of each card in a hand
    :param hand: a list of cards(length 5)  e.g. ['AAAAA', '765'])
    :return: a dictionary with the card as the key and the count as the value
    """
    cards = list(hand[0])
    card_count = {}
    for card in cards:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1
    return card_count


def determine_type(hand: list) -> int:
    """
    Determines the rank of a hand
    :param hand: a list of cards(length 5)  e.g. ['AAAAA', '765'])
    :return: a number representing the rank of the hand
    """
    cards = list(hand[0])
    card_counts = count_cards(hand)
    # get the highest count
    max_count = max(card_counts.values())
    # get the card(s) with the highest count
    max_count_cards = [
        card for card, count in card_counts.items() if count == max_count
    ]

    if max_count == 5:
        return 5, max_count_cards
    elif max_count == 4:
        return 4, max_count_cards
    elif max_count == 3:
        return 3, max_count_cards
    elif max_count == 2:
        return 2, max_count_cards
    elif max_count == 1:
        return 1, max_count_cards
    else:
        return 0, max_count_cards


def order_hands(hands: dict) -> list:
    sorted_hands = []
    for hand in hands:
        hand["value"] = valueOrder.index(hand["hand"][0])
        sorted_hands.append(hand)
    sorted_hands.sort(key=lambda x: x["value"])
    return sorted_hands


def main(input):
    # Parse input
    totalValue = 0
    lines = input.strip().split("\n")
    hands = [line.split(" ") for line in lines]
    data = {}
    for hand in hands:
        type, max_count_cards = determine_type(hand)
        data[len(data) + 1] = {
            "hand": hand[0],
            "bid": hand[1],
            "type": type,
            "max_count_cards": max_count_cards,
            "value": 0,
            "multiplier": 0,
        }
    # order all five of a kind hands
    five_kind_hands = []
    for hand in data:
        if data[hand]["type"] == 5:
            five_kind_hands.append(data[hand])
    ordered_five_kind_hands = order_hands(five_kind_hands)
    # order all four of a kind hands
    four_kind_hands = []
    for hand in data:
        if data[hand]["type"] == 4:
            four_kind_hands.append(data[hand])
    ordered_four_kind_hands = order_hands(four_kind_hands)
    # order all three of a kind hands
    three_kind_hands = []
    for hand in data:
        if data[hand]["type"] == 3:
            three_kind_hands.append(data[hand])
    ordered_three_kind_hands = order_hands(three_kind_hands)
    # order all two of a kind hands
    two_kind_hands = []
    for hand in data:
        if data[hand]["type"] == 2:
            two_kind_hands.append(data[hand])
    ordered_two_kind_hands = order_hands(two_kind_hands)
    # order all one of a kind hands
    one_kind_hands = []
    for hand in data:
        if data[hand]["type"] == 1:
            one_kind_hands.append(data[hand])
    ordered_one_kind_hands = order_hands(one_kind_hands)
    # order all no kind hands
    no_kind_hands = []
    for hand in data:
        if data[hand]["type"] == 0:
            no_kind_hands.append(data[hand])
    ordered_no_kind_hands = order_hands(no_kind_hands)
    # order all hands
    ordered_hands = (
        ordered_five_kind_hands
        + ordered_four_kind_hands
        + ordered_three_kind_hands
        + ordered_two_kind_hands
        + ordered_one_kind_hands
        + ordered_no_kind_hands
    )
    # determine multiplier
    # highest value is lowest multiplier (1)
    # lowest value is highest multiplier (len(ordered_hands))
    ordered_hands.reverse()
    for hand in ordered_hands:
        hand["multiplier"] = ordered_hands.index(hand) + 1
    ordered_hands.reverse()
    return ordered_hands


def run(input):
    list = main(input)
    totalValue = 0
    for item in list:
        print(item)
        totalValue += int(item["bid"]) * int(item["multiplier"])
    print(totalValue)


if __name__ == "__main__":
    input = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
KKKKA 924
JJJ55 672
JJJTT 399"""
    run(input)
