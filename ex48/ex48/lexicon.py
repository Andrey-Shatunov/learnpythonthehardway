def scan(sentence):

    words = sentence.split(' ')
	
    res = []
   
    direction=['left', 'north', 'east', 'west', 'down', 'south', 'up', 'right', 'back']
    verb=  ['go', 'stop', 'kill', 'eat']
    stop= ['the', 'in', 'of', 'from', 'at', 'it']
    noun= ['door', 'bear', 'princess', 'carbinet']

    for word in words:
        #bad code
        if word.lower().isdigit():
            res.append(("number", int(word)))
	elif word.lower() in direction:
	    res.append(("direction", word))
	elif word.lower() in verb:
	    res.append(("verb", word))
	elif word.lower() in stop:
	    res.append(("stop", word))
	elif word.lower() in noun:
            res.append(("noun", word))
        else:
            res.append(("error", word))
    return res

