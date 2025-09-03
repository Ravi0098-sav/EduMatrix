EduMatrix
=========

EduMatrix is a desktop educational application that helps users learn and practice programming and computer science concepts through quizzes, mini-games, and language/code reference tools. The application features a graphical user interface, interactive games, a quiz module, a dashboard, and a language tool for syntax, snippets, and error explanations.

How to Run This Code
====================

1. Download the Project
-----------------------
• Ensure you have the main file: `edumatrix_main.py`  
• (Optional) Download any documentation or supporting files you want (such as `DOCUMENTATION.md`, `README.md`).

2. Install Python
-----------------
• Make sure you have Python 3.x installed on your system.  
• You can download Python from: https://www.python.org/downloads/

3. Required Libraries
---------------------
• The project uses only Python's standard library modules:
  - tkinter (for GUI)
  - sqlite3 (for database)
  - random
  - time
  - datetime

> Note:
• On some Linux systems, you may need to install Tkinter separately. Use the following command:
  sudo apt-get install python3-tk

4. Run the Application
----------------------
• Open a terminal or command prompt in the folder containing `edumatrix_main.py`.  
• Run the following command:

    python edumatrix_main.py  
    or (if your system uses python3):  
    python3 edumatrix_main.py

Project Structure
=================

• edumatrix_main.py       - Main application file (contains all features and GUI)  
• results.db              - SQLite database file for storing quiz results (auto-generated after first quiz)  
• DOCUMENTATION.docx      - Project documentation  
• Presentation.pptx       - Project Presentation  
• README.txt              - This file  

Features
========

• Quiz Module:
  - Timed quizzes on Python, Java, C++, Web, and Operating Systems
  - Includes feedback and explanations

• Dashboard:
  - View quiz performance, history, and statistics

• Game Center:
  - Educational games such as Flashcards, Hangman, Puzzle, Memory, Word Search, and Typing Challenge

• Language Tool:
  - Syntax reference
  - Code snippets
  - Keyword lookup
  - Error explanations for various programming languages

Notes
=====

• All quiz progress is stored locally in `results.db`.  
• No internet connection is required to run the app after downloading.  
• For any errors regarding missing `tkinter`, please install it as described above.

Author
======

Jenish Gohel      (92300527156)  
Yuvrajsinh Zala   (92300527141)  
Ravi Sav          (92300527257)
