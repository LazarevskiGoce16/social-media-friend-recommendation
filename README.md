# Data Structures & Algorithms Final Project

## Social Media Graph

This project implements a social media graph with functionalities to add users, manage friendships, and track user interests. It also includes friend recommendation systems based on mutual friends and shared interests.

## Features

- **Add Users**: Add new users to the social media graph.
- **Manage Friendships**: Create friendships between users.
- **Track Interests**: Assign interests to users.
- **Friend Recommendations**:
  - **Based on Mutual Friends**: Recommend friends using a Breadth-First Search (BFS) approach.
  - **Based on Shared Interests**: Recommend friends based on common interests.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Ensure you have Python installed.

## Usage

1. **Run the main program**:
    ```sh
    python main.py
    ```

2. **Follow the prompts** to add users, interests, and friendships.

3. **Get Friend Recommendations**:
   - Based on mutual friends.
   - Based on shared interests.

### Example Interaction

1. **Adding Users and Interests**:
    ```sh
    Add a user or enter 'EXIT' to exit: Alice
    Add an interest for Alice or enter 'EXIT' to exit: Reading
    Add an interest for Alice or enter 'EXIT' to exit: Music
    Add an interest for Alice or enter 'EXIT' to exit: EXIT
    Add a friend for Alice or enter 'EXIT' to exit: Bob
    User 'Bob' doesn't exist! Please add them first.
    
    Add a user or enter 'EXIT' to exit: Bob
    Add an interest for Bob or enter 'EXIT' to exit: Cooking
    Add an interest for Bob or enter 'EXIT' to exit: Traveling
    Add an interest for Bob or enter 'EXIT' to exit: EXIT
    Add a friend for Bob or enter 'EXIT' to exit: Alice
    
    Add a user or enter 'EXIT' to exit: Charlie
    Add an interest for Charlie or enter 'EXIT' to exit: Reading
    Add an interest for Charlie or enter 'EXIT' to exit: Traveling
    Add an interest for Charlie or enter 'EXIT' to exit: EXIT
    Add a friend for Charlie or enter 'EXIT' to exit: Alice
    Add a friend for Charlie or enter 'EXIT' to exit: Bob
    
    Add a user or enter 'EXIT' to exit: EXIT
    ```

2. **Displaying the Graph and Interests**:
    ```sh
    Social Media Graph:
    Alice: Bob, Charlie
    Bob: Alice, Charlie
    Charlie: Alice, Bob

    User Interests:
    Alice: Reading, Music
    Bob: Cooking, Traveling
    Charlie: Reading, Traveling
    ```

3. **Recommending Friends Based on Mutual Friends**:
    ```sh
    Enter username to recommend friends based on mutual friends: Alice
    Recommended friends for Alice (BFS): No friends recommended for Alice using BFS.
    
    Enter username to recommend friends based on mutual friends: Bob
    Recommended friends for Bob (BFS): No friends recommended for Bob using BFS.
    
    Enter username to recommend friends based on mutual friends: Charlie
    Recommended friends for Charlie (BFS): No friends recommended for Charlie using BFS.
    ```

4. **Recommending Friends Based on Shared Interests**:
    ```sh
    Enter username to recommend friends based on shared interests: Alice
    Recommended friends for Alice (Interests): Charlie
    
    Enter username to recommend friends based on shared interests: Bob
    Recommended friends for Bob (Interests): Charlie
    
    Enter username to recommend friends based on shared interests: Charlie
    Recommended friends for Charlie (Interests): Alice, Bob
    ```

### Explanation

- Users **Alice**, **Bob**, and **Charlie** are added to the social media graph.
- Interests are assigned to each user.
- Friendships are created between the users.
- The graph and interests are displayed to show the current state.
- Friend recommendations are generated based on mutual friends (BFS) and shared interests.

In this example:
- **Alice** and **Charlie** share the interest "Reading", so Charlie is recommended as a friend to Alice based on shared interests.
- **Bob** and **Charlie** share the interest "Traveling", so Charlie is recommended as a friend to Bob based on shared interests.
- **Charlie** is recommended Alice and Bob based on shared interests "Reading" and "Traveling" respectively.

## Logging

The system uses Python's `logging` module to provide informative messages about the operations being performed, such as adding users, friendships, and interests, as well as any errors or warnings.

## File Structure

- `main.py`: Main script to run the program.
- `social_media_graph.py`: Contains the `SocialMediaGraph` class.
- `friend_recommendation.py`: Contains the BFS-based friend recommendation function.
- `interest_recommendation.py`: Contains the interest-based friend recommendation function.
