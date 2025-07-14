import hashlib
import time

MAX_ATTEMPTS = 3
WAIT_TIMES = [10, 60, 300, 1800]  # Wait times in seconds: 10s, 1min, 5min, 30min

def hash_password(password: str) -> str:
    """Hash a password using SHA-256 and return the hexadecimal result."""
    return hashlib.sha256(password.encode()).hexdigest()

protected_password = "my1sec@ure%pass&word"
protected_hash = hash_password(protected_password)

print("Protected hash:", protected_hash)

attempts = 0
block_level = 0

while True:
    if attempts >= MAX_ATTEMPTS:
        wait_time = WAIT_TIMES[min(block_level, len(WAIT_TIMES) - 1)]
        print(f"Too many failed tries. Waiting {wait_time}s...")
        time.sleep(wait_time)
        block_level += 1  # Increment block level for the next potential block
        attempts = 0      # Reset attempts after waiting
        print("You can try again now.")

    user_input = input("Enter password to login: ")
    user_hash = hash_password(user_input)

    if user_hash == protected_hash:
        print("Login successful! Welcome aboard.")
        break
    else:
        attempts += 1
        print(f"Wrong password. Attempts: {attempts}/{MAX_ATTEMPTS}")
