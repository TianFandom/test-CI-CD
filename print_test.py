def test_print_function():
    from datetime import datetime
    
    # Get the current timestamp
    current_timestamp = datetime.now()
    
    # Print the current timestamp
    print(current_timestamp)
    
    # Append the current timestamp to a .txt file in the same folder
    with open("current_timestamp.txt", "a") as file:
        file.write(str(current_timestamp) + '\n')
    return True
