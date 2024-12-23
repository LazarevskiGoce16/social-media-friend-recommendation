# Social Media Graph

## Data Structures & Algorithms Final Project

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

### Example

```sh
Add a user or enter 'EXIT' to exit: Alice
Add an interest for Alice or enter 'EXIT' to exit: Reading
Add a friend for Alice or enter 'EXIT' to exit: Bob
User 'Bob' doesn't exist! Please add them first.
Add a user or enter 'EXIT' to exit: Bob
Add an interest for Bob or enter 'EXIT' to exit: Cooking
Add a friend for Bob or enter 'EXIT' to exit: Alice
Add a user or enter 'EXIT' to exit: EXIT

Social Media Graph:
Alice: Bob
Bob: Alice

User Interests:
Alice: Reading
Bob: Cooking

Enter username to recommend friends based on mutual friends: Alice
No friends recommended for Alice using BFS.

Enter username to recommend friends based on shared interests: Alice
No friends recommended for Alice based on interests.
