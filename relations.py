###################
# Got bored...
# Let A = {1,2,3} and B = {1,3,5} and define relation S from A to B as follows:
# For every (x,y) that is an element of A x B, S is subset whose elements are (x,y) ordered paired which satisfy this expression:
# x < y

def calc_product(domain, codomain):
    """
    accepts two sets of values called domain and codomain
    generates a set which is the product of domain and codomain
    and returns a list of ordered pairs which are the elements
    of the product set.
    E.g. Given set A and set B, find A x B and return the list of its elements
    """
    cartesian_product = []
    for x in domain:
        for y in codomain:
            ordered_pair = (x,y)
            cartesian_product.append(ordered_pair)
    return cartesian_product

def find_relation_set(cartesian_product):
    """
    accepts a list of ordered pairs and tests each ordered pair (x,y)
    for the following condition:
        x < y
    A new subset containing ordered pairs which satisfy this condition will be returned
    """
    relation_set = []
    for x, y in cartesian_product:
        # x < y is our test condition
        if x < y:
            related_pair = (x,y)
            relation_set.append(related_pair)
    return relation_set

def crude_diagram(relation_set):
    """
    accepts a list of ordered pairs called relation_set
    and prints a crude diagram. :)
    """
    for x, y in relation_set:
        print(str(x),"-->",str(y))

def is_function(domain, relation_set):
    values_checked = []
    for x, y in relation_set:
        # we evalute if the first element in the x,y pair is also an element in the domain
        if x in domain:
            # we evaluate the first element of each x, y pair and determine if it has been seen before
            if x not in values_checked:
                # result is false if any two ordered pairs have the same first element
                return False
            else:
                # only executes if x has not been observed in a previous loop
                values_checked.append(x) # keep track of x values we have seen in each loop
        else:
            # result is False if the first element of each ordered pair in the relation_set is not also an element in the domain set
            return False
    return True

# sample sets
A = (1,2,3)
B = (1,3,5)

# the product set A x B
AxB = calc_product(A,B)
print("The domain set A is ",A)
print("The codomain set B is ",B)
print("The cartesian product of A x B is:\n",AxB)
print("The relation set R is:\n",find_relation_set(AxB))

if is_function(A, find_relation_set(AxB)):
    print("The relation set R is also a function from A to B")
else:
    print("The relation set R is not a function from A to B")

crude_diagram(find_relation_set(AxB))
