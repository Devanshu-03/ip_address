## Setting up the Python Environment

1. **Create directories:**
   - Create a directory named `env` and navigate into it.
     ```bash
     mkdir env
     cd env
     ```

2. **Create a virtual environment:**
   - Inside the `env` directory, create another directory named `venv`.
     ```bash
     mkdir venv
     ```

3. **Initialize the virtual environment:**
   - Run the following command to create a virtual environment named `venv` using Python's `venv` module.
     ```bash
     python -m venv venv
     ```

4. **Activate the virtual environment (Git Terminal in VS Code):**
   - If you're using a Git terminal in VS Code (Windows):
     ```bash
     source env/venv/Scripts/activate
     ```

5. **Activate the virtual environment (Windows Command Prompt):**
   - For Windows Command Prompt:
     ```bash
     env\venv\Scripts\activate
     ```

6. **Activate the virtual environment (Mac/Linux):**
   - For macOS or Linux:
     ```bash
     source env/venv/bin/activate
     ```

7. **Install requirements:**
   - Finally, install the Python packages listed in `requirements.txt` into your virtual environment using pip.
     ```bash
     pip install -r requirements.txt
     ```
