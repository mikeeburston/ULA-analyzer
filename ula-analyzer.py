import tkinter as tk
from tkinter import scrolledtext
import re

# Dictionary of bad practices with patterns and descriptions
bad_practices = {
    "forced arbitration": {
        "pattern": r"(arbitration|binding arbitration|waiver of right to sue|resolve disputes through arbitration)",
        "description": "Forces disputes to be resolved through arbitration instead of courts, limiting legal options."
    },
    "limitation of liability": {
        "pattern": r"(limitation of liability|we are not responsible|no liability even in negligence|exclude.*our liability)",
        "description": "Limits the company’s liability for damages, even if the company was negligent."
    },
    "unilateral amendments": {
        "pattern": r"(we may change these terms at any time|modify.*without notice|unilateral change to terms)",
        "description": "Allows the company to modify the agreement without notifying or gaining consent from the user."
    },
    "data sharing with third parties": {
        "pattern": r"(share.*data with third parties|sell.*data to third parties|data.*shared with partners)",
        "description": "The company reserves the right to share or sell your data with third parties without explicit consent."
    },
    "no right to opt-out of data collection": {
        "pattern": r"(cannot opt out|mandatory data collection|no choice to stop data collection)",
        "description": "Prevents the user from opting out of data collection, infringing on privacy."
    },
    "broad license to user content": {
        "pattern": r"(perpetual license|grant.*irrevocable license|we may use your content.*without further consent)",
        "description": "Grants the company a broad license to use, modify, or sell your content, often without compensation."
    },
    "no refunds": {
        "pattern": r"(no refunds|non-refundable|refunds are not available under any circumstances)",
        "description": "The company does not allow any refunds, even if the service is faulty or unsatisfactory."
    },
    "indemnity clauses": {
        "pattern": r"(indemnify|hold harmless|you will be responsible for legal fees|you agree to pay our legal costs)",
        "description": "The user agrees to cover the company's legal fees or damages in certain cases, even if they are not at fault."
    },
    "tracking and behavioral profiling": {
        "pattern": r"(track.*behavior|behavioral profiling|data collected for targeted advertising)",
        "description": "Allows the company to collect data for tracking and behavioral profiling, often for advertising purposes."
    }
}

# Function to search for bad practices
def search_bad_practices(ula_text, bad_practices):
    found_issues = []
    for practice, details in bad_practices.items():
        pattern = details["pattern"]
        if re.search(pattern, ula_text, re.IGNORECASE):
            found_issues.append({
                "practice": practice,
                "description": details["description"]
            })
    return found_issues

# Function to display results with ratings
def display_results(issues):
    result_text.delete(1.0, tk.END)
    
    # Display bad Practices
    if issues:
        result_text.insert(tk.END, "Bad Practice Found:\n\n")
        for issue in issues:
            result_text.insert(tk.END, f"- {issue['practice'].capitalize()}:\n  {issue['description']}\n\n")
    else:
        result_text.insert(tk.END, "No shady practices found.\n\n")

    # Calculate and display rating
    rating = calculate_rating(len(issues))
    result_text.insert(tk.END, f"Company Rating: {rating} stars\n")

# Function to calculate rating based on number of bad practices
def calculate_rating(bad_practices_count):
    if bad_practices_count == 0:
        return 5 # Company may not be shady
    elif 1 <= bad_practices_count <= 2:
        return 4 # Company is slightly shady
    elif 3 <= bad_practices_count <= 4:
        return 3 # Company is shady
    elif 5 <= bad_practices_count <= 6:
        return 2 # Company may think you are the product.
    else:
        return 1 # What the company is selling you is not worth it 

# Function to analyze ULA text
def analyze_ula():
    ula_text = ula_input.get(1.0, tk.END)
    issues = search_bad_practices(ula_text, bad_practices)
    display_results(issues)

# Setting up the main GUI window
root = tk.Tk()
root.title("ULA Analyzer")

# Input section for ULA
tk.Label(root, text="Paste the ULA here:").pack(pady=10)
ula_input = scrolledtext.ScrolledText(root, width=80, height=20)
ula_input.pack(padx=10, pady=10)

# Analyze button
analyze_button = tk.Button(root, text="Analyze ULA", command=analyze_ula)
analyze_button.pack(pady=10)

# Output section for results
tk.Label(root, text="Results:").pack(pady=10)
result_text = scrolledtext.ScrolledText(root, width=80, height=20)
result_text.pack(padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()