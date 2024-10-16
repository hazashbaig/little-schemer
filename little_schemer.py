def car(l):
    if (type(l) == list):
        return l[0]
    else:
        raise TypeError("car only works for list")


# print(car(["a", "b", "c"]))
# print(car([["a", "b", "c"], "a", "b", "c"]))
# print(car("hotdog"))
# print(car([]))
# print(car([[["hotdogs"]], ["and"], ["pickle"], "relish"]))
# print(car(car(  [[["hotdogs"]], ["and"]]  )))



def cdr(l):
    if (type(l) == list):
        if (len(l) != 0):
            return l[1:]
        else:
            raise ValueError("cdr doesnt work for empty list")
    else:
        raise TypeError("cdr only works for list")

# print(cdr( ["a", "b", "c"] ))
# print(cdr([["a", "b", "c"], "a", "b", "c"]))
# print(cdr( ["hamburger"] ))
# print(cdr( [["x"], "t", "r"] ))
# print(cdr("hotdogs"))
# print(cdr([]))


# print(car(cdr( [["b"], ["x", "y"], [["c"]]] )))
# print(cdr(cdr( [["b"], ["x", "y"], [["c"]]] )))
# print(cdr(car( ["a", ["b", ["c"]], "d"] )))


def cons(a, l):
    if (type(l) == list):
        return [a] + l
    else:
        raise TypeError("cons only works if l is a list")



# print(cons("peanut", ["butter",  "and",  "jelly"]))
# print(cons(["banana", "and"], ["peanut", "butter",  "and",  "jelly"]))
# print(cons( [["help"], "this"], ["is", "very", [["hard"], "to", "learn"]] ))
# print(cons(["a", "b", ["c"]], []))
# print(cons("a", []))
# print(cons([["a", "b", "c"]], "b"))
# print(cons("a", "b"))



# print( cons("a", car([["b"], "c", "d"])) ) # cons("a", ["b"]) -> ["a", "b"]
# print( cons("a", cdr([["b"], "c", "d"])) ) # cons("a", ["c", "d"]) -> ["a", "c", "d"]


def is_null(l):
    if (type(l) == list):
        return len(l) == 0
    else:
        raise TypeError("null is defined for only lists")

# print(is_null([]))
# print(is_null(["a", "b", "c"]))
# print(is_null("spaghetti"))


def is_atom(expr):
    return type(expr) == str or type(expr) == int


# print(is_atom("Harry"))
# print(is_atom(["Harry", "had", "a", "heap", "of", "apples"]))
# print(is_atom(car(["Harry", "had", "a", "heap", "of", "apples"]))) #True
# print(is_atom(cdr(["Harry", "had", "a", "heap", "of", "apples"]))) # is_atom(["had", "a", "heap", "of", "apples"]) -> false
# print(is_atom(cdr( ["Harry"] ))) # is_atom([]) -> false
# print(is_atom(car(cdr( ["swing", "low", "sweet", "cherry", "oat"] )))) # is_atom(car(["low", "sweet", "cherry", "oat"])) -> is_atom("low") -> True
# print(is_atom(car(cdr( ["swing", ["low", "sweet"], "cherry", "oat"] )))) # is_atom(car( [["low", "sweet"], "cherry", "oat"] )) -> is_atom(["low", "sweet"]) -> false


def is_eq(expr1, expr2):
    if (is_atom(expr1) and is_atom(expr2)):
        return expr1 == expr2
    else:
        raise TypeError("both expr have to be string")


# print(is_eq("Harry", "Harry"))
# print(is_eq("margarine", "butter"))
# print(is_eq([], ["strawberry"]))
# print(is_eq(6, 7))



# print(is_eq(car( ["Mary", "had", "a", "little", "lamb", "chop"] ), "Mary")) #is_eq("Mary", "Mary") -> True
# print(is_eq(cdr( ["soured", "milk"] ), "milk")) # is_eq(["milk"], "milk") -> Error
# print(is_eq(   car(["beans", "beans", "we", "need", "jelly", "beans"]), 
            #    (car(cdr(["beans", "beans", "we", "need", "jelly", "beans"])))  )) # is_eq("beans", car(["beans", "we", "need", "jelly", "beans"])) -> is_eq("beans", "beans") -> True

def lat(l):
    if (is_null(l)):
        return True
    # return is_atom(car(l)) and lat(cdr(l))
    if is_atom(car(l)):
        return lat(cdr(l))
    else:
        return False

# print(lat(["Jack", "Sprat", "could", "eat", "no", "chicken", "fat"]))
# print(lat([["Jack"], "Sprat", "could", "eat", "no", "chicken", "fat"]))
# print(lat(["Jack", ["Sprat", "could"], "eat", "no", "chicken", "fat"]))
# print(lat([]))


# print(is_null([]) or is_atom(["d", "e", "f", "g"]))
# print(is_null(["a", "b", "c"]) or is_null([]))
# print(is_null(["a", "b", "c"]) or is_null(["atom"]))


