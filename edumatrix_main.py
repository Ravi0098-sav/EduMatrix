import tkinter as tk
from tkinter import messagebox, font, filedialog
import random
import time
import sqlite3
from datetime import datetime

SUBJECTS = {
    "Python": [
        {"question": "What is the output of print(2 ** 4)?", "options": ["6", "8", "16", "12"], "answer": "16", "explanation": "2 raised to the power 4 is 16."},
        {"question": "Which of these is NOT a valid Python variable name?", "options": ["1var", "_var", "var_1", "varOne"], "answer": "1var", "explanation": "Variable names cannot start with a digit."},
        {"question": "What is the keyword to define a function in Python?", "options": ["func", "def", "function", "define"], "answer": "def", "explanation": "'def' is used to define a function in Python."},
        {"question": "Which structure does not allow duplicate elements in Python?", "options": ["list", "set", "tuple", "dictionary"], "answer": "set", "explanation": "A set does not allow duplicate elements."},
        {"question": "Result of len([1, 2, 3]) is?", "options": ["2", "3", "1", "Error"], "answer": "3", "explanation": "len returns number of items in a list."},
        {"question": "Symbol for comments in Python?", "options": ["//", "#", "/* */", "--"], "answer": "#", "explanation": "Comments in Python start with '#'."},
        {"question": "Method to add element to a list?", "options": ["add()", "append()", "insert()", "put()"], "answer": "append()", "explanation": "append() adds an element to the end of a list."},
        {"question": "Output of print('Hi' + 'There')?", "options": ["Hi There", "HiThere", "Hi+There", "Error"], "answer": "HiThere", "explanation": "String concatenation with '+' does not add space."},
        {"question": "Which is a tuple?", "options": ["[1,2,3]", "{1,2,3}", "(1,2,3)", "<1,2,3>"], "answer": "(1,2,3)", "explanation": "Tuples are defined using parentheses."},
        {"question": "Output of bool('False')?", "options": ["False", "True", "Error", "None"], "answer": "True", "explanation": "Any non-empty string is True in boolean context."},
        {"question": "Function to convert string to integer?", "options": ["int()", "str()", "float()", "chr()"], "answer": "int()", "explanation": "int() converts a string or float to integer."},
        {"question": "How to write a multi-line string?", "options": ["'string'", "\"string\"", "'''string'''", "#string#"], "answer": "'''string'''", "explanation": "Triple quotes are used for multi-line strings."},
        {"question": "What is the output of print(type([]))?", "options": ["<class 'list'>", "<type 'list'>", "<class 'dict'>", "<list>"], "answer": "<class 'list'>", "explanation": "type([]) returns the type of the object, which is list."},
        {"question": "Operator for floor division?", "options": ["//", "/", "%", "///"], "answer": "//", "explanation": "'//' is the floor division operator."},
        {"question": "Output of print(3*1**3)?", "options": ["3", "1", "9", "27"], "answer": "3", "explanation": "1**3 is 1, so 3*1 is 3."},
        {"question": "Which is NOT a built-in data type?", "options": ["array", "dict", "tuple", "set"], "answer": "array", "explanation": "Python has no built-in 'array' type."},
        {"question": "Which of these creates a dictionary?", "options": ["{1,2,3}", "{'a':1, 'b':2}", "[1,2,3]", "(1,2,3)"], "answer": "{'a':1, 'b':2}", "explanation": "Dictionaries use key:value pairs inside curly braces."},
        {"question": "What is the output of '5' * 2?", "options": ["10", "'10'", "'55'", "'5' * 2"], "answer": "'55'", "explanation": "String multiplied by int repeats the string."},
        {"question": "Correct way to start a for loop?", "options": ["for i in range(5):", "for(i=0;i<5;i++)", "foreach i in range(5)", "loop i in range(5):"], "answer": "for i in range(5):", "explanation": "Python for loop uses 'for i in range(5):'"},
        {"question": "Result of 3 < 2 < 1?", "options": ["True", "False", "Error", "None"], "answer": "False", "explanation": "3 < 2 is False, so the whole expression is False."},
    ],
    "Java": [
        {"question": "Keyword to inherit a class in Java?", "options": ["extends", "implements", "inherit", "super"], "answer": "extends", "explanation": "'extends' is used for class inheritance."},
        {"question": "Which is not a Java primitive type?", "options": ["int", "float", "String", "char"], "answer": "String", "explanation": "'String' is a class, not primitive."},
        {"question": "Correct way to start main method?", "options": ["public static void main(String[] args)", "public void main(String[] args)", "void main(String args)", "main(String[] args)"], "answer": "public static void main(String[] args)", "explanation": "Standard signature for main method."},
        {"question": "Operator to compare two values?", "options": ["=", "==", "!=", "equals"], "answer": "==", "explanation": "'==' is used for comparing primitive values."},
        {"question": "Which is a loop construct in Java?", "options": ["do-while", "foreach", "repeat", "next"], "answer": "do-while", "explanation": "do-while is a looping construct."},
        {"question": "Default value of a boolean in Java?", "options": ["true", "false", "0", "null"], "answer": "false", "explanation": "Default boolean value is false."},
        {"question": "Package for Scanner class?", "options": ["java.io", "java.util", "java.lang", "java.net"], "answer": "java.util", "explanation": "Scanner class is in java.util."},
        {"question": "Access modifier for visibility to all classes?", "options": ["private", "protected", "public", "default"], "answer": "public", "explanation": "'public' makes a member accessible everywhere."},
        {"question": "Keyword to create an object?", "options": ["object", "new", "create", "class"], "answer": "new", "explanation": "'new' is used to instantiate objects."},
        {"question": "Which is not a valid identifier?", "options": ["_var", "$var", "var#", "var123"], "answer": "var#", "explanation": "Identifiers cannot contain '#' symbol."},
        {"question": "Method called when object is created?", "options": ["main", "finalize", "constructor", "init"], "answer": "constructor", "explanation": "Constructor is called upon object creation."},
        {"question": "Collection that does not allow duplicate elements?", "options": ["ArrayList", "LinkedList", "HashSet", "Vector"], "answer": "HashSet", "explanation": "HashSet does not allow duplicate elements."},
        {"question": "Keyword to inherit an interface?", "options": ["extends", "implements", "interface", "inherits"], "answer": "implements", "explanation": "'implements' is used for interfaces."},
        {"question": "Size of int in Java?", "options": ["2 bytes", "4 bytes", "8 bytes", "Depends on OS"], "answer": "4 bytes", "explanation": "int is always 4 bytes in Java."},
        {"question": "Which class is immutable?", "options": ["String", "StringBuilder", "ArrayList", "HashMap"], "answer": "String", "explanation": "String objects are immutable."},
        {"question": "Exception thrown dividing by zero?", "options": ["NullPointerException", "ArithmeticException", "IOException", "ClassNotFoundException"], "answer": "ArithmeticException", "explanation": "Dividing by zero throws ArithmeticException."},
        {"question": "Keyword to stop a loop?", "options": ["exit", "stop", "break", "end"], "answer": "break", "explanation": "'break' is used to exit loops."},
        {"question": "Keyword to refer to parent class?", "options": ["super", "parent", "base", "this"], "answer": "super", "explanation": "'super' refers to the parent class."},
        {"question": "Method to read a line from input?", "options": ["nextInt()", "nextLine()", "read()", "input()"], "answer": "nextLine()", "explanation": "nextLine() reads a full line in Scanner."},
        {"question": "Annotation to override a method?", "options": ["@Override", "@Overload", "@Over", "@Method"], "answer": "@Override", "explanation": "@Override is used when a method is overridden."},
    ],
    "C++": [
        {"question": "Symbol for single-line comments in C++?", "options": ["//", "#", "/* */", "--"], "answer": "//", "explanation": "// starts a single-line comment in C++."},
        {"question": "Correct declaration of a pointer?", "options": ["int p", "int *p", "int &p", "pointer<int> p"], "answer": "int *p", "explanation": "'int *p;' declares p as a pointer to int."},
        {"question": "To allocate memory dynamically?", "options": ["malloc", "new", "alloc", "memory"], "answer": "new", "explanation": "'new' allocates memory dynamically in C++."},
        {"question": "Not a loop statement in C++?", "options": ["for", "while", "repeat", "do-while"], "answer": "repeat", "explanation": "C++ does not have a 'repeat' loop."},
        {"question": "Header required for cout?", "options": ["<iostream>", "<stdio.h>", "<conio.h>", "<stdlib.h>"], "answer": "<iostream>", "explanation": "<iostream> is required for cout/cin."},
        {"question": "Operator overloaded for object copy?", "options": ["=", "()", "[]", "&"], "answer": "=", "explanation": "'=' is the assignment operator, can be overloaded."},
        {"question": "Not a valid access specifier?", "options": ["public", "private", "protected", "internal"], "answer": "internal", "explanation": "'internal' is not an access specifier in C++."},
        {"question": "Function to free memory?", "options": ["delete", "remove", "free", "clear"], "answer": "delete", "explanation": "'delete' deallocates memory in C++."},
        {"question": "Used for file I/O?", "options": ["fstream", "istream", "ofstream", "All of these"], "answer": "All of these", "explanation": "fstream, istream, and ofstream are used for file I/O."},
        {"question": "Correct syntax for class definition?", "options": ["class MyClass {}", "class MyClass[]", "MyClass class {}", "define class MyClass {}"], "answer": "class MyClass {}", "explanation": "C++ class definition uses 'class MyClass {}'."},
        {"question": "Function called when object is destroyed?", "options": ["constructor", "destructor", "delete", "finalize"], "answer": "destructor", "explanation": "Destructor is called when object is destroyed."},
        {"question": "Not a C++ keyword?", "options": ["class", "template", "public", "function"], "answer": "function", "explanation": "'function' is not a C++ keyword."},
        {"question": "Declare a constant?", "options": ["const", "define", "static", "final"], "answer": "const", "explanation": "'const' is used to declare constants."},
        {"question": "Operator for input?", "options": ["<<", ">>", "<", ">"], "answer": ">>", "explanation": "'>>' is the extraction operator for input."},
        {"question": "Operator for output?", "options": ["<<", ">>", "<", ">"], "answer": "<<", "explanation": "'<<' is the insertion operator for output."},
        {"question": "Used to handle exceptions?", "options": ["try-catch", "handle", "catch-throw", "error"], "answer": "try-catch", "explanation": "try-catch blocks are used for exception handling."},
        {"question": "Not an OOP concept?", "options": ["Inheritance", "Polymorphism", "Encapsulation", "Compilation"], "answer": "Compilation", "explanation": "Compilation is not an OOP concept."},
        {"question": "A preprocessor directive?", "options": ["#include", "#define", "#ifdef", "All of these"], "answer": "All of these", "explanation": "All are preprocessor directives."},
        {"question": "Correct way to declare a reference?", "options": ["int &ref = var;", "ref int = var;", "int ref = &var;", "int *ref = var;"], "answer": "int &ref = var;", "explanation": "C++ references are declared with '&'."},
        {"question": "Extension of C++ files?", "options": [".c", ".cpp", ".java", ".py"], "answer": ".cpp", "explanation": "C++ source files use '.cpp' extension."},
    ],
    "Web": [
        {"question": "What does HTML stand for?", "options": ["Hyper Trainer Marking Language", "Hyper Text Markup Language", "Hyper Text Marketing Language", "Hyper Tool Markup Language"], "answer": "Hyper Text Markup Language", "explanation": "HTML stands for Hyper Text Markup Language."},
        {"question": "Tag for hyperlink in HTML?", "options": ["<a>", "<link>", "<href>", "<hyper>"], "answer": "<a>", "explanation": "The <a> tag creates hyperlinks."},
        {"question": "Property to change text color in CSS?", "options": ["font-color", "color", "text-color", "fgcolor"], "answer": "color", "explanation": "'color' property changes text color in CSS."},
        {"question": "A JavaScript framework?", "options": ["Django", "React", "Flask", "Laravel"], "answer": "React", "explanation": "React is a popular JS framework."},
        {"question": "What does CSS stand for?", "options": ["Colorful Style Sheets", "Cascading Style Sheets", "Computer Style Sheets", "Creative Style System"], "answer": "Cascading Style Sheets", "explanation": "CSS = Cascading Style Sheets."},
        {"question": "Attribute for image source in HTML?", "options": ["src", "href", "alt", "link"], "answer": "src", "explanation": "'src' specifies the image source."},
        {"question": "Tag for table row?", "options": ["<tr>", "<td>", "<th>", "<row>"], "answer": "<tr>", "explanation": "<tr> is a table row tag."},
        {"question": "Method to write output in JavaScript?", "options": ["console.log()", "print()", "echo()", "write()"], "answer": "console.log()", "explanation": "console.log() outputs to console."},
        {"question": "Where to insert JavaScript?", "options": ["<body>", "<head>", "Both <head> and <body>", "<footer>"], "answer": "Both <head> and <body>", "explanation": "JS can be placed in both head and body."},
        {"question": "Input type for selecting a file?", "options": ["text", "file", "select", "upload"], "answer": "file", "explanation": "input type='file' is for file selection."},
        {"question": "Default alignment of table content?", "options": ["left", "center", "right", "justify"], "answer": "left", "explanation": "Default alignment is left."},
        {"question": "Property for background color in CSS?", "options": ["background", "bgcolor", "background-color", "color"], "answer": "background-color", "explanation": "background-color sets background color."},
        {"question": "Refer to external CSS?", "options": ["<style src='style.css'>", "<link rel='stylesheet' href='style.css'>", "<css src='style.css'>", "<stylesheet>"], "answer": "<link rel='stylesheet' href='style.css'>", "explanation": "Standard way to link CSS."},
        {"question": "Tag for largest heading?", "options": ["<h6>", "<h1>", "<heading>", "<head>"], "answer": "<h1>", "explanation": "<h1> is the largest heading."},
        {"question": "Tag for ordered list?", "options": ["<ul>", "<ol>", "<li>", "<dl>"], "answer": "<ol>", "explanation": "<ol> is used for ordered lists."},
        {"question": "Write a comment in HTML?", "options": ["<!-- Comment -->", "// Comment", "# Comment", "/* Comment */"], "answer": "<!-- Comment -->", "explanation": "HTML comments use <!-- -->."},
        {"question": "Select an element with id 'demo' in CSS?", "options": ["#demo", ".demo", "demo", "*demo"], "answer": "#demo", "explanation": "Use # for id selectors in CSS."},
        {"question": "Tag for creating a checkbox?", "options": ["<input type='checkbox'>", "<checkbox>", "<check>", "<input type='check'>"], "answer": "<input type='checkbox'>", "explanation": "Input type='checkbox' creates a checkbox."},
        {"question": "Event for user click in HTML?", "options": ["onmouse", "onchange", "onclick", "onmouseover"], "answer": "onclick", "explanation": "onclick triggers when an element is clicked."},
        {"question": "File extension of JavaScript files?", "options": [".js", ".javascript", ".java", ".jsx"], "answer": ".js", "explanation": "JavaScript files use the .js extension."},
    ],
    "Operating System": [
        {"question": "Which of the following is not an operating system?", "options": ["Linux", "Mac OS", "Oracle", "Windows"], "answer": "Oracle", "explanation": "Oracle is a database, not an OS."},
        {"question": "Which is not a type of OS?", "options": ["Batch", "Time-sharing", "Real-time", "Compiler"], "answer": "Compiler", "explanation": "Compiler is not an OS type."},
        {"question": "Which is a process management task?", "options": ["Process scheduling", "Memory allocation", "File access", "Device control"], "answer": "Process scheduling", "explanation": "Process scheduling is process management."},
        {"question": "Which OS is open source?", "options": ["Windows", "Linux", "Mac OS", "DOS"], "answer": "Linux", "explanation": "Linux is open source."},
        {"question": "Which is a non-preemptive scheduling algorithm?", "options": ["Round Robin", "FCFS", "Priority", "SJF (preemptive)"], "answer": "FCFS", "explanation": "FCFS is non-preemptive."},
        {"question": "What is a deadlock?", "options": ["Memory overflow", "Infinite loop", "Two processes waiting for each other", "File not found"], "answer": "Two processes waiting for each other", "explanation": "Deadlock: two or more processes wait forever for resources."},
        {"question": "Which is not a process state?", "options": ["Running", "Waiting", "Blocked", "Executing"], "answer": "Executing", "explanation": "Executing is not a standard process state."},
        {"question": "Which of the following is a real-time OS?", "options": ["Windows 10", "DOS", "RTLinux", "Unix"], "answer": "RTLinux", "explanation": "RTLinux is a real-time operating system."},
        {"question": "Paging is a technique of:", "options": ["Memory management", "CPU scheduling", "Disk scheduling", "Device management"], "answer": "Memory management", "explanation": "Paging is used in memory management."},
        {"question": "Thrashing is:", "options": ["A process of swapping", "High CPU usage", "Excessive paging", "Low disk space"], "answer": "Excessive paging", "explanation": "Thrashing is excessive paging."},
        {"question": "Which is an example of a device management task?", "options": ["Process table", "Spooling", "Paging", "Segmentation"], "answer": "Spooling", "explanation": "Spooling is device management."},
        {"question": "Which of these is not a disk scheduling algorithm?", "options": ["FCFS", "SSTF", "SCAN", "FIFO"], "answer": "FIFO", "explanation": "FIFO is not a disk scheduling algorithm."},
        {"question": "Which of these is not a kernel function?", "options": ["Process management", "Network access", "Memory management", "Web browsing"], "answer": "Web browsing", "explanation": "Web browsing is not a kernel function."},
        {"question": "Scheduling algorithm with minimum average waiting time?", "options": ["FCFS", "SJF", "Round Robin", "Priority"], "answer": "SJF", "explanation": "SJF gives minimum average waiting time."},
        {"question": "Used to prevent deadlock?", "options": ["Banker's algorithm", "Paging", "Spooling", "Segmentation"], "answer": "Banker's algorithm", "explanation": "Banker's algorithm prevents deadlock."},
        {"question": "Which is not a file system?", "options": ["FAT", "NTFS", "ext2", "FTP"], "answer": "FTP", "explanation": "FTP is a protocol, not a file system."},
        {"question": "Which OS is known for security?", "options": ["Unix", "Windows", "DOS", "Mac OS"], "answer": "Unix", "explanation": "Unix is known for security."},
        {"question": "Full form of BIOS?", "options": ["Basic Input Output System", "Binary Input Output System", "Basic Integrated Output System", "Binary Integrated Output System"], "answer": "Basic Input Output System", "explanation": "BIOS stands for Basic Input Output System."},
        {"question": "First program run on computer boot?", "options": ["BIOS", "Bootloader", "Kernel", "Shell"], "answer": "BIOS", "explanation": "BIOS is the first program run at startup."},
        {"question": "Command to remove file in UNIX?", "options": ["delete", "erase", "rm", "remove"], "answer": "rm", "explanation": "'rm' command removes files in UNIX."},
    ],
}

