import time
import difflib

def calculate_typing_speed(text, time_taken):
    words = text.split()
    num_words = len(words)
    typing_speed = (num_words / time_taken) * 60  # Words per minute
    return typing_speed

def calculate_error_rate(original_text, typed_text):
    matcher = difflib.SequenceMatcher(None, original_text, typed_text)
    total_errors = sum(len(typed_text) - match.size for match in matcher.get_matching_blocks())
    error_rate = (total_errors / len(original_text)) * 100  # Error rate in percentage
    return error_rate

def main():
    prompt_text = "The quick brown fox jumps over the lazy dog."
    
    input("Press Enter to start typing...")
    start_time = time.time()
    
    typed_text = input(prompt_text + "\n")
    
    end_time = time.time()
    time_taken = end_time - start_time
    
    typing_speed = calculate_typing_speed(typed_text, time_taken)
    error_rate = calculate_error_rate(prompt_text, typed_text)
    
    print(f"Your typing speed: {typing_speed:.2f} words per minute")
    print(f"Error rate: {error_rate:.2f}%")

if __name__ == "__main__":
    main()
