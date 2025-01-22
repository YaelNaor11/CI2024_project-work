README

 

This code implements a symbolic regression approach using genetic programming (GP). We evolve mathematical expressions (trees) to fit a given dataset. Below is a short overview:

       1.     Representation

           •   Each individual is a tree composed of function nodes (e.g., add, subtract, multiply, sin, cos, power) and terminal nodes (variables  x_i  or random constants).

       2.     Population Initialization

           •   We use ramped half-and-half, a mix of the full and grow tree-generation methods, ensuring diverse initial trees.

       3.     Fitness

           •   The fitness is the mean squared error (MSE) between the tree’s output and the training labels.

       4.     Genetic Operators

           •   Selection: Tournament selection.

           •   Crossover: Swap subtrees of two parent trees.

           •   Mutation: Either change a node (point mutation) or expand a terminal into a new subtree (expansion mutation).

       5.     Adaptive Hyperparameters

           •   Crossover, mutation, tournament size, and maximum depth can be adjusted dynamically based on improvement to balance exploration/exploitation.

       6.     Assumptions / Notes

           •   Inputs are loaded from .npz files containing x and y.

           •   The terminal set includes all feature variables and randomly generated constants.

           •   The user can customize maximum tree depth, probability thresholds, and population sizes for different problem complexities.

           •   If the best MSE is sufficiently low, the evolution ends early.

 

This provides a flexible framework for evolving symbolic expressions that approximate data-driven functions.
