# Operations on Set

'''
Sets in Python support various operations that allow you to manipulate and work with the elements in 
the sets. Some of the common operations on sets include:
'''
## 1. Union (|): Combines elements from two sets, excluding duplicates.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
# Output: {1, 2, 3, 4, 5}


## 2. Intersection (&): Returns elements common to both sets.
intersection_set = set1 & set2
# Output: {3}


## 3. Difference (-): Returns elements in the first set but not in the second set.
difference_set = set1 - set2
# Output: {1, 2}

## 4. Symmetric Difference (^): Returns elements that are in either of the sets, but not both.
sym_difference_set = set1 ^ set2
# Output: {1, 2, 4, 5}

## 5. Subset (<=): Checks if one set is a subset of another.
is_subset = set1 <= set2
# Output: False

## 6. Superset (>=): Checks if one set is a superset of another.
is_superset = set1 >= set2
# Output: False

## 7. Disjoint (isdisjoint()): Checks if two sets have no common elements.
is_disjoint = set1.isdisjoint(set2)
# Output: False

## 8. Subset Proper (<): Checks if one set is a proper subset of another.
is_proper_subset = set1 < set2
# Output: False

## 9.Superset Proper (>): Checks if one set is a proper superset of another.
is_proper_superset = set1 > set2
# Output: False

'''
These operations provide powerful ways to manipulate sets and perform set-theoretic operations 
efficiently in Python. They are particularly useful for tasks involving unique elements and 
mathematical computations.
'''