def is_member(a, l):
    if (is_null(l)):
        return False
    # return is_eq(car(l), a) or is_member(a, cdr(l))
    if (is_eq(car(l), a)):
        return True
    return is_member(a, cdr(l))
    

# print(is_member("tea", ["coffee", "tea", "or", "milk"]))
# print(is_member("poached", ["fried", "eggs", "and", "scrambled", "eggs"]))
# print(is_member("meat", ["mashed", "potatoes", "and", "meat", "gravy"]))
# print(is_member("liver", ["bagels", "and", "lox"]))
# print(is_member("b", [["a"], "b"])) # ERROR 


def rember(a, l):
    if (is_null(l)):
        return l
    if (is_eq(car(l), a)):
        return cdr(l)
    return cons(car(l), rember(a, cdr(l)))


# print(rember("mint", ["lamb", "chops", "and", "mint", "jelly"]))
# print(rember("mint", ["lamb", "chops", "and", "mint", "flavoured", "mint", "jelly"]))
# print(rember("toast", ["bacon", "lettuce", "and", "tomato"]))
# print(rember("cup", ["coffee", "cup", "tea", "cup", "and", "hick", "cup"]))


def rember_all(a, l):
    if (is_null(l)):
        return l
    if (is_eq(car(l), a)):
        return rember_all(a, cdr(l))
    return cons(car(l), rember_all(a, cdr(l)))


# print(rember_all("mint", ["lamb", "chops", "and", "mint", "jelly"]))
# print(rember_all("mint", ["lamb", "chops", "and", "mint", "flavoured", "mint", "jelly"]))
# print(rember_all("toast", ["bacon", "lettuce", "and", "tomato"]))
# print(rember_all("cup", ["coffee", "cup", "tea", "cup", "and", "hick", "cup"]))

# k is tracking variable
# tracking variable tells us how many times it is left to reccurse
# if tracking variable is 0 no further recursion should take place
#       and we should return whatever answer we have currently
def rember_k(a, l, k): 
    if (is_null(l) or k <= 0):
        return l
    if (is_eq(car(l), a)):
        return rember_k(a, cdr(l), k-1)
    return cons(car(l), rember_k(a, cdr(l), k))

# print(rember_k("mint", ["lamb", "mint", "and", "mint", "flavoured", "mint", "jelly"], -1))
# print(rember_k("mint", ["lamb", "mint", "and", "mint", "flavoured", "mint", "jelly"], 0))
# print(rember_k("mint", ["lamb", "mint", "and", "mint", "flavoured", "mint", "jelly"], 1))
# print(rember_k("mint", ["lamb", "mint", "and", "mint", "flavoured", "mint", "jelly"], 2))
# print(rember_k("mint", ["lamb", "mint", "and", "mint", "flavoured", "mint", "jelly"], 3))
# print(rember_k("mint", ["lamb", "mint", "and", "mint", "flavoured", "mint", "jelly"], 4))

def firsts(l):
    if (is_null(l)):
        return l
    return cons(car(car(l)), firsts(cdr(l)))


# print(firsts([["a", "b"], ["c", "d"], ["e", "f"]])) # ["a", "c", "e"]
# print(firsts([["apple", "peach", "pumpkin"], ["plum", "pear", "cherry"], ["grape", "raisin", "pea"], ["bean", "carrot", "eggplant"]]))
# print(firsts([]))
# print(firsts( [[["five", "plums"], "four"], ["eleven", "green", "oranges"], [["no"], "more"]] ))
# print(firsts([["a", "b"], "c", "d", ["e", "f"]]))
# # [] -> []
# [["a", "b"]] -> "a" + 
# [["a"], ["b"]] -> car(car(l)) => "a" + firsts([["b"]]) -> "a" + "b" + firsts([[]]) -> "a" + "b" + []

def safe_firsts(l):

    # def non_empty_list(l):
    #     return type(l) == list and len(l) > 0
    
        
    if (is_null(l)):
        return l

    if (type(car(l)) != list or len(car(l)) == 0):
        return safe_firsts(cdr(l))

    # if (non_empty_list(car(l))):
    #     return safe_firsts(cdr(l))
    else:
        return cons(car(car(l)), safe_firsts(cdr(l)))
        

# print(safe_firsts([["a", "b"], "c", "d", ["e", "f"]]))
# print(safe_firsts([["a", "b"], [], "d", ["e", "f"]]))

def seconds(l):
    if (is_null(l)):
        return l
    return cons( car(cdr(car(l))), seconds(cdr(l)) )

# print(seconds([["a", "b"], ["c", "d"], ["e", "f"]]))


def insertR(new, old, l):
    if (is_null(l)):
        return l
    if (is_eq(car(l), old)):
        return cons(old, cons(new, cdr(l)))
    return cons(car(l), insertR(new, old, cdr(l)))
    

# print(insertR("topping", "fudge", ["icecream", "with", "fudge", "for", "desert"]))
# print(insertR("jalepeno", "and", ["tacos", "tamales", "and", "salsa"]))
# print(insertR("e", "d", ["a", "b", "c", "d", "f", "g"]))

