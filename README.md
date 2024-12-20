# Simple Password Manager

## Overview
The **Simple Password Manager** is a Python-based program designed to help users securely store and manage their credentials (username, password, and website/URL). It offers encryption for passwords to ensure security and provides an intuitive command-line interface for ease of use.

---

## Features
1. **Add New Credentials**: Securely save your username, password, and associated website/URL.
2. **View Stored Credentials**: Display all saved credentials in a neat table, with passwords decrypted for readability.
3. **Password Encryption and Decryption**: Ensures stored passwords are encrypted for security and decrypted when needed.
4. **Persistent Storage**: Credentials are saved to a local text file (`credentialstorage.txt`) for persistence between sessions.

---

## How It Works
### Encryption/Decryption
- **Encryption**: Passwords are encrypted using a simple Caesar cipher-like method, shifting each character by 3 positions in a defined character set.
- **Decryption**: Encrypted passwords are decrypted by reversing the shift, restoring the original password.

---

## Usage Instructions
### Prerequisites
- Python 3.x installed on your system.

### Running the Program
1. Clone or download the repository.
2. Navigate to the program directory and run the script using:
   ```bash
   python3 password_manager.py
   ```

### Program Menu
Upon running the program, you'll see the following menu:
```
[1] Enter 1 to Add New Credentials.
[2] Enter 2 to View Stored Credentials.
[e] Enter e to Exit the Program.
```

### Options
#### 1. Add New Credentials
- You’ll be prompted to enter the following:
  - **Username**: Your account username.
  - **Password**: Your account password (encrypted before storing).
  - **Website/URL**: The website or service associated with the credentials.
- The entered details are validated to ensure no empty fields.
- Once entered, the credentials are saved in the `credentialstorage.txt` file.

#### 2. View Stored Credentials
- Displays all saved credentials in a tabular format.
  - **Username**: Your stored username.
  - **Password**: Decrypted password for readability.
  - **Website/URL**: Associated website or service.
- If the storage file doesn’t exist or is empty, you’ll be notified.

#### e. Exit the Program
- Safely exits the program with a goodbye message.

---

## Example
### Adding Credentials
```
Welcome to the Simple Password Manager!
[1] Enter 1 to Add New Credentials.
[2] Enter 2 to View Stored Credentials.
[e] Enter e to Exit the Program.

Please enter your response here: 1

• You have chosen to Add New Credentials.

Please enter your username here: example_user
Please enter your password here: securepassword123
Please enter the website/URL here: example.com

• Your credentials have been stored.
```

### Viewing Credentials
```
Welcome to the Simple Password Manager!
[1] Enter 1 to Add New Credentials.
[2] Enter 2 to View Stored Credentials.
[e] Enter e to Exit the Program.

Please enter your response here: 2

• You have chosen to View Stored Credentials.

|     USERNAME      |      PASSWORD      |     WEBSITE/URL     |
|-------------------|--------------------|---------------------|
|  example_user     |  securepassword123 |   example.com       |

• All stored credentials have been displayed.
```

---

## File Details
- **`password_manager.py`**: Main program file containing the logic.
- **`credentialstorage.txt`**: Automatically created to store credentials securely.

---

## Limitations
- The encryption algorithm is basic and not suitable for highly sensitive data.
- Credentials are stored locally, so ensure the text file is not shared.

---

## Future Enhancements
- Implement stronger encryption (e.g., AES).
- Add a master password to access stored credentials.
- Enable search functionality for stored credentials.
- Create a graphical user interface (GUI).

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

---

## Contributions
Contributions, issues, and feature requests are welcome! Feel free to check out the [issues page](https://github.com/your_username/your_repo_name/issues) or submit a pull request.

---

## Contact
For any inquiries, reach out to:
- **Name**: Akira Crews-Low
- **Email**: akiraicrewslow@gmail.com

---

Thank you for using the Simple Password Manager! Stay secure! ❤️

