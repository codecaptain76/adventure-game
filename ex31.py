print "You walk into a room, there are 3 bowls of ice cream on the table. Which one do you choose?"

ice_cream = raw_input("> ")

if ice_cream == "1":
    print "There's a giant spider on top!! What do you do?"
    print "1. Eat the spider."
    print "2. Scream at the spider."
    print "3. Kill the spider."
    
    spider = raw_input("> ")

    if spider == "1":
        print "You gain Spidey-powers!"
    elif spider == "2":
        print "The spider screams back."
    elif spider == "3":
        print "The spider ghost haunts you FOREVER!!"
    else:   
        print "%s was not an option. Game Over!" % spider

elif ice_cream == "2":
    print "You find an empty bowl. What do you do?"
    print "1. Cry Hysterically."
    print "2. Throw it across the room."
    print "3. Wear bowl as a new hat."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Awakens a ferocious bear, that eats your face. Game Over!"
    elif insanity == "3":
        print "Start a new fashion trend. Appear at New York's Fashion Week. Become famous!"
    else:
        print "Don't you know how to follow directions? Game Over!"

else:
    print "Ice Cream falls from the sky, and you die. Game Over!"
