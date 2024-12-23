from social_media_graph import SocialMediaGraph
from friend_recommendation import recommend_friends_bfs
from interest_recommendation import recommend_friends_by_interest

def main():
    graph = SocialMediaGraph()
    users_list = []
    
    while True:
        user = input("Add a user or enter 'EXIT' to exit: ").strip()
        if user.lower() == "exit":
            break 
        if user not in users_list:
            graph.add_user(user)
            users_list.append(user)
        else:
            print(f"User {user} already exists! Try adding a different one.")
            
        while True:
            interest = input(f"Add an interest for {user} or enter 'EXIT' to exit: ").strip()
            if interest.lower() == "exit":
                break
            graph.add_interest(user, interest)
            
        while True:
            friend = input(f"Add a friend for {user} or enter 'EXIT' to exit: ").strip()
            if friend.lower() == "exit":
                break 
            if friend == user:
                print(f"User {friend} cannot be friends with themselves!")
            elif friend not in users_list:
                print(f"User '{friend}' doesn't exist! Please add them first.")
            else:
                graph.add_friendship(user, friend)
                
    graph.display_graph()
    graph.display_interests()
    
    # Breadth-First Search
    user_to_check_bfs = input("\nEnter username to recommend friends based on mutual friends: ")
    recommended_friends_bfs = recommend_friends_bfs(graph, user_to_check_bfs)
    if recommended_friends_bfs:
        print(f"Recommended friends for {user_to_check_bfs} (BFS): {', '.join(recommended_friends_bfs)}")
    else:
        print(f"No friends recommended for {user_to_check_bfs} using BFS.")
        
    # Shared Interests Search
    user_to_check_interest = input("\nEnter username to recommend friends based on shared interests: ")
    recommended_friends_interest = recommend_friends_by_interest(graph, user_to_check_interest)
    if recommended_friends_interest:
        print(f"Recommended friends for {user_to_check_interest} (Interests): {', '.join(recommended_friends_interest)}")
    else:
        print(f"No friends recommended for {user_to_check_interest} based on interests.")
            
if __name__ == "__main__":
    main()