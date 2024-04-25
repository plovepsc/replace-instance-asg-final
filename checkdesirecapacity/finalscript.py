
import subprocess
import time

def run_command(command):
    # Execute the command using subprocess
    subprocess.run(command, shell=True)

# List of commands to execute sequentially
commands = [
    "cd /home/ubuntus/terarom/finalasgcapcity/checkdesirecapacity && python3 script1.py",
    "cd /home/ubuntus/terarom/finalasgcapcity/checkdesirecapacity && python3 script2.py"
]

# Loop through the list of commands and execute them sequentially
for command in commands:
    print(f"Executing command: {command}")
    run_command(command)

    # Introduce a delay (sleep) after each command except the last one
    if command != commands[-1]:
        delay_seconds = 120  # Adjust the delay duration as needed (5 seconds in this example)
        print(f"Sleeping for {delay_seconds} seconds before the next command...")
        time.sleep(delay_seconds)

print("All commands have been executed.")
