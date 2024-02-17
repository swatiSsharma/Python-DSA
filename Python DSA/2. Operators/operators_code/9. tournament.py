# Ask number of games played in a tournament. Ask the user number of games won and number of games 
# loss. Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)

# Ask user for the number of games played, games won, and games lost
total_games = int(input("Enter the total number of games played: "))
games_won = int(input("Enter the number of games won: "))
games_lost = int(input("Enter the number of games lost: "))

# Calculate number of ties
games_tied = total_games - games_won - games_lost

# Calculate total points
total_points = (games_won * 4) + (games_tied * 2)

# Display the results
print("Number of games tied:", games_tied)
print("Total points:", total_points)