<<<<<<< HEAD
'''
Ask a sentence from user. Then ask a integer k from user. Print all the
words which are greater or equal to k
'''
def print_greater(sentence: str,k: int) -> None:
    words = sentence.split()
    for word in words:
        if len(word) >= k:
            print(word, end = ' ')

=======
'''
Ask a sentence from user. Then ask a integer k from user. Print all the
words which are greater or equal to k
'''
def print_greater(sentence: str,k: int) -> None:
    words = sentence.split()
    for word in words:
        if len(word) >= k:
            print(word, end = ' ')

>>>>>>> 5dc3bcbce5040aceb221c751b330de1970861a6d
print_greater('python is a great language. Very easy to understand', 5)