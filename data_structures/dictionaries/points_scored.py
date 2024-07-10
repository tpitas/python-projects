points_scored = {"Michael Jordan": 32292, "LeBron James": 40474, "Kevin Durant": 28924,"Stephen Curry": 23668 }

# Add new points scored
points_scored["Magic Johnson"] = 17707

# # Remove Magic Johnson's points scored
# points_scored.pop("Magic Johnson")  

# Get Lebron's points scored
print(points_scored.get("LeBron James"))

# Print all players names 
print(points_scored.keys())

# Print all points scored 
print(points_scored.values())

# list of key-value pairs
print(points_scored.items())