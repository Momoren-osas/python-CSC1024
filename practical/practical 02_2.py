# Prompt the user to enter elapsed time in seconds
elapsed_seconds = int(input("Enter elapsed time in seconds: "))

# Calculate hours, minutes, and seconds
hours = elapsed_seconds // 3600
minutes = (elapsed_seconds % 3600) // 60
seconds = elapsed_seconds % 60

# Format and display the result as HH:MM:SS
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")