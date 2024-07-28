# Quiz Application

This is a Python-based quiz application that selects 10 random questions from a set of CSV files and calculates the score based on the user's answers.

## Features

- Loads questions from multiple CSV files.
- Randomly selects 10 questions for each quiz session.
- Compares user answers with the correct answers and calculates the score.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/quiz-application.git
    cd quiz-application
    ```

2. **Install required packages:**
    Make sure you have `pandas` installed. You can install it using pip:
    ```sh
    pip install pandas
    ```

## Usage

1. **Prepare your CSV files:**
    Ensure your CSV files are structured with the following columns: `question` and `answer`. For example:
    ```csv
    question,answer
    What is the capital of France?,Paris
    Who wrote "1984"?,George Orwell
    ```

2. **Modify the `filenames` list:**
    In the `main()` function, update the `filenames` list with the paths to your CSV files:
    ```python
    filenames = [r"path\to\your\first_file.csv", r"path\to\your\second_file.csv"]
    ```

3. **Run the application:**
    Execute the script using Python:
    ```sh
    python quiz_application.py
    ```

4. **Answer the questions:**
    The script will display 10 random questions and prompt you to input your answers. At the end of the quiz, your score will be displayed.

## Example

Here is an example of running the quiz application:

```sh
Question 1: What is the capital of France?
Your answer: Paris
Question 2: Who wrote "1984"?
Your answer: George Orwell
...
Your score: 8/10
```

## Dependencies

- pandas

Ensure you have `pandas` installed in your Python environment.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/om-mishra-a62991289).
