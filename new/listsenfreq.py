#.strip() only removes spaces at the beginning and end of a string — it does not touch spaces between words inside the string.

li = [" he is goodboy" , " he is badboy ", "he is awesome" , "he is fanastic"]

# Clean up sentences and split into words
sentences = [sentence.strip().split() for sentence in li]

# Find words common to all sentences
common_words = set(sentences[0])
for sentence in sentences[1:]:
    common_words = common_words.intersection(set(sentence))

# Find unique words for each sentence
for i, sentence in enumerate(sentences):
    # Get all words from other sentences
    other_words = set()
    for j, other_sentence in enumerate(sentences):
        if i != j:
            other_words.update(other_sentence)
    
    # Find words unique to this sentence
    unique_words = set(sentence) - other_words
    
    print(f"\nSentence {i+1}: {' '.join(sentence)}")
    print(f"Unique words in this sentence: {unique_words}")

print(f"\nWords common to all sentences: {common_words}")