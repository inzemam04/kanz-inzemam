
# Screening API

This project implements a REST API that accepts a number as input and returns a list of strings based on certain rules.

## Functionality

- If the number is divisible by 3, the API returns "Kanz".
- If the number is divisible by 5, the API returns "Way".
- If the number is divisible by both 3 and 5, the API returns "KanzWay".
- For all other numbers, the API returns the number itself.

## Project Structure
```
screening-api/
├── app.py          # Main application file
├── test_app.py     # Unit tests for the application
└── README.md       # Project documentation
```

## Requirements
- Python 3.x
- Flask (Install using `pip install flask`)

## How to Run the Project

1. **Install Flask**:
   ```
   pip install flask
   ```

2. **Start the server**:
   ```
   python app.py
   ```
   
3. **Access the endpoint**:
   ```
   http://localhost:5000/api/v1/screening/<number>
   ```
   Replace `<number>` with any integer to test.

## How to Run the Tests

1. Run the following command:
   ```
   python -m unittest test_app.py
   ```
This will execute all the test cases to verify the functionality of the API.

## Additional Notes
- Ensure that you have Python installed and properly set up on your system.
- The API runs locally on `http://127.0.0.1:5000`.