def insertL(new, old, l):
    if (is_null(l)):
        return l
    if (is_eq(car(l), old)):
        return cons(new, l)
    return cons(car(l), insertL(new, old, cdr(l)))

# print(insertL("topping", "fudge", ["icecream", "with", "fudge", "for", "desert"]))
# print(insertL("jalepeno", "and", ["tacos", "tamales", "and", "salsa"]))
# print(insertL("e", "d", ["a", "b", "c", "d", "f", "g"]))


def subst(new, old, l):
    if(is_null(l)):
        return l
    if (is_eq(car(l), old)):
        return cons(new, cdr(l))
    return cons(car(l), subst(new, old, cdr(l)))

# print(subst("topping", "fudge", ["icecream", "with", "fudge", "for", "desert"]))

def subst2(new, o1, o2, l):
    if(is_null(l)):
        return l
    if (is_eq(o1, car(l)) or is_eq(o2, car(l))):
        return cons(new, cdr(l))
    return cons(car(l), subst2(new, o1, o2, l))

# print(subst2("vanilla", "banana", "chocolate", ["banana", "icecream", "with", "chocolate", "topping"]))


def multi_rember(a, l): # same as rember_all()
    if (is_null(l)):
        return l
    if (is_eq(car(l), a)):
        return multi_rember(a, cdr(l))
    return cons(car(l), multi_rember(a, cdr(l)))

# print(multi_rember("cup", ["coffee", "cup", "tea", "cup", "and", "hick", "cup"]))

def multi_insertR(new, old, l):
    if (is_null(l)):
        return l
    if (is_eq(car(l), old)):
        return cons(car(l), cons(new, multi_insertR(new, old, cdr(l)))) # did a mistake before forgot to take cdr(l)
    return cons(car(l), multi_insertR(new, old, cdr(l)))

# print(multi_insertR("lol", "cup", ["coffee", "cup", "tea", "cup", "and", "hick", "cup"]))


def multi_insertL(new : str, old : str, l : list) -> list:
    if (is_null(l)):
        return l
    if (is_eq(car(l), old)):
        return cons(new, cons(old, multi_insertL(new, old, cdr(l))))
    return cons(car(l), multi_insertL(new, old, cdr(l)))

# print(multi_insertL("lol", "cup", ["coffee", "cup", "tea", "cup", "and", "hick", "cup"]))
# print(multi_insertL("fried", "fish", ["chips", "and", "fish", "or", "fish", "and", "fried"]))


def multi_subst(new, old, l):
    if (is_null(l)):
        return l
    if (is_eq(car(l), old)):
        return cons(new, multi_subst(new, old, cdr(l)))
    return cons(car(l), multi_subst(new, old, cdr(l)))

# print(multi_subst("CUP", "cup", ["coffee", "cup", "tea", "cup", "and", "hick", "cup"]))



### Chapter - 4   (Numbers Games)

# print(is_atom(14))



def is_zero(n):
    return n == 0
    
def add1(n):
    return n + 1

def sub1(n):
    if (is_zero(n)):
        raise ValueError("Cannot subtract zero further")
    return n - 1

def plus(n1, n2):
    if (is_zero(n2)):
        return n1
    return plus(add1(n1), sub1(n2))

# print(plus(5, 3))

def minus(n1, n2):
    if (is_zero(n2)):
        return n1
    return minus(sub1(n1), sub1(n2))

# print(minus(3, 14))

def is_num(x):
    return type(x) == int

def is_tuple(l):
    if (is_null(l)):
        return True

    if (is_num(car(l))):
        return is_tuple(cdr(l))
    return False

    # if (not is_num(car(l))):
    #     return False
    # return is_tuple(cdr(l))


# print(is_tuple([8, 4, 5]))
# print(is_tuple([8, 4, "a", 5]))
# print(is_tuple([8, 4, ["a"], 5]))
# print(is_tuple([3, [7, 4], 13, 9]))

def sum_tuple(tup):
    if (is_null(tup)):
        return 0
    return plus(car(tup), sum_tuple(cdr(tup)))

# print(sum_tuple([3, 5, 2, 8]))
# print(sum_tuple([15, 6, 7, 12, 3]))

def sum_tuple_acc(tup, acc=0): # acc = accumulator
    if (is_null(tup)):
        return acc
    return sum_tuple_acc(cdr(tup), plus(acc, car(tup)))

# print(sum_tuple_acc([3, 5, 2, 8]))
# print(sum_tuple_acc([15, 6, 7, 12, 3]))

def mul(n1, n2):
    if (is_zero(n1) or is_zero(n2)):
        return 0
    return plus(n1, mul(n1, sub1(n2))) # 4 x 13 = 4 + (4 x 12)

# print(mul(5, 3))
# print(mul(4, 13))

def pow(n1, n2):
    if (is_zero(n2)):
        return 1
    return mul(n1, pow(n1, sub1(n2))) # 2^8 = 2 x 2^7

# print(pow(2, 5))


# def add_tuples(tup1, tup2):
#     if (is_null(tup1) and is_null(tup2)):
#         return tup1
#     return cons(plus(car(tup1), car(tup2)), add_tuples(cdr(tup1), cdr(tup2)))

