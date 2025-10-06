def solve(numheads, numlegs):
    """
    Solve the chickens and rabbits puzzle.
    
    Args:
        numheads (int): Total number of heads
        numlegs (int): Total number of legs
    
    Returns:
        tuple: (chickens, rabbits) or "No solution" if impossible
    """
    # chickens + rabbits = numheads
    # 2*chickens + 4*rabbits = numlegs
    
    # From first equation: rabbits = numheads - chickens
    # Substitute into second equation:
    # 2*chickens + 4*(numheads - chickens) = numlegs
    # 2*chickens + 4*numheads - 4*chickens = numlegs
    # -2*chickens = numlegs - 4*numheads
    # chickens = (4*numheads - numlegs) / 2
    
    chickens = (4 * numheads - numlegs) / 2
    rabbits = numheads - chickens
    
    # Check if solution is valid (non-negative integers)
    if chickens >= 0 and rabbits >= 0 and chickens.is_integer() and rabbits.is_integer():
        return int(chickens), int(rabbits)
    else:
        return "No solution"

# Test with the given problem
result = solve(35, 94)
print(f"Chickens and rabbits: {result}")