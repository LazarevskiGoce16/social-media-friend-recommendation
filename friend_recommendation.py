import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def recommend_friends_bfs(graph, user):
    if user not in graph.graph:
        logging.error(f"User {user} doesn't exist!")
        return []

    mutual_friends_count = {}

    for friend in graph.graph[user]:
        for potential_friend in graph.graph[friend]:
            if potential_friend == user:
                continue
            
            if potential_friend in graph.graph[user]:
                logging.info(f"Skipping {potential_friend}: Already a friend of {user}!")
                continue
            
            mutual_friends_count[potential_friend] = mutual_friends_count.get(potential_friend, 0) + 1
            
    if not mutual_friends_count:
        logging.info(f"No mutual friends found for user {user}.")
        return []
                
    recommended = sorted(mutual_friends_count.items(), key=lambda x: x[1], reverse=True)
    recommended_friends = [friend for friend, _ in recommended[:5]]
    
    return recommended_friends