# print(add_tuples([1,2, 3], [4, 5, 6]))


def add_tuples(tup1, tup2): # [1, 2, 3] [4, 5, 6, 100]-> [5, 7, 9]
    if (is_null(tup1) or is_null(tup2)):
        return []
    return cons(plus(car(tup1), car(tup2)), add_tuples(cdr(tup1), cdr(tup2)))

# print(add_tuples([1, 2, 3], [4, 5, 6, 100]))

def add_tuples_ext(tup1, tup2): # [1, 2, 3] [4, 5, 6, 100]-> [5, 7, 9, 100]
    if (is_null(tup1) and is_null(tup2)):
        return []
    elif (is_null(tup1)):
        return tup2
    elif (is_null(tup2)):
        return tup1
    else:
       return cons(plus(car(tup1), car(tup2)), add_tuples_ext(cdr(tup1), cdr(tup2)))

# print(add_tuples_ext([1, 2, 3], [4, 5, 6, 100]))


def greater(n1, n2): # True if n1 > n2 or else False
    if (is_eq(n1, n2)):
        return False
    elif (is_zero(n1)):
        return False
    elif (is_zero(n2)):
        return True
    else:
        return greater(sub1(n1), sub1(n2))

# print(greater(12, 5))
# print(greater(12, 51))
# print(greater(3, 3))


def less_than(n1, n2):
    if (is_eq(n1, n2)):
        return False
    if (is_zero(n1)):
        return True
    if (is_zero(n2)):
        return False

    return less_than(sub1(n1), sub1(n2))


# print(less_than(12, 5))
# print(less_than(12, 51))
# print(less_than(3, 3))

def is_same_num(n1, n2):
    if (is_zero(n1) and is_zero(n2)):
        return True
    if (is_zero(n1)):
        return False
    if (is_zero(n2)):
        return False
    return is_same_num(sub1(n1), sub1(n2))

# print(is_same_num(12, 5))
# print(is_same_num(12, 51))
# print(is_same_num(3, 3))


# 14 / 3 = 1 + (11 / 3) = 1 + 1 + (8 / 3) = 1 + 1 + 1 + (5 / 3) = 1 + 1 + 1 + 1 + (2/3) = 1 + 1 + 1 + 1 + 0
def div(n1, n2):
    if (less_than(n1, n2)):
        return 0
    return add1(div(minus(n1, n2), n2))

# print(div(3, 3))


def length(l):
    if (is_null(l)):
        return 0
    return add1(length(cdr(l)))

# print(length(["a", "b", "c"]))

def pick(n : int, l : list):
    if (less_than(n, 1)):
        raise ValueError("n cannot be less than 1")
    if (is_same_num(n, 1)):
        return car(l)
    return pick(sub1(n), cdr(l))


# print(pick(0, ["a", "b", "c", "d", "e", "f"])) # ERROR
# print(pick(2, [1, 2, 3, 4, 5, 6]))
# print(pick(1, ["a", "b", "c", "d", "e", "f"]))
# print(pick(4, ["a", "b", "c", "d", "e", "f"]))
# print(pick(50, ["a", "b", "c", "d", "e", "f"])) # ERROR


def rempick(n : int, l : list) -> list:
    if (is_null(l)):
        return l
    if (is_zero(sub1(n))):
        return cdr(l)
    return cons(car(l), rempick(sub1(n), cdr(l)))

# print(rempick(3, ["hotdogs", "with", "hot", "mustard"]))


def no_nums_lat(l : list) -> list:
    if (is_null(l)):
        return l
    if (is_num(car(l))):
        return no_nums_lat(cdr(l))
    return cons(car(l), no_nums_lat(cdr(l)))
    
# print(no_nums_lat([5, "pears", 6, "prunes", 9, "dates"]))


def all_nums(l : list) -> list:
    if (is_null(l)):
        return l
    if (is_num(car(l))):
        return cons(car(l), all_nums(cdr(l)))
    return all_nums(cdr(l))

# print(all_nums([5, "pears", 6, "prunes", 9, "dates"]))

def eqan(a1, a2) -> bool:
    if (is_num(a1) and is_num(a2)):
        return is_same_num(a1, a2)
    if (is_num(a1) or is_num(a2)):
        return False
    return is_eq(a1, a2)

# print(eqan(1, 1))
# print(eqan(1, "a"))
# print(eqan("a", "a"))
# print(eqan("a", "b"))
# print(eqan(1, 2))


def occur(a : str, l : list) -> int:
    if (is_null(l)):
        return 0
    if (is_eq(car(l), a)):
        return 1 + occur(a, cdr(l))
    return occur(a, cdr(l))

# print(occur("a", ["a", "b", "a", "a"]))

def one(n : int) -> bool:
    return is_same_num(n, 1)
        
# print(one(1))
# print(one(0))
# print(one(2))


### Chapter - 5 

