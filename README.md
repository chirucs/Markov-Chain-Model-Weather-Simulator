# Markov Chain Weather Simulator

A Python project that simulates weather patterns using a Markov chain model. The project predicts future weather conditions based on a set of predefined states (Sunny, Rainy, Cloudy) and transition probabilities. It also visualizes the state transitions using a directed graph to better understand how the Markov chain evolves over time.

## Project Description

This project demonstrates the use of Markov chains to model and simulate weather patterns. In a Markov chain, the next state depends only on the current state, making it a powerful tool for modeling systems that have memoryless transitions.

The simulator:
- Uses a transition matrix to define the probabilities of moving from one weather state to another.
- Generates a sequence of weather states over a specified number of days.
- Visualizes the state transitions with a directed graph, showing the probabilities of moving between weather states.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Future Improvements](#future-improvements)
- [License](#license)

## Features
- Simulate weather patterns over a specified number of days.
- Visualize weather state transitions using a directed graph.
- Easily modify the transition matrix to explore different scenarios.

## Getting Started

### Prerequisites
- Python 3.x
- Libraries: `numpy`, `networkx`, `matplotlib`

You can install the required libraries using:
```bash
pip install numpy networkx matplotlib
