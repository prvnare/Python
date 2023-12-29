def get_input_word(word:str):
    return input(f' enter {word} : ');

noun: str = get_input_word('noun');
verb: str = get_input_word('verb');

noun1: str = get_input_word('noun1');
verb1: str = get_input_word('verb1');

noun2: str = get_input_word('noun2');
verb2: str = get_input_word('verb2');


story: str = f"""
    Title: A Day at the Wacky {noun}

Once upon a time in the bustling {noun2} of Giggleburg, there was a peculiar {noun} known as the Wacky {noun}. This {noun} was unlike any other, as it was filled with extraordinary creatures and bizarre exhibits. One sunny day, three friends named Sally, Bob, and Henry decided to visit this unique establishment.

As they entered the {noun}, they were {verb} by a talking {noun1}, a dancing penguin, and a singing lion. The {noun1}, whose name was Gerald, {verb1} to be their tour guide for the day. Excitedly, the trio agreed and {verb2} on their wacky adventure.

Their first stop was the "Giggle Gorilla Grove," where enormous gorillas played the saxophone and tap-danced to funky tunes. Sally, Bob, and Henry couldn't stop laughing as they watched the gorillas showcase their unexpected talents.

Next, they wandered into the "Whimsical Waterfall Wonderland," a magical place where waterfalls flowed with rainbow-colored water, and fish performed synchronized swimming routines. The friends were mesmerized by the aquatic acrobatics and even joined in a water ballet with the fish.

Their final destination was the "Jolly Jigsaw Jungle," a section of the {noun} where animals had the ability to shape-shift into different forms. The friends were amazed to see elephants turning into butterflies, and snakes morphing into slithering spaghetti noodles. It was a sight to behold, and they couldn't believe their eyes.

As the day at the Wacky {noun} came to an end, Sally, Bob, and Henry reflected on the unforgettable experience they had. It was a day filled with laughter, amazement, and unexpected surprises. Little did they know that the Wacky Zoo had one more surprise in store for them—a group of monkeys presented them with personalized madlib stories, each filled with their favorite nouns and verbs from the day.

And so, with hearts full of joy and memories to last a lifetime, the friends left the Wacky {noun}, grateful for the magical adventure they had shared together.
""";
print('*' * 30);
print (story);