import math

# Function to calculate the distance between two branches
def calculate_distance(branch1, branch2):
    lat1, lon1 = branch1
    lat2, lon2 = branch2
    radius = 6371  # Earth's radius in kilometers

    # Convert latitude and longitude to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Calculate the differences
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Use the Haversine formula to calculate the distance
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(lat1_rad) * math.cos(
        lat2_rad
    ) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius * c


# Function to perform the 2-opt swap
def two_opt_swap(route, i, k):
    return route[:i] + route[i : k + 1][::-1] + route[k + 1 :]


# Function to calculate the total distance of a route
def calculate_total_distance(route):
    total_distance = 0
    num_branches = len(route)

    for i in range(num_branches - 1):
        branch1 = route[i]
        branch2 = route[i + 1]
        distance = calculate_distance(
            branch_coordinates[branch1], branch_coordinates[branch2]
        )
        total_distance += distance

    return total_distance


# Function to apply the 2-opt heuristic
def two_opt(branch_coordinates):
    num_branches = len(branch_coordinates)
    best_route = list(branch_coordinates.keys())

    improvement = True
    while improvement:
        improvement = False
        best_distance = calculate_total_distance(best_route)

        for i in range(1, num_branches - 1):
            for k in range(i + 1, num_branches):
                new_route = two_opt_swap(best_route, i, k)
                new_distance = calculate_total_distance(new_route)

                if new_distance < best_distance:
                    best_route = new_route
                    best_distance = new_distance
                    improvement = True

    return best_route, best_distance


# branch coordinates
branch_coordinates = {
    "Branch A": (23.812281, 90.414840),
    "Branch B": (23.746466, 90.376015),
    "Branch C": (23.780853, 90.426593),
    "Branch D": (23.763654, 90.382447),
    "Branch E": (23.791643, 90.407441),
    "Branch F": (23.730501, 90.411591),
    "Branch G": (23.814145, 90.359092),
    "Branch H": (23.755862, 90.368877),
}

# Perform the 2-opt heuristic
optimal_route, optimal_distance = two_opt(branch_coordinates)

# Print the optimal route and distance
print("Optimal Route:", optimal_route)
print("Optimal Distance:", optimal_distance)
