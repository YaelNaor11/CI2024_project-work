# README

This code implements a **symbolic regression** approach using **genetic programming (GP)**. It evolves mathematical expressions (trees) to fit a given dataset. Below is an overview of its key components:

There are two source files of the project - one type .py and the other type .ipynb. I implemented the project on Google Colab.

## 1. Representation
- Each individual is a tree composed of:
  - **Function nodes**: Add, Subtract, Multiply, Sin, Cos, Power, etc.
  - **Terminal nodes**: Feature variables (\(x_i\)) or random constants.

## 2. Population Initialization
- Uses **ramped half-and-half**, which combines:
  - **Full tree generation**: Produces complete trees up to a maximum depth.
  - **Grow tree generation**: Creates trees with varying depths and structures.
- Ensures a diverse set of initial trees.

## 3. Fitness
- Fitness is measured by the **Mean Squared Error (MSE)** between the tree's output and the training labels.

## 4. Genetic Operators
- **Selection**: Tournament selection.
- **Crossover**: Subtrees are swapped between two parent trees.
- **Mutation**: Two types:
  1. **Point mutation**: A node is replaced with a different one.
  2. **Expansion mutation**: A terminal node is replaced with a new subtree.

## 5. Adaptive Parameters
- Parameters can dynamically adjust based on performance to balance exploration and exploitation:
  - Crossover rate, Mutation rate, Tournament size, Maximum tree depth
