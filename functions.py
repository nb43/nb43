#/!usr/bin/env python3
#-*- coding: utf-8 -*-

''' This file contains functions for the keyboard typing program.'''

import time
import random
import string
import math

class TypingTest:
    '''^'''
    def __init__(self):
        self.elapsed_time = 0 # Used by TIMER for most functions
        self.word_precision = 0
        self.word_error_count = 0
        self.char_precision = 0
        self.char_error_count = 0
        self.char_errors = {}
        self.gross_wpm = 0
        self.net_wpm = 0
        self.scores = [] # Stopover list for proper index order of score items

    #* ACHHIEVEMENT ---------------------------------------------------------- 
    def get_badge(self, net_wpm):
        '''Calculates and prints an achievement badge based on the net WPM.'''
        
        animal = "Prenatal creature"
        
        if 0 <= net_wpm < 10:
            animal = "Frozen Sloth"

        elif 10 <= net_wpm < 20:
            animal = "Sloth"
        
        elif 20 <= net_wpm < 30:
            animal = "Snail"
        
        elif 30 <= net_wpm < 40:
            animal = "Sea-cow"
        
        elif 40 <= net_wpm < 50:
            animal = "Human"
        
        elif 50 <= net_wpm < 60:
            animal = "Gazelle"
        
        elif 60 <= net_wpm < 70:
            animal = "Ostrich"
        
        elif 70 <= net_wpm < 80:
            animal = "Swordfish"
        
        elif 80 <= net_wpm < 90:
            animal = "Spur Goose"
        
        elif 90 <= net_wpm < 100:
            animal = "Spiny Tail Sailer"
        
        elif 100 <= net_wpm < 120:
            animal = "Golden Eagle"
        
        elif net_wpm >= 120:
            animal = "Peregrine Falcon"
        
        print(f"Your animal badge: '{animal}'")
        
        return animal

    #* CLEAR GLOBAL ---------------------------------------------------------- 
    def clear_vars(self):
        '''Resets all modular/global variables.'''

        self.elapsed_time = 0
        self.word_precision = 0
        self.word_error_count = 0
        self.char_precision = 0
        self.char_error_count = 0
        self.char_errors.clear()
        self.gross_wpm = 0
        self.net_wpm = 0
        self.scores.clear()

    #* DIFFICULTY LEVEL ------------------------------------------------------
    def get_difficulty_level(self, filename):
        '''^'''
        # Name difficulty level
        if filename == "easy.txt":
            difficulty_level = "easy"

        elif filename == "medium.txt":
            difficulty_level = "medium"

        elif filename == "hard.txt":
            difficulty_level = "hard"

        else:
            difficulty_level = "unknown"
            print("Could not determine difficulty level.")

        return difficulty_level

    #* PER MINUTE / CHAR / GROSS --------------------------------------------- 
    def calculate_gross_cpm(self, user_chars, elapsed_time):
        '''^'''
        # Calculate and print
        elapsed_minutes = math.ceil(elapsed_time / 60)
        elapsed_minutes = max(1, elapsed_minutes)
        gross_cpm = len(user_chars) / elapsed_minutes
        print(f"Gross CPM: {gross_cpm:.2f}")

        return gross_cpm

    #* PER MINUTE / WORD / GROSS --------------------------------------------- 
    def calculate_gross_wpm(self, user_words, elapsed_time):
        '''^'''
        # Calculate and print
        elapsed_minutes = math.ceil(elapsed_time / 60)
        elapsed_minutes = max(1, elapsed_minutes)  # All values under 1 minute are rounded up to 1 minute
        self.gross_wpm = len(user_words) / elapsed_minutes
        print(f"Gross WPM: {self.gross_wpm:.2f}")

        return self.gross_wpm

    #* PER MINUTE / WORD / NET ----------------------------------------------- 
    def calculate_net_wpm(self, user_words, elapsed_time):
        '''^'''
        # Calculate and print
        elapsed_minutes = math.ceil(elapsed_time / 60)
        elapsed_minutes = max(1, elapsed_minutes)  # All values under 1 minute are rounded up to 1 minute
        self.net_wpm = (len(user_words) - self.word_error_count) / elapsed_minutes
        print(f"Net WPM: {self.net_wpm:.2f}")

        return self.net_wpm

    #* PRECISION / CHAR / % -------------------------------------------------- 
    def calculate_char_precision(self, text_chars, user_chars):
        '''^'''
        # Collect parameters into lists
        correct_chars = 0
        self.char_errors = {}

        for j in range(min(len(text_chars), len(user_chars))):
            if text_chars[j] == user_chars[j]:
                correct_chars += 1
            else:
                self.char_errors[text_chars[j]] = self.char_errors.get(text_chars[j], 0) + 1

        # Calculate and print
        self.char_precision = (correct_chars / len(text_chars)) * 100
        error_list = [
            (char, count) for char, count in sorted(self.char_errors.items(), key=lambda x: x[1], reverse=True)
            ]
        print(f"Character precision: {self.char_precision:.2f}%")
        print(f"Incorrect characters: {error_list}")

        return self.char_precision, self.char_errors

    #* PRECISION / WORD / % -------------------------------------------------- 
    def calculate_word_precision(self, text_words, user_words):
        '''^'''
        # Collect parameters into lists
        correct_words_count = 0
        self.word_error_count = 0

        # Main loop
        for i in range(min(len(text_words), len(user_words))):
            if i >= len(user_words):
                break # If typed more words than original, break to avoid index out of range error
            if text_words[i] == user_words[i]:
                correct_words_count += 1
            else:
                self.word_error_count += 1 

        # Calculate and print
        extra_words_count = max(0, len(user_words) - len(text_words))
        correct_words_count -= extra_words_count
        correct_words_count -= self.word_error_count
        self.word_precision = (correct_words_count / len(text_words)) * 100
        print(f"Word precision: {self.word_precision:.2f}%")
        self.scores.append(f"{self.word_precision:.2f}") # Send to temp score list, pos=1

        return self.word_precision

    #* RANDOMIZER ------------------------------------------------------------ 
    def generate_random_characters(self, length):

        '''Generates and returns a string of random characters of a given length.'''
        return "".join(random.choice(string.ascii_letters + string.digits + '.') for _ in range(length))

    #* SCOREBOARD / SAVE ----------------------------------------------------- 
    def save_score(self, scores):
        '''^'''
        # Append new score data to score.txt
        with open("score.txt", "a", encoding="utf-8") as score_file:
            username, word_precision, difficulty_level= scores
            score_file.write(f"\n{username} {word_precision} {difficulty_level}")

    #* SCOREBOARD / VIEW ----------------------------------------------------- 
    def view_score(self, filename):
        '''^'''
        # Map difficulty to numerical values
        difficulty_values = {"easy": 1, "medium": 2, "hard": 3}

        try:
            # Read the score file and sort lines by difficulty and then by precision
            with open(filename, "r") as scorefile:
                lines = scorefile.readlines()
                scores = []
                for line in lines:
                    username, precision, difficulty = line.split()
                    scores.append((username, float(precision), difficulty_values[difficulty]))
                sorted_scores = sorted(scores, key=lambda x: (x[2], x[1]), reverse=True)
                
                # Print the sorted scores
                print(f"\n{'Username':<12s} {'Precision':<12s} {'Difficulty':<12s}")
                print("-" * 36)
                for _, (username, precision, difficulty) in enumerate(sorted_scores, start=1):
                    difficulty_key = list(difficulty_values.keys())[list(difficulty_values.values()).index(difficulty)]
                    print(f"{username:<12s} {precision:<12.2f} {difficulty_key:<12s}")
        
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

    #* SCOREBOARD / RESET ----------------------------------------------------
    def reset_score(self, filename):
        '''^'''
        # Reset the scoreboard
        with open(filename, "w") as scorefile:
            scorefile.write("")
        print("\nScores have been reset.\n")

    #* TYPING TEST / MAIN ---------------------------------------------------- 
    def main_typing_test(self, filename):
        '''^'''
        try:
            # Prepare text file
            text_lines = self.read_text_file(filename)
            text_lines = [line.strip("\n") for line in text_lines] # Strip "\n" from lines
            
            # Collect parameters into lists
            text_words = []
            text_chars = []
            user_words = []
            user_chars = []

            # Get username
            username = input("\nBefore we start, type your username: ")

            # Main loop
            if text_lines:
                print("\nWrite the following text as fast and correctly as possible:\n")

                start_time = time.time() # Timestamp: Start of test

                for line in text_lines:
                    print(f"{line.strip()}")

                    for words in line.split(): # Pull out words from lines (original)
                        text_words.append(words)
                        
                        for char in words: # Pull out chars from words (original)
                            text_chars.append(char)

                    user_input = input("").split()

                    for words in user_input: # Pull out words form lines (user input)
                        user_words.append(words)

                        for chars in words: # Pull out chars from words (user input)
                            user_chars.append(chars)
                
                end_time = time.time() # Timestamp: End of test

            else:
                print("Could not run typing test.")

            # Calculate and print results
            print("\nTest is over! You can find your results below:\n")
            self.calculate_elapsed_time(start_time, end_time)
            self.scores.append(f"{username}") # Send to temp score list, pos=0
            self.calculate_word_precision(text_words, user_words)
            self.scores.append(f"{self.get_difficulty_level(filename)}") # Send to temp score list, pos=2
            self.save_score(self.scores) # Transfer temp score list to save_score() function
            self.calculate_char_precision(text_chars, user_chars)
            self.calculate_gross_wpm(user_words, self.elapsed_time)
            self.calculate_net_wpm(user_words, self.elapsed_time)
            self.get_badge(self.net_wpm)
            print("Score has been saved to scoreboard.\n")

            self.clear_vars() # Reset modular variables

        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

    #* TYPING TEST / RANDOM -------------------------------------------------- 
    def random_typing_test(self):
        '''Runs a random and timed typing test.'''

        # Set the duration of the test
        try:
            test_duration = int(input("Enter the duration of the test in seconds: "))
        except ValueError:
            print("Invalid input. Please enter a valid number of seconds.")
            return

        print(f"\nType the following characters as fast as possible for {test_duration} seconds:\n")

        # Timer
        start_time = time.time()
        end_time = start_time + test_duration
        
        random_chars = []
        user_chars = []
        self.char_error_count = 0
        
        # Main loop
        while time.time() < end_time:
            randomizer = self.generate_random_characters(1).strip()
            print(randomizer)
            random_chars.append(randomizer)
            
            user_input = input("")
            user_chars.append(user_input)

            if time.time() >= end_time:
                break
        
        # Compare random_chars and user_chars and count errors
        for i, char in enumerate(random_chars):
            if char != user_chars[i]:
                self.char_error_count += 1

        # Calculate and print results
        print("\nTime is up! You can find your results below:\n")
        self.calculate_elapsed_time(start_time, end_time)
        self.calculate_char_precision(random_chars, user_chars)
        self.calculate_gross_cpm(user_chars, self.elapsed_time)
        error_percentage = self.char_error_count / len(user_chars) * 100
        print(f"Error percentage: {error_percentage:.2f}%")

        self.clear_vars() # Reset modular variables

    #* TIMER ----------------------------------------------------------------- 
    def calculate_elapsed_time(self, start_time, end_time):
        '''^'''
        # Calculate and print
        self.elapsed_time = end_time - start_time
        print(f"Elapsed time: {self.elapsed_time:.2f} seconds")

        return self.elapsed_time

    #* TXT FILE -------------------------------------------------------------- 
    def read_text_file(self, filename):
        '''Reads a text file and returns a list of lines.'''

        try:
            with open(filename, "r", encoding="utf-8") as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return None

# NOTE(S) -------------------------------------------------------------------- 
# Add a date stamp to the scoreboard
# Check which modular var(s) can be removed
# Add return to main menu option or function
# Add a warning / confirmation before resetting the scoreboard
# Don't show more than X amount of scores in the scoreboard
# Perhaps modify scoreboard to fit even random_typing_test() results
# Create Net CPM function for random_typing_test()
# ...
