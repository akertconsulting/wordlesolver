from nltk.corpus import words

def wordle_solver(discovered_letter_order=[], 
                  bad_letters=[], 
                  bad_letter_order_one=[],
                  bad_letter_order_two=[],
                  bad_letter_order_three=[],
                  bad_letter_order_four=[],
                  bad_letter_order_five=[]):
    # Corpus
    real_words = [x.lower() for x in words.words()]
    five_letter_words = [x for x in real_words if len(x) == 5]
    
    # Building discovered letters
    discovered_letters = list(set(bad_letter_order_one + bad_letter_order_two + bad_letter_order_three
                            + bad_letter_order_four + bad_letter_order_five))
    possible_words = []
    for possible_word in five_letter_words:
        bad_word = False
        # Remove words that have bad letters
        if bad_letters:
            for letter in possible_word:
                if letter in bad_letters:
                    bad_word = True
        # If word passed bad letters, remove words that have no discovered letters
        if not bad_word:
            if len(discovered_letters) > 0:
                for good_letter in discovered_letters:
                    if good_letter not in possible_word:
                        bad_word = True
        # If word still passing, remove words that don't have discovered letter order
        if not bad_word:
            if discovered_letter_order:
                for i, letter in enumerate(possible_word):
                    if discovered_letter_order[i]:
                        if letter != discovered_letter_order[i]:
                            bad_word = True
        # If word still passing, remove words that have letters in the wrong place
        if not bad_word:
            if bad_letter_order_one:
                if possible_word[0] in bad_letter_order_one:
                    bad_word = True
            if bad_letter_order_two:
                if possible_word[1] in bad_letter_order_two:
                    bad_word = True
            if bad_letter_order_three:
                if possible_word[2] in bad_letter_order_three:
                    bad_word = True
            if bad_letter_order_four:
                if possible_word[3] in bad_letter_order_four:
                    bad_word = True
            if bad_letter_order_five:
                if possible_word[4] in bad_letter_order_five:
                    bad_word = True
                
        # If word still passing, add to possible words
        if not bad_word:
            possible_words.append(possible_word)
    # Sort by more "likely" words, not repeated letters
    enriched_words = []
    for word in possible_words:
        unique_letters = len(set(word)) == len(word)
        enriched_words.append({'word': word, 'unique_letters': unique_letters})
    enriched_words = sorted(enriched_words, key=lambda d: d['unique_letters'], reverse=True)
    return list(set([x.get('word') for x in enriched_words]))