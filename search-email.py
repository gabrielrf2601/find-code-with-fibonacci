from collections import OrderedDict

def fibonacci_iter(n):
    a=1
    b=1
    sequence = []
    if n==1:
        sequence.append(0)
    elif n==2:
        sequence.append(0)
        sequence.append(1)
    else:
        sequence.append(0)
        sequence.append(1)
        sequence.append(1)
        for i in range(n-3):
            total = a + b
            b=a
            a= total
            sequence.append(total)
    
    return sequence
         
sequence = fibonacci_iter(20)

sequence_removed_duplicates = list(OrderedDict.fromkeys(sequence))
sequence_removed_duplicates.remove(0)

text = 'AcoDQeYjrSlByFtyzQhvjoCNVpsaLeQPtGUjQHVzbgabJuAiMHDxwfkNvCwIGmZCTInlSiKvRKxAGzJsgmPeUBAReDzmLzqgJgrXobzfoWiwvRPdFgJzIkSoJscWtVdEbuIRYhXOdHkayBdFIMHSyzIJtmGMhJTiFBaDIzrngCngdSnngUHFWpQpCwElHxunYWsiXKvFOkntcAHiXopTgIKkeovoLrBlPTtMfqTTAgnejUPgKeBsolCtAAjNtKBjf'
code = ''

for index in sequence_removed_duplicates[:10]:
    code += text[index].lower()

print(code)