def rember_star(a, l : list) -> list:
    if (len(l) == 0):
        return []
    if type(l[0]) != list:
        if (l[0] == a):
            return rember_star(a, l[1:])
        else:
            return [l[0]] + rember_star(a, l[1:])
    else:
        # return cons(rember_star(a, l[0]), rember_star(a, l[1:]))
        return [rember_star(a, l[0])] + rember_star(a, l[1:])



# cup, [[cup, coffee], coffee] -> [[coffee], coffee]
# cup, [[cup, coffee], coffee] -> rember_star(cup, [cup, coffee]) + rember_star(cup, [coffee])
#                              ->  [coffee] + [coffee] -> [coffee, coffee]
# print(rember_star("cup", [["coffee"], "cup", [["tea"], "cup"], ["and", ["hick"]], "cup"]))






def insertR_star(new, old, l : list) -> list:
    if (len(l) == 0):
        return []
    if (type(l[0]) != list):
        if (l[0] == old):
            return [l[0], new] + insertR_star(new, old, l[1:])
        else:
            return [l[0]] + insertR_star(new, old, l[1:])
    else:
        return [insertR_star(new, old, l[0])] + insertR_star(new, old, l[1:])

# print(insertR_star("roast", "chuck", [["how", "much", ["wood"]],
#                                       "could",
#                                       [["a", ["wood"], "chuck"]],
#                                       [[["chuck"]]], 
#                                       ["if", ["a"], [["wood", "chuck"]]], 
#                                       "could", "chuck", "would"]))

# "a", "b", ["a", ["b"], "b"] -> ["a", ["b", "a"], "b", "a"]
# print(insertR_star("a", "b", ["a", ["b"], "b"]))
# print(insertR_star("a", "b", ["a"]))


def occur_star(a, l : list) -> int:
    if (len(l) == 0):
        return 0
    if (type(l[0] != list and l[0] == a)):
        return 1 + occur_star(a, l[1:])
    if (type(l[0] != list and l[0] != a)):
        return occur_star(a, l[1:])
    return occur_star(a, l[0]) + occur_star(a, l[1:])

# print(occur_star("banana", [["banana"],
#                             ["split", [[[["banana", "ice"]]],
#                                         ["cream", ["banana"]],
#                                         "sherbet"]],
#                             ["banana"],
#                             ["bread"],
#                             ["banana", "brandy"]]))

def subst_star(new, old, l : list) -> list:
    if (len(l) == 0):
        return []
    if (type(l[0]) != list and l[0] == old):
        return [new] + subst_star(new, old, l[1:])
    if (type(l[0]) != list and l[0] != old):
        return [l[0]] + subst_star(new, old, l[1:])
    return [subst_star(new, old, l[0])] + subst_star(new, old, l[1:])

# print(subst_star("ice", "banana", [["banana"],
#                             ["split", [[[["banana", "ice"]]],
#                                         ["cream", ["banana"]],
#                                         "sherbet"]],
#                             ["banana"],
#                             ["bread"],
#                             ["banana", "brandy"]]))

def insertL_star(new, old, l : list) -> list:
    if (len(l) == 0):
        return []
    if (type(l[0]) != list and l[0] == old):
        return [new, old] + insertL_star(new, old, l[1:])
    if (type(l[0]) != list and l[0] != old):
        return [l[0]] + insertL_star(new, old, l[1:])
    return [insertL_star(new, old, l[0])] + insertL_star(new, old, l[1:])


# print(insertL_star("roast", "chuck", [["how", "much", ["wood"]],
#                                       "could",
#                                       [["a", ["wood"], "chuck"]],
#                                       [[["chuck"]]], 
#                                       ["if", ["a"], [["wood", "chuck"]]], 
#                                       "could", "chuck", "wood"]))



def member_star(a, l : list) -> bool:
    if (len(l) == 0):
        return False
    if (type(l[0]) != list):
        if (l[0] == a):
            return True
        else:
            return member_star(a, l[1:])
    else:
        return member_star(a, l[0]) or member_star(a, l[1:])

# print(member_star("chips", [["potato"], ["chips", [["with"], "fish"], ["chips"]]]))


def leftmost(l : list):
    if (len(l) == 0):
        raise ValueError("Theres no element in the list")
    if (type(l[0]) != list):
        return l[0]
    else:
        return leftmost(l[0])
    
# print(leftmost([["potato"], ["chips", [["with"], "fish"], ["chips"]]]))
# print(leftmost([[["hot"], ["tuna", ["and"]]], "cheese"]))


def eqlist(l1 : list, l2 : list) -> bool:
    if (len(l1) == 0 and len(l2) == 0):
        return True
    if (len(l1) == 0 or len(l2) == 0):
        return False
    if (type(l1[0]) != list and type(l2[0]) != list):
        if (l1[0] != l2[0]):
            return False
        else:
            return eqlist(l1[1:], l2[1:])
    elif (type(l1[0]) != list or type(l2[0]) != list):
        return False
    else:
        return eqlist(l1[0], l2[0]) and eqlist(l1[1:], l2[1:])
    

