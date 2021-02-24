"""
####################################
1 Arrays and Strings
####################################
"""
# Is Unique
def isUnique(string):
  if len(string) > 128:
    return False

  chars = [False] * 128

  for char in string:
    if chars[ord(char)] == False:
      chars[ord(char)] = True
    else:
      return False
  return True

print(isUnique('Aaron Soler'))

# Check Permutation
# URLify
# Palindrome Premutation
# One Away
# String Compression
# Rotate Matrix
# Zero Matrix
# String Rotation

"""
####################################
2 Linked Lists
####################################
"""
# Remove Dups
# Return Kth to Last
# Delete Middle Node
# Partition
# Sum Lists
# Palindrome
# Intersection
# Loop Detection

"""
####################################
3 Stacks and Queues
####################################
"""
# Three in One
# Stack Min
# Stack of Plates
# Queue via Stacks
# Sort Stack
# Animal Shelter

"""
####################################
4 Trees and Graphs
####################################
"""
# Route Between Nodes
# Minimal Tree
# List of Depths
# Check Balanced
# Validate BST
# Successor
# Build Order
# First Common Ancestor
# BST Sequences
# Check Subtree
# Random Node
# Paths with Sum

"""
####################################
5 Bit Manipulation
####################################
"""
# Insertion
# Binary to String
# Flip Bit to Win
# Next Number
# Debugger
# Conversion
# Pairwise Swap
# Draw Line

"""
####################################
6 Math and Logic Puzzles
####################################
"""
# The Heavy Pill
# Basketball
# Dominos
# Ants on a Triangle
# Jugs of Water
# Blue-Eyed Island
# The Apocalypse
# The Egg Drop Problem
# 100 Lockers
# Poison

"""
####################################
7 Object-Oriented Design
####################################
"""
# Deck of Cards
# Call Center
# Jukebox
# Parking Lot
# Online Book Reader
# Jigsaw
# Chat Server
# Othello
# Circular Array
# Minesweeper
# File System
# Hash Table

"""
####################################
8 Recursion and Dynamic Programming
####################################
"""
# Triple Step
# Robot in a Grid
# Magic Index
# Power Set
# Recursive Multiply
# Towers of Hanoi
# Permutations without Dups
# Permutations with Dups
# Parens
# Paint Fill
# Coins
# Eight Queens
# Stack of Boxes
# Boolean Evaluation

"""
####################################
9 System Design and Scalability
####################################
"""
# Stock Data
# Social Network
# Web Crawler
# Duplicate URLs
# Cache
# Sales Rank
# Personal Financial Manager
# Pastebin

"""
####################################
10 Sorting and Searching
####################################
"""
# Sorted Merge
# Group Anagrams
# Search in Rotated Array
# Sorted Search, No Size
# Sparse Search
# Sort Big File
# Missing Int
# Find Duplicates
# Sorted Matrix Search
# Rank from Stream
# Peaks and Valleys

"""
####################################
11 Testing
####################################
"""
# Mistake
# Random Crashes
# Chess Test
# No Test Tools
# Test a Pen
# Test an ATM

"""
####################################
12 C and C++
####################################
"""

"""
####################################
13 Java
####################################
"""

"""
####################################
14 Databases (SQL)
####################################
"""

"""
####################################
15 Threads and Locks (Java)
####################################
"""

"""
####################################
16 Moderate
####################################
"""
# Number Swapper
# Word Frequencies
# Intersection
# Tic Tac Win
# Smallest Difference
# Number Max
# English Int
# Operations
# Living People
# Diving Board
# XML Encoding
# Bisect Squares
# Best Line
# Master Mind
# Sub Sort
# Contiguous Sequence
# Pattern Matching
# Pond Sizes
# T9
# Sum Swap
# Langton's Ant
# Rand7 from Rand5
# Pairs with Sum
# LRU Cache
# Calculator

"""
####################################
17 Hard
####################################
"""
# Add Without Plus
# Shuffle
# Random Set
# Missing Number
# Letters and Numbers
# Count of 2s
# Baby Names
# Circus Tower
# Kth Multiple
# Majority Element
# Word Distance
# BiNode
# Re-Space
# Smallest K
# Longest Word
# The Masseuse
# Multi Search
# Shortest Supersequence
# Missing Two
# Continuous Median
# Volume of Histogram
# Word Transformer
# Max Black Square
# Max Submatrix
# Word Rectangle
# Sparse Similarity