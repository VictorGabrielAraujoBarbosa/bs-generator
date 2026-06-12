import random
import time
import sys

VERBS = [
    "Bypassing", "Decrypting", "Initializing", "Overriding", 
    "Infiltrating", "Routing", "Compromising", "Injecting"
]

TARGETS = [
    "mainframe firewall", "core database", "NSA proxy server", 
    "quantum encryption matrix", "bios mainframe", "satellite uplink"
]

STATUSES = ["SUCCESS", "FAILED", "PENDING", "RETRYING"]

def generate_ip():
    """Generates a random, plausible-looking IPv4 address."""
    return f"{random.randint(11, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

def generate_loading_bar(percentage, length=20):
    """Generates a text-based ASCII loading bar."""
    # Clamp the percentage between 0 and 100
    percentage = max(0, min(100, percentage))
    length = max(0, min(20, length))
    
    filled_length = int(length * percentage // 100)
    bar = '█' * filled_length + '░' * (length - filled_length)
    
    return f"[{bar}] {percentage}%"

def generate_bs_line():
    """Randomly selects a type of hacker jargon line to print."""
    line_type = random.choice(["action", "connection", "progress"])
    
    if line_type == "connection":
        return f"Routing connection through {generate_ip()}... ESTABLISHED"
        
    elif line_type == "progress":
        verb = random.choice(VERBS)
        return f"{verb} {random.choice(TARGETS)}: {generate_loading_bar(random.randint(10, 99))}"
        
    else:
        verb = random.choice(VERBS)
        target = random.choice(TARGETS)
        status = random.choice(STATUSES)
        hex_addr = f"0x{random.randint(0x1000, 0xFFFF):X}"
        return f"[{hex_addr}] {verb} {target}... {status}"

def main(duration=5):
    """Runs the stream for a set duration (in seconds)."""
    print("--- INITIALIZING HACKERMAN PROTOCOL ---")
    start_time = time.time()
    
    while time.time() - start_time < duration:
        print(generate_bs_line())
        # Slightly faster sleep for a more frantic hacker feel
        time.sleep(0.15) 
        
    print("--- ACCESS GRANTED ---")

if __name__ == "__main__":
    run_duration = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    main(run_duration)