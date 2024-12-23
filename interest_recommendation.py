import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def recommend_friends_by_interest(graph, user):
    if user not in graph.graph:
        logging.error(f"User {user} doesn't exist!")
        return []
    
    if user not in graph.interests:
        logging.error(f"User {user} has no interests!")
        return []
    
    user_interests = graph.interests[user]
    interests_overlap_count = {}
    
    for other_user, interests in graph.interests.items():
        if other_user != user:
            if other_user in graph.graph[user]:
                logging.info(f"Skipping {other_user}: Already a friend of {user}!")
                continue
            overlap = len(user_interests.intersection(interests))
            if overlap > 0:
                interests_overlap_count[other_user] = overlap
                logging.info(f"User {other_user} shares {overlap} interest/s with {user}.")
            else:
                logging.info(f"No shared interests between {user} and {other_user}.")
            
    if not interests_overlap_count:
        logging.info(f"No mutual interests found for user {user}.")
        return []
                
    recommended = sorted(interests_overlap_count.items(), key=lambda x: x[1], reverse=True)
    
    recommended_friends = [friend for friend, _ in recommended[:5]]
    return recommended_friends