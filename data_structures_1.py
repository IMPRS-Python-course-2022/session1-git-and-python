# Simple data types can be combined into collections, which can have different structures
# The structure can matter a lot to efficiency and simplicity of use

# For example, we have seen lists, which are ordered collections of elements with a dynamic size and type
# Lists are very flexible, but not necessarily super efficient
#   Indexing:        0    1    2    3    4    5    6    7    8    9
participant_1_RTs = [713, 552, 473, 143, 638, 311, 668, 937, 621, 459]
participant_2_RTs = [287, 750, 411, 410, 351, 1040, 1124, 891, 924, 664]
participant_3_RTs = [342, 1063, 131, 485, 480, 159, 60, 389, 375, 653]

# Compare the RTs on the 4th trial (index 3)
print(participant_1_RTs[3], participant_2_RTs[3], participant_3_RTs[3])

# Maybe a list of lists is slightly cleaner?
#   Second (inner) index >  
#    0    1    2    3    4    5    6    7    8    9         First (outer) index \/
participants = [
    [713, 552, 473, 143, 638, 311, 668, 937, 621, 459],    # 0
    [287, 750, 411, 410, 351, 1040, 1124, 891, 924, 664],  # 1
    [342, 1063, 131, 485, 480, 159, 60, 389, 375, 653]     # 2
]

# Getting a single value, e.g. RT of 4th trial from 2nd participant
print(participants[1, 3])

# Comparing all of them is cleaner, but still slightly cumbersome
for participant in participants:
    print(participant[3])

# There are also arrays, provided by the numpy package!
# So what's the difference between a list and an array?
# Mostly technical, so not much to worry about, but:
#  - Fixed size (no appending)
#  - Fixed type (everything of the same type)
#  - Bulk computations on arrays are much faster
import numpy as np  # noqa: E402

participants_array = np.array(participants)  # Convert our list of lists to an array
print(participants_array[:, 3])  # It's so simple now to compare reaction times!
print(participants_array[1, :])  # Or to get all RTs from a single participant.

# What about participant RT means and stdevs?
print(participants_array.mean(axis=1), participants_array.std(axis=1))

# ... or trial RT means?
print(participants_array.mean(axis=0))

# Homework exercise:
#   1) Import the log function from the math package (built-in)
#   2) Try to calculate the log-RTs (the logarithm of each reaction time), using:
#      - the three separate RT lists (hint: you may need to use several for-loops)
#      - the participants list of lists (hint: two for-loops should be enough here!)
#      - the participants array in numpy (hint: use np.log instead of Python's log function)