QUIZ_TIME_SECONDS = 10 * 60

DB_FILE = "results.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            subject TEXT,
            score INTEGER,
            max_score INTEGER,
            time_used TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_result(subject, score, max_score, time_used):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        'INSERT INTO results (date, subject, score, max_score, time_used) VALUES (?,?,?,?,?)',
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), subject, score, max_score, time_used)
    )
    conn.commit()
    conn.close()

def get_all_results():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT date, subject, score, max_score, time_used FROM results ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return rows

def get_stats():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT subject, MAX(score), AVG(score*1.0/max_score)*100, COUNT(*) FROM results GROUP BY subject')
    stats = c.fetchall()
    conn.close()
    return stats

class EduMatrixApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EduMatrix")
        self.state('zoomed')
        self.configure(bg="#e9ecef")
        self.custom_font = font.Font(family="Segoe UI", size=18)
        self.title_font = font.Font(family="Segoe UI", size=40, weight="bold")
        self.button_font = font.Font(family="Segoe UI", size=18, weight="bold")
        self.subjects = list(SUBJECTS.keys())
        self.protocol("WM_DELETE_WINDOW", self.on_quit)
        init_db()
        self.show_main_menu()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear()
        tk.Label(self, text="EduMatrix", font=self.title_font, bg="#e9ecef", fg="#003049").pack(pady=50)
        menu = tk.Frame(self, bg="#e9ecef")
        menu.pack(pady=40)
        tk.Button(menu, text="Quiz", width=25, height=2, font=self.button_font, bg="#2a9d8f", fg="white",
                  activebackground="#52b788", relief="flat", command=self.show_subject_menu).pack(pady=18)
        tk.Button(menu, text="Dashboard", width=25, height=2, font=self.button_font, bg="#6a4c93", fg="white",
                  activebackground="#b983ff", relief="flat", command=self.show_dashboard).pack(pady=18)
        tk.Button(menu, text="Game", width=25, height=2, font=self.button_font, bg="#d62828", fg="white",
                  activebackground="#f77f00", relief="flat", command=self.show_game_menu).pack(pady=18)
        tk.Button(menu, text="Language Tool", width=25, height=2, font=self.button_font, bg="#457b9d", fg="white",
                  activebackground="#a8dadc", relief="flat", command=self.show_language_tool).pack(pady=18)
    def show_dashboard(self):
        self.clear()
        self.create_back_button(self.show_main_menu)
        tk.Label(self, text="Dashboard", font=self.title_font, bg="#e9ecef", fg="#003049").pack(pady=20)
        stats = get_stats()
        res = get_all_results()
        stat_frame = tk.Frame(self, bg="#e9ecef")
        stat_frame.pack(pady=10)
        if stats:
            tk.Label(stat_frame, text="Subject", font=self.button_font, width=15, bg="#e9ecef").grid(row=0, column=0)
            tk.Label(stat_frame, text="Best Score", font=self.button_font, width=12, bg="#e9ecef").grid(row=0, column=1)
            tk.Label(stat_frame, text="Avg. %", font=self.button_font, width=12, bg="#e9ecef").grid(row=0, column=2)
            tk.Label(stat_frame, text="Attempts", font=self.button_font, width=12, bg="#e9ecef").grid(row=0, column=3)
            for i, (sub, best, avg, count) in enumerate(stats):
                tk.Label(stat_frame, text=sub, font=self.custom_font, width=15, bg="#e9ecef").grid(row=i+1, column=0)
                tk.Label(stat_frame, text=f"{best}", font=self.custom_font, width=12, bg="#e9ecef").grid(row=i+1, column=1)
                tk.Label(stat_frame, text=f"{avg:.1f}%", font=self.custom_font, width=12, bg="#e9ecef").grid(row=i+1, column=2)
                tk.Label(stat_frame, text=f"{count}", font=self.custom_font, width=12, bg="#e9ecef").grid(row=i+1, column=3)
        else:
            tk.Label(stat_frame, text="No quiz data yet.", font=self.custom_font, bg="#e9ecef").pack()

        # Quiz history
        tk.Label(self, text="Quiz Attempt History", font=self.button_font, bg="#e9ecef", fg="#003049").pack(pady=18)
        hist_frame = tk.Frame(self, bg="#e9ecef")
        hist_frame.pack(pady=10)
        tk.Label(hist_frame, text="Date/Time", font=self.button_font, width=20, bg="#e9ecef").grid(row=0, column=0)
        tk.Label(hist_frame, text="Subject", font=self.button_font, width=12, bg="#e9ecef").grid(row=0, column=1)
        tk.Label(hist_frame, text="Score", font=self.button_font, width=10, bg="#e9ecef").grid(row=0, column=2)
        tk.Label(hist_frame, text="Time Used", font=self.button_font, width=10, bg="#e9ecef").grid(row=0, column=3)
        for i, (date, subject, score, max_score, time_used) in enumerate(res[:20]):
            tk.Label(hist_frame, text=date, font=self.custom_font, width=20, bg="#f0f0f0" if i%2==0 else "#fff").grid(row=i+1, column=0)
            tk.Label(hist_frame, text=subject, font=self.custom_font, width=12, bg="#f0f0f0" if i%2==0 else "#fff").grid(row=i+1, column=1)
            tk.Label(hist_frame, text=f"{score}/{max_score}", font=self.custom_font, width=10, bg="#f0f0f0" if i%2==0 else "#fff").grid(row=i+1, column=2)
            tk.Label(hist_frame, text=time_used, font=self.custom_font, width=10, bg="#f0f0f0" if i%2==0 else "#fff").grid(row=i+1, column=3)

    def show_subject_menu(self):
        self.clear()
        self.create_back_button(lambda: self.ask_quit_to_main())
        tk.Label(self, text="Select a subject to begin:", font=self.title_font, bg="#e9ecef", fg="#003049").pack(pady=40)
        btn_frame = tk.Frame(self, bg="#e9ecef")
        btn_frame.pack(pady=30)
        colors = ["#457b9d", "#2a9d8f", "#f77f00", "#d62828", "#6a4c93"]
        for i, subject in enumerate(self.subjects):
            tk.Button(
                btn_frame, text=subject, font=self.custom_font, width=22, height=2,
                bg=colors[i], fg="white", activebackground="#dee2e6", relief="flat",
                command=lambda s=subject: self.start_quiz(s)
            ).grid(row=i // 2, column=i % 2, padx=50, pady=22)

    def create_back_button(self, command):
        back_frame = tk.Frame(self, bg="#e9ecef")
        back_frame.pack(fill='x', pady=8)
        tk.Button(back_frame, text="⟵ Back", font=self.custom_font, bg="#adb5bd", fg="white",
                  activebackground="#ced4da", relief="flat", width=8, command=command).pack(anchor='w', padx=20)

    def ask_quit_to_main(self):
        if messagebox.askyesno("Quit", "Do you want to quit?"):
            self.show_main_menu()

    def start_quiz(self, subject):
        total_available = len(SUBJECTS[subject])
        num_questions = min(20, total_available)
        if total_available < 20:
            messagebox.showwarning("Not enough questions", f"Only {total_available} questions available for {subject}. The quiz will use all available questions.")
        QuizWindow(self, subject, num_questions)

    def on_quit(self):
        if messagebox.askyesno("Exit", "Do you really want to quit EduMatrix?"):
            self.destroy()

class QuizWindow(tk.Toplevel):
    def __init__(self, master, subject, num_questions):
        super().__init__(master)
        self.master = master
        self.subject = subject
        self.num_questions = num_questions
        self.quiz_data = [dict(q) for q in random.sample(SUBJECTS[subject], num_questions)]
        for q in self.quiz_data:
            random.shuffle(q['options'])
        self.user_answers = [None] * num_questions
        self.score = 0
        self.current_q = 0
        self.remaining_seconds = QUIZ_TIME_SECONDS
        self.timer_running = True
        self.timer_label = None
        self.reviewing = False
        self.state('zoomed')
        self.configure(bg="#e9ecef")
        self.custom_font = font.Font(family="Segoe UI", size=18)
        self.title_font = font.Font(family="Segoe UI", size=32, weight="bold")
        self.button_font = font.Font(family="Segoe UI", size=16, weight="bold")
        self.protocol("WM_DELETE_WINDOW", self.ask_quit_and_score)
        self.dialog_open = False
        self.build_ui()
        self.update_timer()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def build_ui(self):
        self.clear()
        self.create_back_button(self.ask_quit_and_score)
        self.timer_label = tk.Label(self, text="", font=self.button_font, bg="#e9ecef", fg="#d62828")
        self.timer_label.pack(pady=10)
        self.update_timer_label()

        tk.Label(self, text=f"{self.subject} Quiz - Question {self.current_q+1}/{self.num_questions}",
                 font=self.title_font, bg="#e9ecef", fg="#003049").pack(pady=16)
        qdata = self.quiz_data[self.current_q]
        tk.Label(self, text=qdata["question"], font=self.custom_font, wraplength=1200,
                 bg="#e9ecef", fg="#212529", justify="left").pack(pady=10)
        self.answer_var = tk.StringVar(value=self.user_answers[self.current_q] or "")
        opt_frame = tk.Frame(self, bg="#e9ecef")
        opt_frame.pack(pady=8)
        for opt in qdata["options"]:
            tk.Radiobutton(
                opt_frame, text=opt, variable=self.answer_var, value=opt,
                font=self.custom_font, bg="#e9ecef", fg="#495057", anchor="w", width=52,
                selectcolor="#f1faee", highlightthickness=0, bd=0, activebackground="#f1faee"
            ).pack(anchor="w", padx=90, pady=6)

        nav_frame = tk.Frame(self, bg="#e9ecef")
        nav_frame.pack(pady=20)

        self.submit_btn = tk.Button(
            nav_frame, text="Submit", font=self.button_font, bg="#2a9d8f", fg="white",
            activebackground="#52b788", relief="flat", width=14, command=self.submit_answer
        )
        self.submit_btn.grid(row=0, column=1, padx=18)

        tk.Button(
            nav_frame, text="Previous", font=self.button_font, bg="#adb5bd", fg="white",
            activebackground="#ced4da", relief="flat", width=10, command=self.prev_question,
            state="normal" if self.current_q > 0 else "disabled"
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            nav_frame, text="Next", font=self.button_font, bg="#457b9d", fg="white",
            activebackground="#a8dadc", relief="flat", width=10, command=self.next_question,
            state="normal" if self.current_q < self.num_questions - 1 else "disabled"
        ).grid(row=0, column=2, padx=10)

        tk.Button(nav_frame, text="Review Answers", font=self.button_font, bg="#f77f00", fg="white",
                  activebackground="#ffd166", relief="flat", width=14, command=self.review_answers).grid(row=0, column=3, padx=15)

        self.expl_label = tk.Label(self, text="", font=self.custom_font, bg="#e9ecef", fg="#d62828", wraplength=1100)
        self.expl_label.pack(pady=10)
        if self.user_answers[self.current_q] is not None:
            self.answer_var.set(self.user_answers[self.current_q])
            self.show_explanation()

    def create_back_button(self, command):
        back_frame = tk.Frame(self, bg="#e9ecef")
        back_frame.pack(fill='x', pady=8)
        tk.Button(back_frame, text="⟵ Back", font=self.custom_font, bg="#adb5bd", fg="white",
                  activebackground="#ced4da", relief="flat", width=8, command=command).pack(anchor='w', padx=20)

    def ask_quit_and_score(self):
        if self.dialog_open:
            return
        self.dialog_open = True
        self.after(100, self._show_quit_dialog)

    def _show_quit_dialog(self):
        result = messagebox.askyesno("Quit Quiz", "Do you want to quit and see your score?", parent=self)
        self.dialog_open = False
        if result:
            self.timer_running = False
            self.show_results(force_aborted=True)

    def submit_answer(self):
        answer = self.answer_var.get()
        if not answer:
            messagebox.showwarning("Select an answer", "Please select an option before submitting.")
            return
        already_answered = self.user_answers[self.current_q] is not None
        self.user_answers[self.current_q] = answer
        if not already_answered:
            if answer == self.quiz_data[self.current_q]["answer"]:
                self.score += 1
        self.show_explanation()
        if all(ans is not None for ans in self.user_answers):
            self.submit_btn.config(state="disabled")

    def show_explanation(self):
        correct = self.quiz_data[self.current_q]["answer"]
        user_ans = self.user_answers[self.current_q]
        expl = self.quiz_data[self.current_q]["explanation"]
        if user_ans == correct:
            self.expl_label.config(text=f"✅ Correct! {expl}", fg="#2c7a7b")
        else:
            self.expl_label.config(text=f"❌ Incorrect! Correct answer: {correct}\nExplanation: {expl}", fg="#d62828")
        self.submit_btn.config(state="disabled")

    def prev_question(self):
        self.current_q -= 1
        self.build_ui()

    def next_question(self):
        self.current_q += 1
        self.build_ui()

    def review_answers(self):
        self.timer_running = False
        self.reviewing = True
        self.clear()
        tk.Label(self, text="Review Your Answers", font=self.title_font, bg="#e9ecef", fg="#003049").pack(pady=20)
        # Add a container frame to hold canvas and scrollbar
        container = tk.Frame(self, bg="#e9ecef")
        container.pack(fill='both', expand=True)

        canvas = tk.Canvas(container, bg="#e9ecef", highlightthickness=0, width=1250, height=600)
        canvas.pack(side="left", fill='both', expand=True)
        vsb = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        frame = tk.Frame(canvas, bg="#e9ecef")
        canvas.create_window((0,0), window=frame, anchor='nw')

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox('all'))
        frame.bind('<Configure>', on_frame_configure)

        def _on_mousewheel(event):
                canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            # Windows and MacOS
        canvas.bind("<Enter>", lambda e: canvas.focus_set())
        canvas.bind("<Leave>", lambda e: self.focus_set())

        canvas.bind("<MouseWheel>", _on_mousewheel)
        canvas.bind("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))
        canvas.bind("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))
        for idx, q in enumerate(self.quiz_data):
            f = tk.Frame(frame, bg="#e9ecef")
            f.grid(row=idx, column=0, sticky="w", pady=2, padx=2)
            qtext = f"Q{idx+1}. {q['question'][:60]}{'...' if len(q['question'])>60 else ''}"
            tk.Label(f, text=qtext, font=self.custom_font, bg="#e9ecef", fg="#212529", width=55, anchor="w").pack(side="left")
            selected = self.user_answers[idx] or "Not answered"
            tk.Label(f, text=f"Your answer: {selected}", font=self.custom_font, bg="#e9ecef", fg="#2a9d8f" if selected == q['answer'] else "#d62828", width=28, anchor="w").pack(side="left")
            tk.Button(f, text="Change", font=self.button_font, bg="#f77f00", fg="white", width=7,
                      command=lambda i=idx: self.go_to_question(i)).pack(side="left", padx=5)

        btn_frame = tk.Frame(self, bg="#e9ecef")
        btn_frame.pack(pady=18)
        tk.Button(btn_frame, text="Submit Quiz", font=self.button_font, bg="#2a9d8f", fg="white",
                  activebackground="#52b788", relief="flat", width=18, command=self.submit_quiz_from_review).pack(side="left", padx=18)
        tk.Button(btn_frame, text="Return to Quiz", font=self.button_font, bg="#adb5bd", fg="white",
                  activebackground="#ced4da", relief="flat", width=18, command=self.return_to_quiz).pack(side="left", padx=18)

    def submit_quiz_from_review(self):
        if any(ans is None for ans in self.user_answers):
            if not messagebox.askyesno("Unanswered", "Some questions are unanswered. Submit anyway?"):
                return
        self.show_results(force_aborted=False)

    def return_to_quiz(self):
        self.reviewing = False
        self.timer_running = True
        self.build_ui()
        self.update_timer()

    def go_to_question(self, idx):
        self.current_q = idx
        self.reviewing = False
        self.timer_running = True
        self.build_ui()
        self.update_timer()

    def show_results(self, force_aborted=False):
        self.timer_running = False
        self.clear()
        answered = [a for a in self.user_answers if a is not None]
        correct = 0
        for idx, ans in enumerate(self.user_answers):
            if ans is not None and ans == self.quiz_data[idx]["answer"]:
                correct += 1
        title = "Quiz Completed!" if not force_aborted and len(answered) == self.num_questions else "Quiz Ended!"
        tk.Label(self, text=title, font=self.title_font, bg="#e9ecef", fg="#003049").pack(pady=10)
        tk.Label(self, text=f"Subject: {self.subject}", font=self.custom_font, bg="#e9ecef", fg="#264653").pack(pady=6)
        tk.Label(self, text=f"Your Score: {correct} / {len(answered)}", font=self.custom_font, bg="#e9ecef", fg="#2a9d8f").pack(pady=6)
        tk.Label(self, text=f"Time Used: {self.time_used_str()}", font=self.custom_font, bg="#e9ecef", fg="#6a4c93").pack(pady=6)
        ratio = correct / len(answered) if answered else 0
        color = "#2a9d8f" if ratio >= 0.8 else "#f77f00" if ratio >= 0.5 else "#d62828"
        tk.Label(self, text="Performance: "+("Excellent!" if ratio >= 0.8 else "Good" if ratio >= 0.5 else "Needs Practice"),
                 font=self.custom_font, bg="#e9ecef", fg=color).pack(pady=8)
        # Save result to SQLite database
        save_result(self.subject, correct, self.num_questions, self.time_used_str())
        # Show full answers table
        # --- Add scrollable result area START ---
        container = tk.Frame(self, bg="#e9ecef")
        container.pack(pady=10, fill='both', expand=True)

        canvas = tk.Canvas(container, bg="#e9ecef", highlightthickness=0, width=1250, height=400)
        canvas.pack(side="left", fill="both", expand=True)
        vsb = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        result_frame = tk.Frame(canvas, bg="#e9ecef")
        canvas.create_window((0,0), window=result_frame, anchor='nw')

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox('all'))
        result_frame.bind('<Configure>', on_frame_configure)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind("<Enter>", lambda e: canvas.focus_set())
        canvas.bind("<Leave>", lambda e: self.focus_set())

        canvas.bind("<MouseWheel>", _on_mousewheel)
        canvas.bind("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))
        canvas.bind("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))
        # --- Add scrollable result area END ---
        header = tk.Frame(result_frame, bg="#e9ecef")
        header.pack()
        tk.Label(header, text="Q#", font=self.button_font, width=3, bg="#e9ecef").pack(side="left")
        tk.Label(header, text="Question", font=self.button_font, width=42, bg="#e9ecef").pack(side="left")
        tk.Label(header, text="Your Answer", font=self.button_font, width=17, bg="#e9ecef").pack(side="left")
        tk.Label(header, text="Correct Answer", font=self.button_font, width=17, bg="#e9ecef").pack(side="left")
        tk.Label(header, text="Explanation", font=self.button_font, width=33, bg="#e9ecef").pack(side="left")

        for idx, q in enumerate(self.quiz_data):
            a = self.user_answers[idx] or "Not answered"
            correct_a = q['answer']
            expl = q['explanation']
            row = tk.Frame(result_frame, bg="#f0f0f0" if idx%2==0 else "#fff")
            row.pack(fill="x")
            tk.Label(row, text=f"{idx+1}", font=self.custom_font, width=3, anchor="w", bg=row['bg']).pack(side="left")
            tk.Label(row, text=q['question'][:36] + ("..." if len(q['question'])>36 else ""), font=self.custom_font, width=42, anchor="w", bg=row['bg']).pack(side="left")
            tk.Label(row, text=a, font=self.custom_font, width=17, anchor="w", fg="#2a9d8f" if a==correct_a else "#d62828", bg=row['bg']).pack(side="left")
            tk.Label(row, text=correct_a, font=self.custom_font, width=17, anchor="w", fg="#2a9d8f", bg=row['bg']).pack(side="left")
            tk.Label(row, text=expl[:45]+("..." if len(expl)>45 else ""), font=self.custom_font, width=33, anchor="w", bg=row['bg']).pack(side="left")

        btn_frame = tk.Frame(self, bg="#e9ecef")
        btn_frame.pack(pady=15)
        tk.Button(btn_frame, text="Export Results", font=self.button_font, bg="#457b9d", fg="white",
                  activebackground="#a8dadc", relief="flat", width=22, command=lambda: self.export_results(correct, len(answered))).pack(side="left", padx=18)
        tk.Button(btn_frame, text="Back to Subject List", font=self.button_font, bg="#adb5bd", fg="white",
                  activebackground="#ced4da", relief="flat", width=22, command=self.on_back_to_subjects).pack(side="left", padx=18)

    def on_back_to_subjects(self):
        self.destroy()
        self.master.show_subject_menu()

    def export_results(self, correct, total):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text Files", "*.txt")],
            title="Export Quiz Results"
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"EduMatrix MCQ Quiz Results\n")
                f.write(f"Subject: {self.subject}\n")
                f.write(f"Score: {correct} / {total}\n")
                f.write(f"Time Used: {self.time_used_str()}\n\n")
                for idx, q in enumerate(self.quiz_data):
                    f.write(f"Q{idx+1}: {q['question']}\n")
                    f.write(f"Your answer: {self.user_answers[idx] or 'Not answered'}\n")
                    f.write(f"Correct answer: {q['answer']}\n")
                    f.write(f"Explanation: {q['explanation']}\n\n")
            messagebox.showinfo("Exported!", "Results exported successfully.")

    def update_timer_label(self):
        mins, secs = divmod(self.remaining_seconds, 60)
        self.timer_label.config(text=f"Time Left: {mins:02d}:{secs:02d}")
        if self.remaining_seconds <= 30:
            self.timer_label.config(fg="#d62828")
        elif self.remaining_seconds <= 120:
            self.timer_label.config(fg="#f77f00")
        else:
            self.timer_label.config(fg="#2a9d8f")

    def update_timer(self):
        if not hasattr(self, 'timer_label') or self.timer_label is None:
            return
        if self.timer_running and not self.reviewing:
            self.update_timer_label()
            if self.remaining_seconds > 0:
                self.remaining_seconds -= 1
                self.after(1000, self.update_timer)
            else:
                messagebox.showwarning("Time's Up", "Time is up! The quiz will be submitted.")
                self.show_results(force_aborted=False)

    def time_used_str(self):
        used = QUIZ_TIME_SECONDS - self.remaining_seconds
        mins, secs = divmod(max(0, used), 60)
        return f"{mins:02d}:{secs:02d}"
# ================== GAME CENTER MENU ==================
def game_center_menu(self):
    self.clear()
    self.create_back_button(self.show_main_menu)
    tk.Label(self, text="Game Center", font=self.title_font, bg="#e9ecef", fg="#d62828").pack(pady=32)
    tk.Label(self, text="Select a Game to Play", font=self.button_font, bg="#e9ecef", fg="#003049").pack(pady=10)
    game_frame = tk.Frame(self, bg="#e9ecef")
    game_frame.pack(pady=24)
    games = [
        ("🃏 Flashcards", "flashcards"),
        ("🎩 Hangman", "hangman"),
        ("🧩 Puzzle Game (Code Order)", "puzzle"),
        ("🧠 Memory Game (Pairs)", "memory"),
        ("🔍 Word Search", "wordsearch"),
        ("⌨️ Typing Challenge", "typing"),
    ]
    for i, (gname, gkey) in enumerate(games):
        tk.Button(
            game_frame, text=gname, font=self.custom_font, width=32, height=2,
            bg="#f77f00" if i % 2 == 0 else "#457b9d", fg="white",
            activebackground="#a8dadc", relief="raised",
            command=lambda key=gkey: self.game_subject_menu(key)
        ).grid(row=i//2, column=i%2, padx=18, pady=8)

def game_subject_menu(self, game_key):
    self.clear()
    self.create_back_button(self.game_center_menu)
    tk.Label(self, text="Select Subject", font=self.title_font, bg="#e9ecef", fg="#003049").pack(pady=32)
    sub_frame = tk.Frame(self, bg="#e9ecef")
    sub_frame.pack(pady=24)
    for i, subject in enumerate(self.subjects):
        tk.Button(
            sub_frame, text=subject, font=self.custom_font, width=22, height=2,
            bg="#2a9d8f" if i % 2 == 0 else "#6a4c93", fg="white",
            activebackground="#52b788", relief="raised",
            command=lambda s=subject, g=game_key: self.launch_game(g, s)
        ).grid(row=i//2, column=i%2, padx=28, pady=16)

def launch_game(self, game_key, subject):
    if game_key == "flashcards":
        FlashcardsGameWindow(self, subject)
    elif game_key == "hangman":
        HangmanGameWindow(self, subject)
    elif game_key == "puzzle":
        PuzzleGameWindow(self, subject)
    elif game_key == "memory":
        MemoryGameWindow(self, subject)
    elif game_key == "wordsearch":
        WordSearchGameWindow(self, subject)
    elif game_key == "typing":
        TypingChallengeWindow(self, subject)

# Attach to the EduMatrixApp class
EduMatrixApp.show_game_menu = game_center_menu
EduMatrixApp.game_center_menu = game_center_menu
EduMatrixApp.game_subject_menu = game_subject_menu
EduMatrixApp.launch_game = launch_game

# ================== FLASHCARDS GAME ==================
class FlashcardsGameWindow(tk.Toplevel):
    def __init__(self, master, subject):
        super().__init__(master)
        self.subject = subject
        self.title(f"Flashcards - {subject}")
        self.state('zoomed')
        self.configure(bg="#e9ecef")
        self.custom_font = font.Font(family="Segoe UI", size=20)
        self.title_font = font.Font(family="Segoe UI", size=32, weight="bold")
        self.mcqs = list(SUBJECTS[subject])
        random.shuffle(self.mcqs)
        self.idx = 0
        self.showing_answer = False
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.build_ui()

    def build_ui(self):
        self.clear()
        tk.Label(self, text=f"Flashcards: {self.subject}", font=self.title_font, bg="#e9ecef", fg="#d62828").pack(pady=16)
        self.card_frame = tk.Frame(self, bg="#f7fff7", bd=4, relief="ridge", padx=20, pady=20)
        self.card_frame.pack(pady=30, fill="both", expand=True)
        self.q_label = tk.Label(self.card_frame, text="", font=self.custom_font, wraplength=700, bg="#f7fff7", fg="#003049")
        self.q_label.pack(pady=10)
        self.a_label = tk.Label(self.card_frame, text="", font=self.custom_font, wraplength=700, bg="#f7fff7", fg="#2a9d8f")
        self.a_label.pack(pady=10)
        self.btn_frame = tk.Frame(self, bg="#e9ecef")
        self.btn_frame.pack(pady=12)
        tk.Button(self.btn_frame, text="⟵ Previous", font=self.custom_font, bg="#adb5bd", fg="white",
                  activebackground="#ced4da", relief="flat", width=10, command=self.prev_card).grid(row=0, column=0, padx=16)
        tk.Button(self.btn_frame, text="Flip", font=self.custom_font, bg="#2a9d8f", fg="white",
                  activebackground="#52b788", relief="flat", width=12, command=self.flip_card).grid(row=0, column=1, padx=16)
        tk.Button(self.btn_frame, text="Next ⟶", font=self.custom_font, bg="#457b9d", fg="white",
                  activebackground="#a8dadc", relief="flat", width=10, command=self.next_card).grid(row=0, column=2, padx=16)
        self.status_label = tk.Label(self, text="", font=self.custom_font, bg="#e9ecef", fg="#495057")
        self.status_label.pack(pady=10)
        self.show_card()

    def show_card(self):
        qdata = self.mcqs[self.idx]
        self.q_label.config(text=f"Q{self.idx+1}: {qdata['question']}")
        if self.showing_answer:
            self.a_label.config(text=f"Answer: {qdata['answer']}\n\n{qdata['explanation']}")
        else:
            self.a_label.config(text="(Tap 'Flip' to reveal the answer)")
        self.status_label.config(text=f"Card {self.idx+1} of {len(self.mcqs)}")

    def prev_card(self):
        if self.idx > 0:
            self.idx -= 1
            self.showing_answer = False
            self.show_card()

    def next_card(self):
        if self.idx < len(self.mcqs) - 1:
            self.idx += 1
            self.showing_answer = False
            self.show_card()

    def flip_card(self):
        self.showing_answer = not self.showing_answer
        self.show_card()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def on_close(self):
        self.destroy()

# ================== HANGMAN GAME ==================
class HangmanGameWindow(tk.Toplevel):
    def __init__(self, master, subject):
        super().__init__(master)
        self.subject = subject
        self.title(f"Hangman - {subject}")
        self.state('zoomed')
        self.configure(bg="#e9ecef")
        self.custom_font = font.Font(family="Segoe UI", size=20)
        keywords = [q["answer"] for q in SUBJECTS[subject]]
        self.word = random.choice([w for w in keywords if w.isalpha() and len(w) > 3]).lower()
        self.guessed = set()
        self.tries = 8
        self.build_ui()

    def build_ui(self):
        self.clear()
        tk.Label(self, text=f"Hangman: {self.subject}", font=self.custom_font, bg="#e9ecef", fg="#d62828").pack(pady=10)
        self.word_label = tk.Label(self, text=self.get_display_word(), font=self.custom_font, bg="#e9ecef")
        self.word_label.pack(pady=10)
        self.entry = tk.Entry(self, font=self.custom_font, width=5)
        self.entry.pack()
        self.entry.bind("<Return>", lambda e: self.guess())
        self.guess_btn = tk.Button(self, text="Guess", font=self.custom_font, command=self.guess)
        self.guess_btn.pack(pady=5)
        self.status_label = tk.Label(self, text=f"Tries left: {self.tries}", font=self.custom_font, bg="#e9ecef")
        self.status_label.pack(pady=5)
        self.guessed_label = tk.Label(self, text="Guessed: ", font=self.custom_font, bg="#e9ecef")
        self.guessed_label.pack(pady=5)

    def get_display_word(self):
        return " ".join([c if c in self.guessed else "_" for c in self.word])

    def guess(self):
        letter = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        if not letter or not letter.isalpha() or len(letter) != 1:
            self.status_label.config(text="Enter a single letter.")
            return
        if letter in self.guessed:
            self.status_label.config(text="Already guessed.")
            return
        self.guessed.add(letter)
        if letter not in self.word:
            self.tries -= 1
        self.word_label.config(text=self.get_display_word())
        self.status_label.config(text=f"Tries left: {self.tries}")
        self.guessed_label.config(text="Guessed: " + ", ".join(sorted(self.guessed)))
        if "_" not in self.get_display_word():
            messagebox.showinfo("Hangman", f"You Win! The word was '{self.word}'.")
            self.destroy()
        elif self.tries == 0:
            messagebox.showinfo("Hangman", f"Out of tries! The word was '{self.word}'.")
            self.destroy()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

# ================== PUZZLE GAME (CODE ORDER) ==================
class PuzzleGameWindow(tk.Toplevel):
    def __init__(self, master, subject):
        super().__init__(master)
        self.subject = subject
        self.title(f"Puzzle Game - {subject}")
        self.state('zoomed')
        self.configure(bg="#e9ecef")
        self.custom_font = font.Font(family="Segoe UI", size=20)
        self.puzzle_data = self.pick_code_order_puzzle()
        self.shuffled = self.puzzle_data.copy()
        random.shuffle(self.shuffled)
        self.build_ui()

    def pick_code_order_puzzle(self):
        # For demo, pick explanation as "lines of code" split to steps if available
        for q in SUBJECTS[self.subject]:
            if " " in q["answer"]:
                lines = q["answer"].split(" ")
                if len(lines) >= 3:
                    return lines
        # fallback
        return ["print('Hello')", "print('World')", "print('!')"]

    def build_ui(self):
        self.clear()
        tk.Label(self, text="Arrange the code in correct order:", font=self.custom_font, bg="#e9ecef").pack(pady=10)
        self.listbox = tk.Listbox(self, font=self.custom_font, selectmode=tk.SINGLE, width=40, height=len(self.shuffled))
        for line in self.shuffled:
            self.listbox.insert(tk.END, line)
        self.listbox.pack(pady=10)
        self.listbox.bind('<Double-Button-1>', self.move_up)
        tk.Button(self, text="Check Order", command=self.check_order, font=self.custom_font).pack(pady=10)
        self.status_label = tk.Label(self, text="", font=self.custom_font, bg="#e9ecef")
        self.status_label.pack(pady=5)

    def move_up(self, event):
        idx = self.listbox.curselection()
        if idx and idx[0] > 0:
            val = self.listbox.get(idx)
            self.listbox.delete(idx)
            self.listbox.insert(idx[0]-1, val)
            self.listbox.selection_set(idx[0]-1)

    def check_order(self):
        user_order = [self.listbox.get(i) for i in range(self.listbox.size())]
        if user_order == self.puzzle_data:
            messagebox.showinfo("Puzzle Game", "Correct Order! Well done.")
            self.destroy()
        else:
            self.status_label.config(text="Incorrect order. Try again.")

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

# ================== MEMORY GAME (PAIRS) ==================
class MemoryGameWindow(tk.Toplevel):
    def __init__(self, master, subject):
        super().__init__(master)
        self.subject = subject
        self.title(f"Memory Game - {subject}")
        self.state('zoomed')
        self.configure(bg="#e9ecef")
        self.custom_font = font.Font(family="Segoe UI", size=20)
        self.pairs = self.pick_memory_pairs()
        self.buttons = []
        self.flipped = []
        self.solved = set()
        self.build_ui()

    def pick_memory_pairs(self):
        questions = random.sample(SUBJECTS[self.subject], 5)
        pairs = []
        for q in questions:
            pairs.append((q["question"], q["answer"]))
        flat = []
        for q, a in pairs:
            flat.append(("Q", q))
            flat.append(("A", a))
        random.shuffle(flat)
        return flat

    def build_ui(self):
        self.clear()
        tk.Label(self, text="Match Questions with Answers!", font=self.custom_font, bg="#e9ecef").pack(pady=10)
        self.grid_frame = tk.Frame(self, bg="#e9ecef")
        self.grid_frame.pack()
        self.buttons = []
        for i, (typ, val) in enumerate(self.pairs):
            btn = tk.Button(self.grid_frame, text="❓", font=self.custom_font, width=30, height=2,
                            command=lambda idx=i: self.flip(idx))
            btn.grid(row=i//2, column=i%2, padx=10, pady=10)
            self.buttons.append(btn)
        self.flipped = []
        self.solved = set()

    def flip(self, idx):
        if idx in self.solved or idx in self.flipped:
            return
        btn = self.buttons[idx]
        typ, val = self.pairs[idx]
        btn.config(text=val)
        self.flipped.append(idx)
        if len(self.flipped) == 2:
            i1, i2 = self.flipped
            t1, v1 = self.pairs[i1]
            t2, v2 = self.pairs[i2]
            if ((t1 == "Q" and t2 == "A" and v2 in v1) or (t2 == "Q" and t1 == "A" and v1 in v2)):
                self.solved.update([i1, i2])
                self.flipped.clear()
                if len(self.solved) == len(self.buttons):
                    messagebox.showinfo("Memory Game", "All pairs matched! Good job!")
                    self.destroy()
            else:
                self.after(1000, self.unflip)

    def unflip(self):
        for idx in self.flipped:
            self.buttons[idx].config(text="❓")
        self.flipped.clear()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

# ================== WORD SEARCH GAME ==================
class WordSearchGameWindow(tk.Toplevel):
    def __init__(self, master, subject):
        super().__init__(master)
        self.subject = subject
        self.title(f"Word Search - {subject}")
        self.state('zoomed')
        self.configure(bg="#e9ecef")
        self.custom_font = font.Font(family="Segoe UI", size=18)
        self.words = random.sample([q["answer"] for q in SUBJECTS[subject] if q["answer"].isalpha()], 5)
        self.grid, self.word_positions = self.create_grid(self.words)
        self.selected_word = tk.StringVar()
        self.build_ui()
    
    def create_grid(self, words):
        size = 12
        grid = [["" for _ in range(size)] for _ in range(size)]
        positions = []
        for idx, word in enumerate(words):
            row = idx*2
            for col, letter in enumerate(word.upper()):
                grid[row][col] = letter
            positions.append((row, word))
        # Fill empty cells
        for r in range(size):
            for c in range(size):
                if not grid[r][c]:
                    grid[r][c] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return grid, positions

    def build_ui(self):
        self.clear()
        tk.Label(self, text="Find these words:", font=self.custom_font, bg="#e9ecef").pack()
        tk.Label(self, text=", ".join(self.words), font=self.custom_font, bg="#e9ecef").pack()
        self.grid_frame = tk.Frame(self, bg="#e9ecef")
        self.grid_frame.pack(pady=10)
        for r in range(12):
            for c in range(12):
                tk.Label(self.grid_frame, text=self.grid[r][c], font=self.custom_font, width=2, bg="#fff", relief="solid").grid(row=r, column=c)
        self.entry = tk.Entry(self, font=self.custom_font)
        self.entry.pack(pady=10)
        tk.Button(self, text="Submit Word", font=self.custom_font, command=self.check_word).pack()
        self.status_label = tk.Label(self, text="", font=self.custom_font, bg="#e9ecef")
        self.status_label.pack(pady=5)
        self.found = set()

    def check_word(self):
        word = self.entry.get().strip().lower()
        self.entry.delete(0, tk.END)
        if not word or word not in [w.lower() for w in self.words]:
            self.status_label.config(text="Not in list.")
            return
        if word in self.found:
            self.status_label.config(text="Already found.")
            return
        self.found.add(word)
        self.status_label.config(text=f"Found {word}!")
        if len(self.found) == len(self.words):
            messagebox.showinfo("Word Search", "All words found! Well done.")
            self.destroy()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

# ================== TYPING CHALLENGE GAME ==================
class TypingChallengeWindow(tk.Toplevel):
    def __init__(self, master, subject):
        super().__init__(master)
        self.subject = subject
        self.title(f"Typing Challenge - {subject}")
        self.state('zoomed')
        self.configure(bg="#e9ecef")
        self.custom_font = font.Font(family="Segoe UI", size=20)
        self.sentences = [q["question"] for q in random.sample(SUBJECTS[subject], 5)]
        self.idx = 0
        self.start_time = None
        self.build_ui()

    def build_ui(self):
        self.clear()
        tk.Label(self, text="Type the sentence as quickly and accurately as you can!", font=self.custom_font, bg="#e9ecef").pack(pady=10)
        self.sentence_label = tk.Label(self, text=self.sentences[self.idx], font=self.custom_font, bg="#e9ecef", wraplength=800)
        self.sentence_label.pack(pady=10)
        self.entry = tk.Entry(self, font=self.custom_font, width=60)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda e: self.check())
        self.status_label = tk.Label(self, text="", font=self.custom_font, bg="#e9ecef")
        self.status_label.pack()
        self.start_time = time.time()

    def check(self):
        typed = self.entry.get().strip()
        expected = self.sentences[self.idx].strip()
        if typed == expected:
            self.idx += 1
            if self.idx == len(self.sentences):
                elapsed = time.time() - self.start_time
                messagebox.showinfo("Typing Challenge", f"Completed! Time: {elapsed:.2f} seconds.")
                self.destroy()
            else:
                self.entry.delete(0, tk.END)
                self.sentence_label.config(text=self.sentences[self.idx])
        else:
            self.status_label.config(text="Incorrect! Try again.")

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()
import tkinter as tk
from tkinter import font, ttk, scrolledtext

LANG_SYNTAX = {
    "Python": {
        "Variables": {
            "syntax": "x = 42\nname = \"Alice\"\npi = 3.14",
            "explanation": "Python uses dynamic typing. No need to declare type. Strings use single or double quotes."
        },
        "Data Types": {
            "syntax": "num = 10         # int\nflt = 3.14      # float\nname = 'Bob'    # str\nlst = [1,2,3]   # list\ntup = (1,2,3)   # tuple\nst = {1,2,3}    # set\ndct = {'a':1}   # dict",
            "explanation": "Common types are int, float, str, list, tuple, set, dict. Use type(var) to check type."
        },
        "Input/Output": {
            "syntax": "name = input('Enter name: ')\nprint('Hello,', name)",
            "explanation": "Use input() to get user input, print() to display output."
        },
        "If-Else Condition": {
            "syntax": "if age >= 18:\n    print('Adult')\nelse:\n    print('Minor')",
            "explanation": "Indentation is used for code blocks. elif is used for else-if."
        },
        "For Loop": {
            "syntax": "for i in range(5):\n    print(i)\n\nfor item in [10,20,30]:\n    print(item)",
            "explanation": "Use range() for a sequence of numbers. You can loop over any iterable."
        },
        "While Loop": {
            "syntax": "count = 0\nwhile count < 5:\n    print(count)\n    count += 1",
            "explanation": "while repeats the block as long as condition is True."
        },
        "Functions": {
            "syntax": "def greet(name):\n    print('Hello', name)\ngreet('Jenish')",
            "explanation": "def keyword defines a function. Functions can return values using return."
        },
        "Lists": {
            "syntax": "nums = [1,2,3]\nnums.append(4)\nnums[0] = 10\nprint(nums)",
            "explanation": "Lists are mutable, ordered, and can store mixed types."
        },
        "Tuples": {
            "syntax": "point = (2, 3)\nx, y = point",
            "explanation": "Tuples are immutable, ordered collections. Useful for fixed data."
        },
        "Dictionaries": {
            "syntax": "person = {'name':'Alice', 'age':22}\nprint(person['name'])",
            "explanation": "Dictionaries store key-value pairs. Keys must be unique."
        },
        "Set": {
            "syntax": "nums = {1,2,3,2}\nnums.add(4)",
            "explanation": "Sets store unique items. Useful for membership checks."
        },
        "Class & Object": {
            "syntax": "class Dog:\n    def __init__(self, name):\n        self.name = name\n    def bark(self):\n        print(self.name, 'says woof!')\nd = Dog('Buddy')\nd.bark()",
            "explanation": "Classes group data and functions. __init__ is the constructor."
        },
        "Exception Handling": {
            "syntax": "try:\n    x = 1/0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero!')",
            "explanation": "Handle errors using try-except blocks."
        },
        "File I/O": {
            "syntax": "with open('data.txt', 'r') as f:\n    content = f.read()",
            "explanation": "with handles file closing automatically. Use 'w' for writing."
        },
        "Importing Modules": {
            "syntax": "import math\nprint(math.sqrt(16))",
            "explanation": "Use import to access standard or custom modules."
        },
    },
    "Java": {
        "Variables": {
            "syntax": "int age = 25;\ndouble pi = 3.14;\nString name = \"Jenish\";",
            "explanation": "Variables must be declared with their type."
        },
        "Data Types": {
            "syntax": "int x = 10;\nfloat y = 5.5f;\nchar c = 'A';\nboolean done = false;\nString s = \"Hello\";",
            "explanation": "Primitive types: int, float, double, char, boolean. String is a class."
        },
        "Input/Output": {
            "syntax": "import java.util.Scanner;\nScanner sc = new Scanner(System.in);\nint n = sc.nextInt();\nSystem.out.println(\"Value: \" + n);",
            "explanation": "Use Scanner for input, System.out.println for output."
        },
        "If-Else Condition": {
            "syntax": "if (age >= 18) {\n    System.out.println(\"Adult\");\n} else {\n    System.out.println(\"Minor\");\n}",
            "explanation": "Use curly braces for code blocks. else if is allowed."
        },
        "For Loop": {
            "syntax": "for (int i=0; i<5; i++) {\n    System.out.println(i);\n}",
            "explanation": "Classic C-style for loop."
        },
        "While Loop": {
            "syntax": "int count = 0;\nwhile (count < 5) {\n    System.out.println(count);\n    count++;\n}",
            "explanation": "while repeats block as long as condition is true."
        },
        "Functions/Methods": {
            "syntax": "public static int add(int a, int b) {\n    return a + b;\n}",
            "explanation": "All code is inside a class. Methods can be static or instance."
        },
        "Array": {
            "syntax": "int[] arr = {1,2,3};\nSystem.out.println(arr[0]);",
            "explanation": "Arrays are fixed-size and zero-indexed."
        },
        "ArrayList": {
            "syntax": "import java.util.ArrayList;\nArrayList<Integer> nums = new ArrayList<>();\nnums.add(10);",
            "explanation": "ArrayList is resizable, supports add, remove, etc."
        },
        "String": {
            "syntax": "String s = \"hello\";\nSystem.out.println(s.length());",
            "explanation": "String is immutable. Use methods like charAt, length, substring."
        },
        "Class & Object": {
            "syntax": "class Dog {\n    String name;\n    void bark() {\n        System.out.println(name + \" says woof!\");\n    }\n}\nDog d = new Dog();\nd.name = \"Buddy\";\nd.bark();",
            "explanation": "Classes define blueprint, objects are instances."
        },
        "Inheritance": {
            "syntax": "class Animal {}\nclass Dog extends Animal {}",
            "explanation": "Use extends for class inheritance."
        },
        "Interface": {
            "syntax": "interface Drawable { void draw(); }\nclass Circle implements Drawable {\n    public void draw() { System.out.println(\"Circle\"); }\n}",
            "explanation": "Interfaces define methods to implement."
        },
        "Exception Handling": {
            "syntax": "try {\n    int x = 1/0;\n} catch (ArithmeticException e) {\n    System.out.println(\"Error!\");\n}",
            "explanation": "Use try-catch to handle exceptions."
        },
        "File I/O": {
            "syntax": "import java.io.*;\nBufferedReader br = new BufferedReader(new FileReader(\"file.txt\"));\nString line = br.readLine();\nbr.close();",
            "explanation": "Use BufferedReader for reading files."
        }
    },
    "C++": {
        "Variables": {
            "syntax": "int age = 20;\ndouble pi = 3.14;\nstring name = \"Jenish\";",
            "explanation": "#include <string> for string. Variables need type."
        },
        "Data Types": {
            "syntax": "int x = 10;\ndouble d = 2.5;\nchar c = 'A';\nbool ok = false;\nstring s = \"Hi\";",
            "explanation": "Basic types: int, double, char, bool, string."
        },
        "Input/Output": {
            "syntax": "#include <iostream>\nusing namespace std;\ncout << \"Hello\" << endl;\nint n;\ncin >> n;",
            "explanation": "Use cout for output, cin for input."
        },
        "If-Else Condition": {
            "syntax": "if (x > 0) {\n    cout << \"Positive\";\n} else {\n    cout << \"Non-positive\";\n}",
            "explanation": "Use curly braces for blocks."
        },
        "For Loop": {
            "syntax": "for (int i=0; i<5; i++) {\n    cout << i << endl;\n}",
            "explanation": "Classic for loop. All 3 expressions required."
        },
        "While Loop": {
            "syntax": "int count = 0;\nwhile (count < 5) {\n    cout << count << endl;\n    count++;\n}",
            "explanation": "while executes as long as condition is true."
        },
        "Functions": {
            "syntax": "int add(int a, int b) {\n    return a + b;\n}",
            "explanation": "Specify return type, name, and parameters."
        },
        "Array": {
            "syntax": "int arr[3] = {1,2,3};\ncout << arr[0];",
            "explanation": "Arrays are fixed size and zero-indexed."
        },
        "Vector": {
            "syntax": "#include <vector>\nvector<int> v = {1,2,3};\nv.push_back(4);",
            "explanation": "Vectors are dynamic arrays in C++ STL."
        },
        "String": {
            "syntax": "#include <string>\nstring s = \"hi\";\ncout << s.length();",
            "explanation": "Use string class for text."
        },
        "Class & Object": {
            "syntax": "class Dog {\npublic:\n    string name;\n    void bark() { cout << name << \" says woof!\"; }\n};\nDog d;\nd.name = \"Buddy\";\nd.bark();",
            "explanation": "Classes group data and functions."
        },
        "Inheritance": {
            "syntax": "class Animal {};\nclass Dog : public Animal {};",
            "explanation": "Use : public for inheritance."
        },
        "Pointer": {
            "syntax": "int x = 5;\nint *p = &x;\ncout << *p;",
            "explanation": "Pointers store memory addresses. Use * and &."
        },
        "Exception Handling": {
            "syntax": "try {\n    throw 10;\n} catch (int e) {\n    cout << \"Error: \" << e;\n}",
            "explanation": "try-catch handles exceptions."
        },
        "File I/O": {
            "syntax": "#include <fstream>\nifstream fin(\"file.txt\");\nstring line;\ngetline(fin, line);\nfin.close();",
            "explanation": "ifstream for reading, ofstream for writing."
        }
    },
    "Web": {
        "HTML Structure": {
            "syntax": "<!DOCTYPE html>\n<html>\n<head><title>Page</title></head>\n<body>\n<h1>Hello</h1>\n</body>\n</html>",
            "explanation": "Basic HTML structure with head and body."
        },
        "Paragraph & Headings": {
            "syntax": "<h1>Main Heading</h1>\n<p>This is a paragraph.</p>",
            "explanation": "Use <h1>-<h6> for headings, <p> for paragraph."
        },
        "Links & Images": {
            "syntax": "<a href='https://example.com'>Visit</a>\n<img src='img.png' alt='desc'>",
            "explanation": "<a> creates a link. <img> displays images."
        },
        "Lists": {
            "syntax": "<ul>\n  <li>Item 1</li>\n  <li>Item 2</li>\n</ul>\n<ol>\n  <li>First</li>\n</ol>",
            "explanation": "<ul> unordered, <ol> ordered lists."
        },
        "Table": {
            "syntax": "<table>\n<tr><th>Name</th></tr>\n<tr><td>Jenish</td></tr>\n</table>",
            "explanation": "Use <table>, <tr>, <th>, <td> for tables."
        },
        "CSS Selectors": {
            "syntax": "h1 { color: blue; }\n#main { font-size:20px; }\n.item { margin:10px; }",
            "explanation": "# for id, . for class."
        },
        "CSS Layout": {
            "syntax": "div {\n  display: flex;\n  justify-content: center;\n}",
            "explanation": "Use flexbox or grid for modern layouts."
        },
        "JS Variables & Types": {
            "syntax": "let x = 5;\nconst pi = 3.14;\nvar name = 'Jenish';",
            "explanation": "let/const (block scope), var (function scope)."
        },
        "JS Functions": {
            "syntax": "function greet(name) {\n  alert('Hello ' + name);\n}\ngreet('Jenish');",
            "explanation": "Use function keyword or arrow functions."
        },
        "JS Loops": {
            "syntax": "for(let i=0;i<5;i++) {\n  console.log(i);\n}",
            "explanation": "for, while, for...of, for...in available."
        },
        "JS DOM": {
            "syntax": "document.getElementById('main').innerHTML = 'Hi';",
            "explanation": "Manipulate HTML with DOM methods."
        },
        "JS Events": {
            "syntax": "<button onclick=\"myFunc()\">Click</button>\n<script>\nfunction myFunc(){alert('Hi');}\n</script>",
            "explanation": "onclick, onchange, etc. for event handling."
        },
        "Form": {
            "syntax": "<form>\n  <input type='text' name='user'>\n  <input type='submit'>\n</form>",
            "explanation": "Forms collect and submit user data."
        },
        "Responsive Design": {
            "syntax": "@media (max-width:600px) {\n  body { font-size:14px; }\n}",
            "explanation": "Media queries help with mobile design."
        },
        "Meta Tags": {
            "syntax": "<meta charset='UTF-8'>\n<meta name='viewport' content='width=device-width, initial-scale=1.0'>",
            "explanation": "Meta tags control page info and responsiveness."
        }
    },
    "Operating System": {
        "Linux Directory Commands": {
            "syntax": "ls -l     # List files\ntree      # Directory tree\npwd       # Current dir",
            "explanation": "ls lists files, tree shows structure, pwd shows path."
        },
        "File Operations": {
            "syntax": "cp file1.txt backup/\nrm file.txt\nmv file.txt docs/\ncat file.txt",
            "explanation": "cp copies, rm removes, mv moves/renames, cat displays content."
        },
        "Permissions": {
            "syntax": "chmod +x script.sh\nchown user file.txt\nls -l",
            "explanation": "chmod changes permissions, chown changes owner."
        },
        "Process Management": {
            "syntax": "ps aux\nkill 1234\ntop",
            "explanation": "ps lists, kill ends process, top shows usage."
        },
        "Networking": {
            "syntax": "ping google.com\nifconfig\nnetstat -tulnp",
            "explanation": "ping tests connection, ifconfig/netstat show network info."
        },
        "File Editing": {
            "syntax": "nano file.txt\nvim file.txt",
            "explanation": "nano and vim are file editors."
        },
        "Searching": {
            "syntax": "grep 'main' *.py\nfind . -name '*.txt'",
            "explanation": "grep searches text, find locates files."
        },
        "Shell Scripting": {
            "syntax": "#!/bin/bash\necho \"Hello World\"\nfor i in 1 2 3; do\n  echo $i\ndone",
            "explanation": "Scripts automate tasks. Use #!/bin/bash."
        },
        "Windows Commands": {
            "syntax": "dir        # List files\ncopy a.txt b.txt\ndel file.txt\ncls",
            "explanation": "dir=ls, copy=cp, del=rm, cls=clear screen."
        },
        "Environment Variables": {
            "syntax": "export PATH=$PATH:/usr/local/bin\nset VAR=value\nprintenv VAR",
            "explanation": "export/set defines env vars. printenv/echo shows them."
        },
        "Disk Usage": {
            "syntax": "df -h    # Disk free\ndu -sh * # Folder size",
            "explanation": "df shows disk space, du shows folder/file size."
        },
        "User Management": {
            "syntax": "whoami\nadduser test\npasswd test",
            "explanation": "whoami shows user, adduser creates, passwd sets password."
        },
        "Archive/Compress": {
            "syntax": "tar -czvf file.tar.gz folder/\ngzip file.txt",
            "explanation": "tar/gzip compress files/folders."
        },
        "System Info": {
            "syntax": "uname -a\nuptime\nfree -m",
            "explanation": "uname=kernel info, uptime=how long on, free=RAM."
        },
    }
}

# Keywords/Commands and their descriptions and samples (for lookup)
KEYWORD_LOOKUP = {
    "Python": {
        "append": {
            "usage": "Adds an item to the end of a list.",
            "sample": "nums = [1,2,3]\nnums.append(4)  # [1,2,3,4]"
        },
        "range": {
            "usage": "Creates a sequence of numbers, often used in for loops.",
            "sample": "for i in range(5): print(i)  # 0 1 2 3 4"
        },
        "def": {
            "usage": "Defines a function.",
            "sample": "def greet(name):\n    print('Hi', name)"
        },
        "input": {
            "usage": "Gets user input from the console.",
            "sample": "name = input('Enter: ')"
        },
        "dict": {
            "usage": "Dictionary type for key-value pairs.",
            "sample": "d = {'a':10, 'b':20}\nprint(d['a'])"
        }
    },
    "Java": {
        "System.out.println": {
            "usage": "Prints message to the console.",
            "sample": "System.out.println(\"Hello\");"
        },
        "Scanner": {
            "usage": "Used to read input from user.",
            "sample": "Scanner sc = new Scanner(System.in); int n = sc.nextInt();"
        },
        "ArrayList": {
            "usage": "Resizable array from java.util.",
            "sample": "ArrayList<String> list = new ArrayList<>();"
        },
        "public": {
            "usage": "Access modifier for classes, methods, variables.",
            "sample": "public int value;"
        },
        "static": {
            "usage": "Keyword for class-level methods/fields.",
            "sample": "public static void main(String[] args) {...}"
        }
    },
    "C++": {
        "cout": {
            "usage": "Outputs to standard output.",
            "sample": "cout << \"Hello\" << endl;"
        },
        "cin": {
            "usage": "Inputs from standard input.",
            "sample": "int n; cin >> n;"
        },
        "vector": {
            "usage": "Dynamic array from STL.",
            "sample": "#include <vector>\nvector<int> v;"
        },
        "new": {
            "usage": "Allocates dynamic memory.",
            "sample": "int* p = new int;"
        },
        "delete": {
            "usage": "Frees memory allocated by new.",
            "sample": "delete p;"
        }
    },
    "Web": {
        "<a>": {
            "usage": "Anchor tag for hyperlinks.",
            "sample": "<a href='https://example.com'>Visit</a>"
        },
        "<img>": {
            "usage": "Embeds images into a page.",
            "sample": "<img src='logo.png' alt='Logo'>"
        },
        "console.log": {
            "usage": "Prints message to browser console (JS).",
            "sample": "console.log('Hello');"
        },
        "flexbox": {
            "usage": "CSS layout model for flex containers.",
            "sample": "display: flex; justify-content: center;"
        },
        "onclick": {
            "usage": "JavaScript event, fires on click.",
            "sample": "<button onclick='myFunc()'>Click</button>"
        }
    },
    "Operating System": {
        "ls": {
            "usage": "Lists files and directories (Linux).",
            "sample": "ls -l"
        },
        "cd": {
            "usage": "Change directory.",
            "sample": "cd /home/user"
        },
        "chmod": {
            "usage": "Change file permissions.",
            "sample": "chmod +x script.sh"
        },
        "ping": {
            "usage": "Check network connectivity.",
            "sample": "ping google.com"
        },
        "nano": {
            "usage": "Terminal-based text editor.",
            "sample": "nano file.txt"
        }
    }
}

ERROR_EXPLAIN = {
    "Python": {
        "IndentationError": "Occurs when code is not properly indented. Python relies on indentation to define scope. Example: Make sure blocks after if, for, def, etc. are indented equally.",
        "TypeError": "Happens when an operation or function is applied to an object of inappropriate type. Example: Trying to add a string and an integer.",
        "NameError": "Raised when a variable is not defined. Example: Using a variable before assigning it.",
        "ZeroDivisionError": "Raised when dividing by zero. Check your denominator before dividing.",
        "SyntaxError": "General error for incorrect Python syntax. Review your code for typos or misplaced characters."
    },
    "Java": {
        "NullPointerException": "Occurs when you try to use an object reference that is not pointing to any object (null). Always check if the object is null before using.",
        "ArrayIndexOutOfBoundsException": "Happens when accessing an array index that does not exist. Make sure your index is within array bounds.",
        "ClassNotFoundException": "Thrown when the JVM can't find the class you are trying to use. Did you spell the class name correctly?",
        "NumberFormatException": "Occurs when converting a string to a number but the string is not a valid number.",
        "Syntax Error": "General error for incorrect Java syntax. Check for missing semicolons, braces, or typos."
    },
    "C++": {
        "Segmentation fault": "Commonly caused by accessing memory you shouldn't (e.g., dereferencing a null pointer). Check your pointers and array bounds.",
        "Compilation error": "General syntax or semantic error. Check for missing semicolons, brackets, or undeclared variables.",
        "Undefined reference": "Occurs when you declare something but did not define it (e.g., missing function definition).",
        "Stack overflow": "Likely caused by infinite recursion. Check recursive functions for correct base case.",
        "Memory leak": "Happens when you allocate memory with new but forget to free it with delete."
    },
    "Web": {
        "404 Not Found": "The requested resource could not be found on the server. Check URL spelling or file location.",
        "Uncaught TypeError": "JavaScript error; usually means you tried to use a value as a function or object when it isn't.",
        "CORS Error": "Browser blocked a cross-origin request. Check server headers or use the same origin.",
        "Invalid CSS Property": "You used a CSS property that does not exist or is misspelled.",
        "HTML Validation Error": "HTML is not well-formed. Use a validator to check for missing tags or attributes."
    },
    "Operating System": {
        "Permission denied": "You do not have the rights to perform this action. Use sudo or check file permissions.",
        "Command not found": "The command you typed is not recognized. Is it installed and in your PATH?",
        "File not found": "The file or directory does not exist. Check your spelling or path.",
        "Disk quota exceeded": "You've used all of your allowed disk space. Clean up files or request more space.",
        "Segmentation fault": "A program crashed due to invalid memory access. Usually a bug in C/C++ programs."
    }
}

class LanguageToolWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Language Tool")
        self.state('zoomed')
        self.configure(bg="#dbeafe")
        self.custom_font = font.Font(family="Segoe UI", size=18)
        self.title_font = font.Font(family="Segoe UI", size=32, weight="bold")
        self.topic_font = font.Font(family="Segoe UI", size=16, weight="bold")
        self.build_ui()

    def build_ui(self):
        tk.Label(self, text="🔎 Language Tool Center", font=self.title_font, bg="#dbeafe", fg="#2c3e50").pack(pady=10)
        tab_frame = tk.Frame(self, bg="#dbeafe")
        tab_frame.pack(pady=6)
        self.tabs = ["Syntax Reference", "Code Snippet", "Keyword Lookup", "Error Explanations"]
        self.tab_vars = {}
        for i, tab in enumerate(self.tabs):
            b = tk.Button(tab_frame, text=tab, font=self.topic_font, bg="#2563eb" if i==0 else "#38bdf8", fg="white",
                          width=18, height=2, relief="flat", command=lambda idx=i: self.show_tab(idx))
            b.grid(row=0, column=i, padx=6)
            self.tab_vars[tab] = b

        self.content_frame = tk.Frame(self, bg="#e0f2fe", padx=20, pady=10)
        self.content_frame.pack(fill="both", expand=True)
        self.active_tab = 0
        self.show_tab(0)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_tab(self, idx):
        for i, tab in enumerate(self.tabs):
            self.tab_vars[tab].configure(bg="#2563eb" if i==idx else "#38bdf8")
        self.active_tab = idx
        self.clear_content()
        if idx == 0:
            self.syntax_reference_tab()
        elif idx == 1:
            self.code_snippet_tab()
        elif idx == 2:
            self.keyword_lookup_tab()
        elif idx == 3:
            self.error_explanations_tab()

    # Tab 1: Syntax Reference
    def syntax_reference_tab(self):
        tk.Label(self.content_frame, text="Choose Language:", font=self.topic_font, bg="#e0f2fe").grid(row=0,column=0,sticky="w")
        lang_var = tk.StringVar(value="Python")
        langs = list(LANG_SYNTAX.keys())
        lang_dd = ttk.Combobox(self.content_frame, values=langs, textvariable=lang_var, state="readonly", font=self.custom_font)
        lang_dd.grid(row=0, column=1, sticky="w", padx=8)
        topics_label = tk.Label(self.content_frame, text="Select Topic:", font=self.topic_font, bg="#e0f2fe")
        topics_label.grid(row=1, column=0,sticky="w", pady=(16,0))
        topic_var = tk.StringVar()
        topic_dd = ttk.Combobox(self.content_frame, values=[], textvariable=topic_var, state="readonly", font=self.custom_font)
        topic_dd.grid(row=1, column=1, sticky="w", padx=8, pady=(16,0))
        code_label = tk.Label(self.content_frame, text="Code Example:", font=self.topic_font, bg="#e0f2fe")
        code_label.grid(row=2, column=0,sticky="nw", pady=(20,0))
        code_box = scrolledtext.ScrolledText(self.content_frame, font=("Fira Mono", 16), height=8, width=70, bg="#f0f9ff", fg="#2d3748")
        code_box.grid(row=2, column=1, sticky="w", pady=(18,0))
        code_box.config(state="disabled")
        expl_label = tk.Label(self.content_frame, text="Explanation:", font=self.topic_font, bg="#e0f2fe")
        expl_label.grid(row=3, column=0,sticky="nw", pady=(10,0))
        expl_box = tk.Label(self.content_frame, text="", font=self.custom_font, bg="#f0f9ff", fg="#334155", wraplength=700, justify="left")
        expl_box.grid(row=3, column=1, sticky="w", pady=(10,0))

        def update_topics(*_):
            lang = lang_var.get()
            topics = list(LANG_SYNTAX.get(lang, {}).keys())
            topic_dd['values'] = topics
            if topics:
                topic_var.set(topics[0])
                update_code()
        def update_code(*_):
            lang = lang_var.get()
            topic = topic_var.get()
            data = LANG_SYNTAX.get(lang, {}).get(topic)
            code_box.config(state="normal")
            code_box.delete(1.0, tk.END)
            expl_box.config(text="")
            if data:
                code_box.insert(tk.END, data['syntax'])
                expl_box.config(text=data['explanation'])
            else:
                code_box.insert(tk.END, "No code for this topic.")
            code_box.config(state="disabled")
        lang_dd.bind("<<ComboboxSelected>>", update_topics)
        topic_dd.bind("<<ComboboxSelected>>", update_code)
        update_topics()

    # Tab 2: Code Snippet Generator (same as syntax, but big list + copy button)
    def code_snippet_tab(self):
        tk.Label(self.content_frame, text="Select Language:", font=self.topic_font, bg="#e0f2fe").grid(row=0,column=0,sticky="w")
        lang_var = tk.StringVar(value="Python")
        langs = list(LANG_SYNTAX.keys())
        lang_dd = ttk.Combobox(self.content_frame, values=langs, textvariable=lang_var, state="readonly", font=self.custom_font)
        lang_dd.grid(row=0, column=1, sticky="w", padx=8)

        topics_label = tk.Label(self.content_frame, text="Select Snippet:", font=self.topic_font, bg="#e0f2fe")
        topics_label.grid(row=1, column=0,sticky="w", pady=(16,0))
        topic_var = tk.StringVar()
        topic_dd = ttk.Combobox(self.content_frame, values=[], textvariable=topic_var, state="readonly", font=self.custom_font)
        topic_dd.grid(row=1, column=1, sticky="w", padx=8, pady=(16,0))

        code_box = scrolledtext.ScrolledText(self.content_frame, font=("Fira Mono", 16), height=10, width=70, bg="#fefce8", fg="#2d3748")
        code_box.grid(row=2, column=0, columnspan=2, sticky="w", pady=(20,0))
        code_box.config(state="disabled")
        copy_btn = tk.Button(self.content_frame, text="📋 Copy to Clipboard", font=self.topic_font, bg="#2563eb", fg="white", command=lambda: self.clipboard_copy(code_box.get(1.0, tk.END)))
        copy_btn.grid(row=3, column=1, sticky="e", pady=12)

        def update_topics(*_):
            lang = lang_var.get()
            topics = list(LANG_SYNTAX.get(lang, {}).keys())
            topic_dd['values'] = topics
            if topics:
                topic_var.set(topics[0])
                update_code()
        def update_code(*_):
            lang = lang_var.get()
            topic = topic_var.get()
            data = LANG_SYNTAX.get(lang, {}).get(topic)
            code_box.config(state="normal")
            code_box.delete(1.0, tk.END)
            if data:
                code_box.insert(tk.END, data['syntax'])
            else:
                code_box.insert(tk.END, "No snippet for this topic.")
            code_box.config(state="disabled")
        lang_dd.bind("<<ComboboxSelected>>", update_topics)
        topic_dd.bind("<<ComboboxSelected>>", update_code)
        update_topics()

    # Tab 3: Keyword/Command Lookup
    def keyword_lookup_tab(self):
        tk.Label(self.content_frame, text="Select Language:", font=self.topic_font, bg="#e0f2fe").grid(row=0,column=0,sticky="w")
        lang_var = tk.StringVar(value="Python")
        langs = list(KEYWORD_LOOKUP.keys())
        lang_dd = ttk.Combobox(self.content_frame, values=langs, textvariable=lang_var, state="readonly", font=self.custom_font)
        lang_dd.grid(row=0, column=1, sticky="w", padx=8)

        tk.Label(self.content_frame, text="Enter keyword/command:", font=self.topic_font, bg="#e0f2fe").grid(row=1, column=0, sticky="w", pady=(16,0))
        kw_var = tk.StringVar()
        kw_entry = tk.Entry(self.content_frame, textvariable=kw_var, font=self.custom_font, width=22)
        kw_entry.grid(row=1, column=1, sticky="w", padx=8, pady=(16,0))

        usage_lbl = tk.Label(self.content_frame, text="", font=self.custom_font, bg="#f0f9ff", fg="#334155", wraplength=700, justify="left")
        usage_lbl.grid(row=2, column=0, columnspan=2, sticky="w", pady=(20,0))
        sample_box = scrolledtext.ScrolledText(self.content_frame, font=("Fira Mono", 16), height=5, width=65, bg="#f0f9ff", fg="#2d3748")
        sample_box.grid(row=3, column=0, columnspan=2, sticky="w", pady=(14,0))
        sample_box.config(state="disabled")

        def lookup(*_):
            lang = lang_var.get()
            kw = kw_var.get().strip()
            usage_lbl.config(text="")
            sample_box.config(state="normal")
            sample_box.delete(1.0, tk.END)
            found = False
            if kw:
                for k, v in KEYWORD_LOOKUP.get(lang, {}).items():
                    if kw.lower() == k.lower():
                        usage_lbl.config(text=f"{k}: {v['usage']}")
                        sample_box.insert(tk.END, v['sample'])
                        found = True
                        break
            if not found:
                usage_lbl.config(text="No info found for this keyword in selected language.")
            sample_box.config(state="disabled")
        kw_entry.bind("<Return>", lookup)
        tk.Button(self.content_frame, text="Search", font=self.topic_font, bg="#2563eb", fg="white", command=lookup).grid(row=1, column=2, padx=8, pady=(16,0))

    # Tab 4: Error Explanations
    def error_explanations_tab(self):
        tk.Label(self.content_frame, text="Select Language:", font=self.topic_font, bg="#e0f2fe").grid(row=0,column=0,sticky="w")
        lang_var = tk.StringVar(value="Python")
        langs = list(ERROR_EXPLAIN.keys())
        lang_dd = ttk.Combobox(self.content_frame, values=langs, textvariable=lang_var, state="readonly", font=self.custom_font)
        lang_dd.grid(row=0, column=1, sticky="w", padx=8)
        tk.Label(self.content_frame, text="Select Error/Message:", font=self.topic_font, bg="#e0f2fe").grid(row=1, column=0, sticky="w", pady=(16,0))
        err_var = tk.StringVar()
        err_dd = ttk.Combobox(self.content_frame, values=[], textvariable=err_var, state="readonly", font=self.custom_font)
        err_dd.grid(row=1, column=1, sticky="w", padx=8, pady=(16,0))
        expl_lbl = tk.Label(self.content_frame, text="", font=self.custom_font, bg="#f0f9ff", fg="#334155", wraplength=700, justify="left")
        expl_lbl.grid(row=2, column=0, columnspan=2, sticky="w", pady=(20,0))

        def update_errs(*_):
            lang = lang_var.get()
            errs = list(ERROR_EXPLAIN.get(lang, {}).keys())
            err_dd['values'] = errs
            if errs:
                err_var.set(errs[0])
                update_expl()
        def update_expl(*_):
            lang = lang_var.get()
            err = err_var.get()
            expl = ERROR_EXPLAIN.get(lang, {}).get(err, "No explanation available.")
            expl_lbl.config(text=expl)
        lang_dd.bind("<<ComboboxSelected>>", update_errs)
        err_dd.bind("<<ComboboxSelected>>", update_expl)
        update_errs()

    def clipboard_copy(self, text):
        self.clipboard_clear()
        self.clipboard_append(text)
        self.update() # Now it stays on clipboard after window is closed
def show_language_tool(self):
    LanguageToolWindow(self)
EduMatrixApp.show_language_tool = show_language_tool

if __name__ == "__main__":
    app = EduMatrixApp()
    app.mainloop()