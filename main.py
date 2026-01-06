import sys

def run_app():
    print("--- Welcome to the Portable App ---")
    user_input = input("Enter a message to save: ")
    
    with open("output.txt", "w") as f:
        f.write(f"User said: {user_input}")
    
    print("Success! Your message was saved to output.txt.")

if __name__ == "__main__":
    run_app()