# CodeAlpha_Project_Hasan
Completed a remote Python Programming internship at CodeAlpha, developing a Stock Portfolio Tracker, an NLP-based chatbot, and automation scripts, gaining experience in API integration, natural language processing, and workflow optimization.


# Basic Chatbot Using NLTK and CSV-Based Responses

This chatbot is implemented using Python's NLTK library and pandas for dynamic, CSV-driven responses. It follows a rule-based approach using pre-defined patterns and responses stored in a CSV file.

How It Works:
  1. Loading Responses – The chatbot loads conversational patterns and responses from a CSV file using pandas. The dataset consists of user input patterns mapped to corresponding replies.
  2. Chatbot Initialization – The chatbot is built using NLTK’s Chat class, leveraging the loaded response pairs along with predefined reflections (e.g., handling pronoun swaps).
  3. User Interaction – The chatbot continuously takes user input, processes it using pattern matching, and returns the appropriate response.
  4. Exit Condition – The conversation runs in a loop until the user types "bye", at which point the chatbot terminates gracefully with a farewell message.

This implementation allows easy customization by modifying the responses.csv file, making it adaptable for different chatbot applications.

# File Oraganizer Script 

This Python script automatically organizes files in a specified directory by categorizing them into predefined folders based on their file types. It helps keep directories clean and structured by moving files into appropriate subfolders.

How It Works:
  1. File Categorization – The script classifies files into categories such as Documents, Images, Videos, Audio, Archives, Executables, and Others, based on their extensions.
  2. Directory Scanning – It scans the target folder (TARGET_FOLDER) for all files while ignoring subdirectories.
  3. Sorting and Moving – Each file is moved into its respective category folder, which is created if it does not already exist.
  4. Logging – After organizing, the script displays a summary of how many files were moved and their new locations.

You can modify the FILE_CATEGORIES dictionary to add or remove file types based on your needs.
Supports easy expansion for additional file formats and categories.
