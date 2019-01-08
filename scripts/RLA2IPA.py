"""Convert Russian Linguistic Alphabet to International Phonetic Alphabet."""
# TODO Are there already tools out there to do this?

# Translation tables would probably be a good approach
# https://docs.python.org/3/library/stdtypes.html#str.maketrans
# tt = ''.maketrans('сту', 'stu')
# https://docs.python.org/3/library/stdtypes.html#str.translate
# 'сло́въ'.translate(tt)

# check that the output does not contain any characters from the input
# something like...
# overlap = set(input_str).intersection(set(output_str))
# if len(overlap) > 0:
#     raise NotImplementedError('The following characters are not implemented: '
#                               '{}'.format(overlap))
...
