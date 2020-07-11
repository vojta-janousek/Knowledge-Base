import re


# \b - Word boundary
# Matches 'Ha' and 'bla Ha' but not 'fooHa'
pattern.compile(r'\bHa')



# EER7ANIMAL
pattern = re.compile(r'EER7ANIMAL')
pattern = re.compile(r'eer7animal', re.IGNORECASE)
pattern = re.compile(r'eer7animal', re.I)
match = pattern.search(s)
