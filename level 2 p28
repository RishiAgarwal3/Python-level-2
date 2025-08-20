def word_frquency(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
        
        words = text.split()
        frequency = {}
        
        for char in '.,!?;:"()[]{}':
            text = text.replace(char, '')
        text = text.lower()
        words = text.split()

        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

        print("\n The Top ten most common words are:")
        for word, count in sorted_words[:10]:
            print(word+ ":", count)
    except FileNotFoundError:
        print("The file does not exist.")

#example usage

filename = input("Enter the filename: ")
word_frquency(filename)
