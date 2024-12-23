import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class SocialMediaGraph:
    def __init__(self):
        self.graph = {}
        self.interests = {}
        
    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = set()
            self.interests[user] = set()
        else:
            logging.warning(f"User {user} already exists!")
            
    def add_friendship(self, user1, user2):
        if user1 not in self.graph and user2 not in self.graph:
            logging.error(f"One or both users ({user1}, {user2}) don't exist in the graph!")
            return
        
        if user1 == user2:
            logging.warning("A user cannot be friends with themselves!")
            return 
        
        if user2 in self.graph[user1]:
            logging.info(f"{user1} and {user2} are already friends!")
            return
        
        if user1 not in self.graph or user2 not in self.graph:
            logging.error(f"One or both users ({user1}, {user2}) don't exist in the graph!")
            return

        self.graph[user1].add(user2)
        self.graph[user2].add(user1)
        logging.info(f"Friendship added between {user1} and {user2}")

    def add_interest(self, user, interest):
        if user not in self.interests:
            logging.error(f"User {user} doesn't exist!")
            return
        
        if interest in self.interests[user]:
            logging.info(f"{user} already has {interest} as an interest!")
            return
            
        self.interests[user].add(interest)
        logging.info(f"Interest {interest} added for user {user}")
        
    def display_graph(self):
        print("\nSocial Media Graph:")
        for user, friends in self.graph.items():
            logging.info(f"{user}: {', '.join(friends) if friends else 'No friends.'}")
        
    def display_interests(self):
        print("\nUser Interests:")
        for user, interests in self.interests.items():
            logging.info(f"{user}: {', '.join(interests) if interests else 'No interests.'}")