# print(eqlist(["strawberry", "ice", "cream"], ["strawberry", "ice", "cream"]))
# print(eqlist(["strawberry", "ice", "cream"], ["strawberry", "cream", "ice"]))
# print(eqlist(["banana", [["split"]]], [["banana"], ["split"]]))
# print(eqlist(["beef", [["sauage"]], ["and", ["soda"]]], ["beef", [["sauage"]], ["and", ["soda"]]]))
    
def eqlist(l1 : list, l2 : list) -> bool:
    if (len(l1) == 0 and len(l2) == 0):
        return True
    if (len(l1) == 0 or len(l2) == 0):
        return False
    if (equal(l1[0], l2[0])):
        return eqlist(l1[1:], l2[1:])
    else:
        return False


def equal(s1, s2) -> bool:
    if (is_atom(s1) and is_atom(s2)):
        return eqan(s1, s2)
    if (is_atom(s1) or is_atom(s2)):
        return False
    else:
        return eqlist(s1, s2)

# print(equal(1, "1"))


### Chapter - 6 

# def numbered(item) -> bool:
#     return type(item) == int or item in ["x", "+", "-", "/", "^"]


# def numbered_list(l):
#     if (len(l) == 0):
#         return True
#     if (type(l[0]) == list):
#         return numbered_list(l[0]) and numbered_list(l[1:])
#     else:
#         return numbered(l[0]) and numbered_list(l[1:])
    
# def numbered_star(expr):
#     if (type(expr) == list):
#         return numbered_list(expr)
#     return numbered(expr)
    
# print(numbered_star([[3,"+", 4], "^", 5]))
# print(numbered_star([3, "+", [4, "^", 5]]))
# print(numbered_star([2, "x", "sausage"]))
# print(numbered_star(3))
# print(numbered_star(["+"]))
# print(numbered_star("+"))
# print(numbered_star([]))





# print(numbered_list([[3,"+", 4], "^", 5]))
# print(numbered_list([3, "+", [4, "^", 5]]))
# print(numbered_list([2, "x", "sausage"]))
# print(numbered(3))
# print(numbered_list(["+"]))
# print(numbered("+"))
# print(numbered_list([]))


def numbered(expr : int | str | list):
    if (type(expr) != list):
        return type(expr) == int or expr in ["x", "+", "-", "/", "^"]
    if (len(expr) == 0):
        return True
    return numbered(expr[0]) and numbered(expr[1:])

# print(numbered([[3,"+", 4], "^", 5]))
# print(numbered([3, "+", [4, "^", 5]]))
# print(numbered([2, "x", "sausage"]))
# print(numbered(3))
# print(numbered(["+"]))
# print(numbered("+"))
# print(numbered([]))



def value(expr):
    if (type(expr) != list):
        if (type(expr) == int):
            return expr
        raise ValueError("Invalid Expression")
    
    if (len(expr) == 1):
        return value(expr[0])
    
    if (len(expr) != 3):
        raise ValueError("Invalid Expression")
    
    lhs = expr[0]
    op = expr[1]
    rhs = expr[2]
    if (op == "+"):
        return value(lhs) + value(rhs)
    if (op == "x"):
        return value(lhs) * value(rhs)
    if (op == "-"):
        return value(lhs) - value(rhs)
    if (op == "/"):
        return value(lhs) / value(rhs)
    if (op == "^"):
        return value(lhs) ** value(rhs)
    else:
        raise ValueError("Invalid Expression")
    

    



# print(value(13))
# print(value([13]))
# print(value([1, "+", 3]))
# print(value([1, "+", [3, "x", 4]]))
# print(value([[1, "+", 3], "x", 4]))
# print(value([[1, "+", 2], "x", [3, "+", 4]]))

# print(value([]))
# print(value("+"))
# print(value([1, "+"]))
# print(value(["+", 3]))
# print(value(["+"]))
# print(value([1, "+", "-", 3]))
# print(value([1, "+", 2, "+", 3]))




### Chapter - 7
def unique(l : list) -> bool:
    if (len(l) == 0):
        return True
    if (l[0] not in l[1:]):
        return unique(l[1:])
    return False


# print(unique(["apple", "peaches", "apple", "plum"]))
# print(unique(["apples", "peaches", "pears", "plums"]))
# print(unique(["apple", 3, "pear", 4, 9, "apple", 3, 4]))


def make_unique(l : list) -> list:
    if (len(l) == 0):
        return []
    if (l[0] in l[1:]):
        return make_unique(l[1:])
    return [l[0]] + make_unique(l[1:])

# print(make_unique(["apple", "peaches", "apple", "plum"]))
# print(make_unique(["apple", "peach", "pear", "plum", "apple", "lemon", "peach"]))
# print(make_unique(["apple", 3, "pear", 4, 9, "apple", 3, 4]))

def make_unique_by_removing(l):
    if (len(l) == 0):
        return []
    return [l[0]] + rember_all(l[0], make_unique_by_removing(l[1:]))


# print(make_unique_by_removing(["apple", "peaches", "apple", "plum"]))
# print(make_unique_by_removing(["apple", "peach", "pear", "plum", "apple", "lemon", "peach"]))
# print(make_unique_by_removing(["apple", 3, "pear", 4, 9, "apple", 3, 4]))


