import streamlit as st
import random

def show_section_questions(section, student_id):
    score = 0
    submitted = False
    
    if section == "English":
        score, submitted = english_section(student_id)
    elif section == "Urdu":
        score, submitted = urdu_section(student_id)
    elif section == "Math":
        score, submitted = math_section(student_id)
    elif section == "General Knowledge":
        score, submitted = gk_section(student_id)
    elif section == "Islamiat":
        score, submitted = islamiat_section(student_id)
    
    return score, submitted

def english_section(student_id):
    score = 0
    st.write("### English Assessment")
    
    # Question 1
    correct_letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    st.write(f"Q1. Identify this letter: **{correct_letter}**")
    options = [correct_letter] + random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 3)
    random.shuffle(options)
    answer1 = st.radio("Select the correct letter:", options, key=f"eng1_{student_id}")
    if answer1 == correct_letter:
        score += 1
    
    # Question 2
    words = {"CAT": ["CAT", "DOG", "RAT", "BAT"]}
    word = random.choice(list(words.keys()))
    st.write(f"Q2. Find the word: **{word}**")
    answer2 = st.radio("Select the correct word:", words[word], key=f"eng2_{student_id}")
    if answer2 == word:
        score += 1
    
    return score, True

def urdu_section(student_id):
    score = 0
    st.write("### Urdu Assessment")
    
    # Question 1
    urdu_letters = ["ا", "ب", "ت", "ث", "ج"]
    correct_urdu = random.choice(urdu_letters)
    st.write(f"Q1. Identify this letter: **{correct_urdu}**")
    answer1 = st.radio("Select the correct letter:", urdu_letters, key=f"urdu1_{student_id}")
    if answer1 == correct_urdu:
        score += 1
    
    # Question 2
    urdu_words = ["کتاب", "قلم", "کاپی", "میز"]
    correct_word = random.choice(urdu_words)
    st.write(f"Q2. Read this word: **{correct_word}**")
    answer2 = st.radio("Select the correct word:", urdu_words, key=f"urdu2_{student_id}")
    if answer2 == correct_word:
        score += 1
    
    return score, True

def math_section(student_id):
    score = 0
    st.write("### Mathematics Assessment")
    
    # Question 1
    num1 = random.randint(1, 5)
    num2 = random.randint(1, 5)
    st.write(f"Q1. How much is {num1} + {num2}?")
    answer1 = st.number_input("Enter your answer:", min_value=0, max_value=10, key=f"math1_{student_id}")
    if answer1 == num1 + num2:
        score += 1
    
    # Question 2
    numbers = list(range(1, 11))
    correct_num = random.choice(numbers)
    st.write(f"Q2. Select the number: **{correct_num}**")
    options = [correct_num] + random.sample(numbers, 3)
    random.shuffle(options)
    answer2 = st.radio("Choose the correct number:", options, key=f"math2_{student_id}")
    if answer2 == correct_num:
        score += 1
    
    return score, True

def gk_section(student_id):
    score = 0
    st.write("### General Knowledge Assessment")
    
    # Question 1
    gk_questions = {
        "What color is an apple?": ["Red", "Blue", "Green", "Yellow"],
        "What animal says 'meow'?": ["Cat", "Dog", "Bird", "Fish"],
        "How many days are in a week?": ["7", "5", "6", "8"],
        "What do we use to write?": ["Pencil", "Plate", "Chair", "Table"]
    }
    
    questions = random.sample(list(gk_questions.items()), 2)
    
    for i, (question, options) in enumerate(questions):
        st.write(f"Q{i+1}. {question}")
        correct_answer = options[0]
        random.shuffle(options)
        answer = st.radio("Select your answer:", options, key=f"gk{i}_{student_id}")
        if answer == correct_answer:
            score += 1
    
    return score, True

def islamiat_section(student_id):
    score = 0
    st.write("### Islamiat Assessment")
    
    # Question 1
    islamic_questions = {
        "How many Kalmas are there?": ["6", "5", "4", "7"],
        "What do we say before eating?": ["Bismillah", "Alhamdulillah", "SubhanAllah", "MashaAllah"],
        "How many times do we pray in a day?": ["5", "3", "4", "6"],
        "What is our holy book called?": ["Quran", "Bible", "Torah", "Zabur"]
    }
    
    questions = random.sample(list(islamic_questions.items()), 2)
    
    for i, (question, options) in enumerate(questions):
        st.write(f"Q{i+1}. {question}")
        correct_answer = options[0]
        random.shuffle(options)
        answer = st.radio("Select your answer:", options, key=f"isl{i}_{student_id}")
        if answer == correct_answer:
            score += 1
    
    return score, True 