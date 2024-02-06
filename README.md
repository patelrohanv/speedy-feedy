# Getting Started

This section will guide you through the installation of Python on a Mac.

## Installing Python on Mac with Homebrew

1. Open Terminal.

2. Check if Python is already installed by typing `python --version` or `python3 --version`. If Python is installed, the terminal will display the version number. If not, proceed to the next step.

3. Install Homebrew, a package manager for Mac, by pasting the following command in the Terminal: 

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

4. Once Homebrew is installed, install Python by typing the following command in the Terminal:

    ```bash
    brew install python
    ```

5. After the installation is complete, verify it by typing `python3 --version` in the Terminal. It should display the version of Python you just installed.

Now you have Python installed on your Mac and you're ready to start coding!

## Setting Up a Virtual Environment

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated Python environments for them. This is one of the most important tools that most Python developers use.

### Creating a Virtual Environment

1. Navigate to the project directory in the Terminal.

2. Create a virtual environment named `venv` by running:

    ```bash
    python3 -m venv venv
    ```

### Activating the Virtual Environment

1. Activate the virtual environment by running:

    ```bash
    source venv/bin/activate
    ```

    Your shell prompt will change to show the name of the activated environment.

### Installing Requirements

1. If you have a `requirements.txt` file, you can install all the dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

    This will download and install all the packages listed in `requirements.txt`.

Remember to always activate your virtual environment before you start working on your project, and deactivate it when you're done.

To deactivate the virtual environment and return to your normal shell, simply run:

```bash
deactivate
```

## Running the Application Development Server

After setting up and activating the virtual environment, you can run the Django application.

1. Ensure that your virtual environment is activated.

2. Navigate to the `app` directory where your Django project is located:

    ```bash
    cd app
    ```

3. Run the Django server with the following command:

    ```bash
    python manage.py runserver
    ```

    This will start the Django development server. You should see output indicating that the server is running, along with the address where it is listening. It's usually `http://127.0.0.1:8000/`.

4. Open your web browser and enter the address of your local server (usually `http://127.0.0.1:8000/`) to view your application.


## Database Migrations and Running Commands

Django uses a migration system to handle changes to your models and the corresponding database schema. Here's how to create and apply migrations.

### Running Migrations

1. Ensure that your virtual environment is activated and you are in the `app` directory.

2. To create new migrations based on the changes you've made to your models, run:

    ```bash
    python manage.py makemigrations
    ```

3. To apply and unapply migrations, run:

    ```bash
    python manage.py migrate
    ```

### Running Commands in Specific Applications

If you want to run commands specific to the `employees` or `feedback` applications, you can do so by specifying the application name before the command.

For example, to run a command in the `employees` application, use:

```bash
python manage.py employees <command>
```
And for the feedback application, use:
```bash
python manage.py feedback <command>
```
Replace <command> with the specific command you want to run.

## Running Scripts

This project includes two scripts that help with development: `run_dev.sh` and `seed_dev.sh`.

### Ensure the Scripts Can Execute

2. Make the script executable by running:

    ```bash
    chmod +x <script_name.sh>
    ```

### Seeding the Development Database

The `seed_dev.sh` script seeds the development database with initial data. To run this script:

1. Ensure that your virtual environment is activated and you are in the project root directory.

2. Make the script executable


3. Run the script:

    ```bash
    ./seed_dev.sh
    ```
    
### Running the Development Server

The `run_dev.sh` script starts the development server. To run this script:

1. Ensure that your virtual environment is activated and you are in the project root directory.

2. Make the script executable

3. Run the script:

    ```bash
    ./run_dev.sh
    ```
