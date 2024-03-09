string = "abc xyz pqr lmn"

#'cba zyx rqp nml'

rev_string = ' '.join(word[::-1] for word in string.split())
print(rev_string)