def subset(set1, set2) -> bool:
    if (len(set1) == 0):
        return True
    if (set1[0] in set2):
        return subset(set1[1:], set2)

    return False

# print(subset([5, "chicken", "wings"], [5, "hamburgers", 2, "pieces", "fried", "chicken", "and", "light", "duckling", "wings"]))
# print(subset([4, "pounds", "of", "horseradish"], ["four", "pounds", "chicken", "and", 5, "ounces", "horseradish"]))

def eqset(set1, set2) -> bool:
    return subset(set1, set2) and subset(set2, set1)

# print(eqset([6, "large", "chickens", "with", "wings"], [6, "chickens", "with", "large", "wings"]))

def intersect(set1, set2) -> bool:
    if (len(set1) == 0):
        return False
    # if (set1[0] in set2):
    #     return True
    return set1[0] in set2 or intersect(set1[1:], set2)

# print(intersect(["stewed", "tomatoes", "and", "macaroni"], ["macaroni", "and", "cheese"]))
# print(intersect(["a"], ["b"]))
# print(intersect(["a"], ["b", "a"]))

def union(set1, set2):
    if (len(set1) == 0):
        return set2
    if (set1[0] in set2):
        return union(set1[1:], set2)
    return [set1[0]] + union(set1[1:], set2)

# print(union(["stewed", "tomatoes", "and", "macaroni", "casserole"], ["macaroni", "and", "cheese"]))


def diff(set1, set2):
    if (len(set1) == 0):
        return []
    if (set1[0] in set2):
        return diff(set1[1:], set2)
    return [set1[0]] + diff(set1[1:], set2)

# print(diff(["stewed", "tomatoes", "and", "macaroni", "casserole"], ["macaroni", "and", "cheese"]))



def common(set1, set2):
    if (len(set1) == 0):
        return []
    if (set1[0] in set2):
        return [set1[0]] + common(set1[1:], set2)
    return common(set1[1:], set2)

# print(common(["b", "c"], ["a"]))

def intersect_all(lset):
    if (len(lset) == 1):
        return lset
    if (len(lset) == 2):
        return common(lset[0], lset[1])
    return common(lset[0], intersect_all(lset[1:]))

# print(intersect_all([["a", "b", "c"], ["c", "a", "d", "e"], ["e", "f", "g", "h", "a", "b", "c"]]))

def pair(l):
    if (len(l) == 2):
        return True
    return False


# print(pair([]))
# print(pair(["a", 3]))
# print(pair(["a"]))
# print(pair(["a", "a", "a"]))
# print(pair(["pear", "pear"]))
# print(pair([[2], ["pair"]]))

def rel(l):
    if (len(l) == 0):
        return True
    return pair(l[0]) and rel(l[1:])

# print(rel(["apples", "peaches", "pumpkin", "pie"]))
# print(rel([["apples", "peaches"], ["pumpkin", "pie"], ["apples", "peaches"]]))
# print(rel([[4, 5], [4, 2], [3, 4]]))


def firsts(l):
    if (len(l) == 0):
        return []
    return [l[0][0]] + firsts(l[1:])

def fun(l):
    if (len(l) == 0):
        return True
    return unique(firsts(l))

# print(fun([[4, 3], [4, 2], [7, 6], [6, 2], [3, 4]]))
# print(fun([[8, 3], [4, 2], [7, 6], [6, 2], [3, 4]]))
# print(fun([["d", 4], ["b", 0], ["b", 9], ["e", 5]]))



def revrel(l):
    if (len(l) == 0):
        return []
    return [[l[0][1],l[0][0]]] + revrel(l[1:])


# print(revrel([[8, "a"], ["pumpkin", "pie"], ["got", "sick"]]))

def seconds(l):
    if (len(l) == 0):
        return []
    return [l[0][1]] + seconds(l[1:])

# print(seconds([[8, 3], [4, 2], [7, 6], [6, 2], [3, 4]]))

def fullfun(l):
    if (len(l) == 0):
        return []
        
    return unique(seconds(l))

# print(fullfun([[8, 3], [4, 2], [7, 6], [6, 2], [3, 4]]))
# print(fullfun([[8, 3], [4, 8], [7, 6], [6, 2], [3, 4]]))



def merge_sorted_lists(l1, l2):
    if (is_null(l1) and is_null(l2)):
        return []
    if (is_null(l1)):
        return l2
    if (is_null(l2)):
        return l1
    if (is_same_num(car(l1), car(l2))):
        return cons(car(l1), merge_sorted_lists(cdr(l1), l2))
    if (less_than(car(l1), car(l2))):
        return cons(car(l1), merge_sorted_lists(cdr(l1), l2))
    else:
        return cons(car(l2), merge_sorted_lists(l1, cdr(l2)))

# print(merge_sorted_lists([3, 4], [1, 2, 5]))
# [1, 3], [2, 4] -> cons(1, msl([3], [2, 4])) 
#                   cons(1, cons(2, msl([3], [4])))
#                   cons(1, cons(2, cons(3, msl([], [4]))))
#                   cons(1, cons(2, cons(3, [4])))))


