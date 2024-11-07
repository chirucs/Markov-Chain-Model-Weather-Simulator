import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import random

# Defining the states
states=['Sunny','Rainy','Cloudy']

# Defining the transition matrix
# Each row represents the probability of transitioning to a different state
# from the corresponding state in the same order as the states list
# For example, P(Sunny|Sunny) = transition_matrix[0][0]

transition_matrix=[
    [0.8, 0.1, 0.1],  # Probabilities for transitioning from Sunny
    [0.2, 0.6, 0.2],  # Probabilities for transitioning from Rainy
    [0.3, 0.3, 0.4]   # Probabilities for transitioning from Cloudy
]

# function to choose the next state
def get_next_state(current_state_index):
  return np.random.choice(states, p=transition_matrix[current_state_index])

# Simulate weather over a number of days
def simulate_weather(days):
    weather_sequence = []
    current_state_index = random.randint(0, len(states) - 1)  # Random start
    weather_sequence.append(states[current_state_index])

    for _ in range(days - 1):
        current_state_index = states.index(get_next_state(current_state_index))
        weather_sequence.append(states[current_state_index])

    return weather_sequence

# Lets simulate a 30 days of weather
days=30
weather_sequence=simulate_weather(days)
print("Weather Sequence Over 30 Days:")
print(weather_sequence)

# Create a directed graph using networkx
G = nx.DiGraph()

# Add nodes for each state
G.add_nodes_from(states)

# Add edges with transition probabilities as weights
for i, state in enumerate(states):
    for j, next_state in enumerate(states):
        G.add_edge(state, next_state, weight=transition_matrix[i][j])

# Draw the graph
pos = nx.spring_layout(G)  # Position nodes using a force-directed layout
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_weight='bold')
edge_labels = {(state, next_state): f"{transition_matrix[i][j]:.2f}" 
               for i, state in enumerate(states) 
               for j, next_state in enumerate(states)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

# Show the plot
plt.title("Weather State Transition Graph")
plt.show()
