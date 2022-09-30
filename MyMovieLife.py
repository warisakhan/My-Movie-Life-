#I received no assistance on this assignment that violates the ethical guidelines set forth by professor and class syllabus 
def myMovieLife(lastname_fstletter, birth_month, cell_digit):

        M = ""

        if months(cell_digit) == 1:
                M = 'month'
        else:
                M = 'months'


        final_sentence = "The " + str(status(cell_digit) ) + " " + (adjective(lastname_fstletter) ) + " " + (subject(birth_month) ) + " " + (complement(cell_digit) ) + " in " + str(months(cell_digit) ) + " " +  M
        return final_sentence


def status(cell_digit):
# can u have multiple or statements in the same line?
#finding true/false status using cell digit 
        if cell_digit == 0: 
                status = True
        elif cell_digit == 2:
                status = True
        elif cell_digit == 4:
                status = True
        elif cell_digit == 6:
                status = True
        elif cell_digit == 8:
                status = True
        elif cell_digit == 1:
                status = False
        elif cell_digit == 3:
                status = False
        elif cell_digit == 5:
                status = False
        elif cell_digit == 7:
                status = False
        elif cell_digit == 9:
                status = False
        return status
        

#finding adjective 
def adjective(lastname_fstletter): #if elif statements for adjective
	if lastname_fstletter == 'A': 
		adjective = 'awesome'
	elif lastname_fstletter == 'B': 
		adjective = 'shocking'
	elif lastname_fstletter == 'C':
		adjective = 'hilarious'
	elif lastname_fstletter == 'D':
		adjective = 'fascinating'
	elif lastname_fstletter == 'E':
		adjective = 'marvelous'
	elif lastname_fstletter == 'F':
		adjective = 'unbelievable'
	elif lastname_fstletter == 'G':
		adjective = 'funny'
	elif lastname_fstletter == 'H':
		adjective = 'epic'
	elif lastname_fstletter == 'I':
		adjective = 'thrilling'
	elif lastname_fstletter == 'J':
		adjective = 'wonderful'
	elif lastname_fstletter == 'K':
		adjective = 'dramatic'
	elif lastname_fstletter == 'L':
		adjective = 'intriguing'
	elif lastname_fstletter == 'M':
		adjective = 'courageous'
	elif lastname_fstletter == 'N':
		adjective = 'beautiful'
	elif lastname_fstletter == 'O':
		adjective = 'bracing'
	elif lastname_fstletter == 'P':
		adjective = 'lively'
	elif lastname_fstletter == 'Q':
		adjective = 'dangerous'
	elif lastname_fstletter == 'R':
		adjective = 'impressive'
	elif lastname_fstletter == 'S':
		adjective = 'astonishing'
	elif lastname_fstletter == 'T':
		adjective = 'interesting'
	elif lastname_fstletter == 'U':
		adjective = 'unexpected'
	elif lastname_fstletter == 'V':
		adjective = 'surpising'
	elif lastname_fstletter == 'W':
		adjective = 'lovely'
	elif lastname_fstletter == 'X':
		adjective = 'electrifying'
	elif lastname_fstletter == 'Y':
		adjective = 'commoving'
		# determine if z should be else or elif?
	elif lastname_fstletter == 'Z':
		adjective = 'overwhelming'
	return adjective 
##finding subject using if/else statements 
def subject(birth_month):
	if birth_month == 'Jan':
		subject = 'biography'
	elif birth_month == 'Feb':
		subject = 'history'
	elif birth_month == 'Mar':
		subject = 'legend'
	elif birth_month == 'Apr':
		subject = 'life'
	elif birth_month == 'May':
		subject = 'anecdote'
	elif birth_month == 'Jun':
		subject = 'revenge'
	elif birth_month == 'Jul':
		subject = 'mission'
	elif birth_month == 'Aug':
		subject = 'existence'
	elif birth_month == 'Sep':
		subject = 'battle'
	elif birth_month == 'Oct':
		subject = 'chronicle'
	elif birth_month == 'Nov':
		subject = 'combat'
	elif birth_month == 'Dec':
		subject = 'fairy tale'
	return subject 
#indentation error?
        #elif birth_month == 'Nov':
                #subject = 'combat'
        #elif birth_month == 'Dec':
                #subject = 'fairy tale'
        #return subject
#finding complement
def complement(cell_digit):
	if cell_digit == 0:
		complement = 'of an adventurer'
	elif cell_digit == 1:
		complement = 'of a warrior'
	elif cell_digit == 2:
		complement = 'of a genius'
	elif cell_digit == 3:
		complement = 'of a movie star'
	elif cell_digit == 4:
		complement = 'of a hero'
	elif cell_digit == 5:
		complement = 'of a scientific'
	elif cell_digit == 6:
		complement = 'of a dreamer'
	elif cell_digit == 7:
		complement = 'of a cowboy'
	elif cell_digit == 8:
		complement = 'of a jedi'
	elif cell_digit == 9:
		complement = 'of an ogre'
	return complement 
#indentation error?in line w cell digit 9
# calculating the months by finding days thru cell digit and then converting to months 
# does this def go here or in front of the if/else statements?
def months(cell_digit):
        days = (cell_digit) ** ((cell_digit%2)+1) * (cell_digit)
        #why is it rounding down and how to fix
        months = int(days / 30) + 1
        return months 
#finding month/months 
#def M(months):
	#if months == 1: 
		#M = 'month'
	#elif months > 1:
		#M = 'months'
	#return M

 	
#print(myMovieLife('Z',"Dec",9))
#print(myMovieLife('G', 'Jan', 6))
#print(myMovieLife('M', 'Aug', 3))