# print(merge_sorted_lists([1, 3], [2, 4]))

def merge_sort(l: list):
    if (len(l) <= 1):
        return l
    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge_sorted_lists(sorted_left, sorted_right)

# print(merge_sort([4, 3, 2, 1, 5]))



# filter takes a list and predicate function,
#     and returns only the elements which satisfy the predicate
# predicate function takes exactly one argument and returns a boolean
#       it tells whether the argument satisfies some condition 
def filter(l, predicate):
    if (is_null(l)):
        return l
    if (predicate(car(l))):
        return cons(car(l), filter(cdr(l), predicate))
    return filter(cdr(l), predicate)


def filter(l, predicate):
    res = []
    for n in l:
        if (predicate(n)):
            res.append(n)
    
    return res

def filter_string(l):
    return filter(l, lambda x : type(x) == str)

# filter([1, 2, 3, 4, 5], greater_than_3) -> [4, 5]
# print(filter([1, 2, 3, 4, 5], greater_than_3))
# print(filter([1, 2, 3, 4, 5], lambda n : n > 3))
# [4, 2, 1, 3, 1, 5] -> 4 [2, 1, 3, 1] [4, 5] -> [2, 1, 3, 1] [4, 5] -> [2, 1, 3, 1, 4, 5]
# [2, 1, 3, 1, 4, 5] -> 2 [1, 1] [3, 4, 5] -> [1, 1] 2 [3, 4, 5] -> [1, 1, 2, 3, 4, 5]
# [1, 1, 2, 3, 4, 5] -> 1 [] [1, 2, 3, 4, 5] 

# [1, 1, 2, 3, 5, 4] ->  1 [] [1, 2, 3, 5, 4]



def quick_sort(l : list) -> list:
    if (len(l) <= 1):
        return l

    pivot = l[0]

    left = filter(l, lambda n : n < pivot)
    middle = filter(l, lambda n : n == pivot)
    right = filter(l, lambda n : n > pivot)

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    return sorted_left + middle + sorted_right



# print(quick_sort([3]))
# print(quick_sort([4, 2, 3, 1, 5]))
# print(quick_sort([2, 1, 3, 4, 5]))
    












def power_limit(a, b):
    max_time = 0
    def _power_limit(a, b, time):
        if (a == 0 or b == 0):
            return time
        if (a == 1 and b == 1):
            return time
        if (a == 1):
            return _power_limit(a+1, b-2, time+1)
        if (b == 1):
            return _power_limit(a-2, b+1, time+1)

        return max(_power_limit(a-2, b+1, time+1), _power_limit(a+1, b-2, time+1))

    max_time = _power_limit(a, b, 0)
    return max_time


# print(power_limit(200, 3))

def power_limit(a, b):
    max_time = 0
    memo = dict()
    def _power_limit(a, b):
        if (a, b) in memo:
            return memo[(a, b)]

        if a == 0 or b == 0:
            memo[(a, b)] = 0
            return 0
        if a == 1 and b == 1:
            memo[(a, b)] = 0
            return 0

        if a == 1:
            result = 1 + _power_limit(a+1, b-2)
        elif b == 1:
            result = 1 + _power_limit(a-2, b+1)
        else:
            result = 1 + max(_power_limit(a-2, b+1), _power_limit(a+1, b-2))

        memo[(a, b)] = result
        return result

    max_time = _power_limit(a, b)
    return max_time


# print(power_limit(3, 5))


# pro way for memoizing
def cache(fn):
    memo = {}
    def wrapper(a, b):
        if (a, b) in memo: return memo[(a, b)]

        res = fn(a, b)

        memo[(a, b)] = res
        return res

    return wrapper

@cache
def power_limit(a, b):

    if a == 0 or b == 0:
        return 0

    if a < 2 and b < 2:
        return 0

    if a == 1:
        return 1 + power_limit(a+1, b-2)
    
    if b == 1:
        return 1 + power_limit(a-2, b+1)
    
    return 1 + max(power_limit(a+1, b-2), power_limit(a-2, b+1))






grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]


class Solution:
    def maxAreaOfIsland(self, grid):

        max_area = 0
        count = 0
        def remove_island(r, c):
            nonlocal count
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            if grid[r][c] == 0:
                return

            count = count + 1
            grid[r][c] = 0

            remove_island(r+1, c)
            remove_island(r-1, c)
            remove_island(r, c+1)
            remove_island(r, c-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    remove_island(i, j)
                    max_area = max(count, max_area)
                    count = 0
        
        return max_area

# s =  Solution()
# print(s.maxAreaOfIsland(grid))




"""

portfolio website in react: https://ethnus-react-task-6.vercel.app/
capstone: https://capstone-six-silk.vercel.app/

http://github.com/parzevl24
https://art-gallery-iota-vert.vercel.app/

https://nosql-finalproj.vercel.app/
https://ethnus-react-task-2.vercel.app/


"""