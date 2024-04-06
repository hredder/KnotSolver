from fourMarking import *
from copy import *

# Coefficients are set as prime integers for now
class coef(Enum):
    ONE = 1
    A = 2
    B = 3
    C = 5
    D = 7

# Utility function to multiply two multiples of variables, replaces dest parameter with result
def multiply_multiples(dest:list, src:list):
    for i in range(len(src)):
        dest.append(src[i])


# Function that multiplies two sums, replaces dest parameter with result
def multiply_sums(dest:list, src:list):
    original = dest.copy()
    # Clear destination list so we can append new terms as we calculate them
    dest.clear()
    for i in range(len(original)):
        for j in range(len(src)):
            # Make a copy of term i from the original list, then multiply and append to destination list
            term = copy.deepcopy(original[i])
            multiply_multiples(term, src[j])
            dest.append(term)


# Function that finds common factor of terms in a sum
# Removes common factor from each term and returns it as a multiple
def get_common_factor(sum:list)->'list':
    # Copy the first term of the sum, assume it is the common factor at first
    common = copy.deepcopy(sum[0])
    for i in range(1,len(sum)):
        # Iterate over all following terms
        next = sum[i]
        for j in range(len(common)):
            # Iterate over each variable in the common factor
            x = common[j]
            # If a term has fewer instances of a variable than the common factor,
            #   remove the extra instances in the common factor
            if next.count(x) < common.count(x):
                for k in range(common.count(x) - next.count(x)):
                    common.remove(x)
    
    # Now, remove the common factor from each term
    for i in range(len(common)):
        for j in range(len(sum)):
            sum[j].remove(common[i])
    
    return common


class coefficient:
    def __init__(self, numerator:tuple, denominator:tuple):
        # Initialize numerator and denominator, expected to be 2-tuples
        # The first element of each is the common factor, the second is the list of summand terms
        self.numerator = numerator
        self.denominator = denominator

    def mult(self, factor:'coefficient'):
        multiply_multiples(self.numerator[0],factor.numerator[0])
        multiply_multiples(self.denominator[0],factor.denominator[0])
        multiply_sums(self.numerator[1], factor.numerator[1])
        multiply_sums(self.denominator[1], factor.denominator[1])


class relation:
    def __init__(self, lefthandside:list, righthandside:list):
        # Each side is a list of 2-tuples containing coefficient and diagram
        # Set LHS of relation to given LHS
        self.lefthandside = lefthandside
        # Set RHS of relation to given RHS
        self.righthandside = righthandside

vertex = relation(fourMarking([crossingType.VERTEX]), [fourMarking([crossingType.VERTEX])])