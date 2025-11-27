def hide(card_number):

    card_text = str(card_number)
    
    first_part = card_text[:2]

    last_part = card_text[-4:]

    return first_part + "*" * 10 + last_part

