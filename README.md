# Create a README.md file
echo "# Coffee Machine Project" > README.md

# Open the file and edit it manually OR use this command to add content
echo "
# Coffee Machine Project

This is an Object-Oriented Programming (OOP) based coffee machine simulation in Python.  
It allows users to select coffee types, handles transactions, and manages ingredients.

## Features
- Supports multiple coffee types.
- Uses OOP principles with \`CoffeeMaker\`, \`MoneyMachine\`, and \`Menu\` classes.
- Handles transactions and resource management.

## How to Run
1. Clone this repository:
   \`\`\`
   git clone https://github.com/jasonberylmini/coffemachine_with_oop2.git
   cd coffemachine_with_oop2
   \`\`\`
2. Run the Python script:
   \`\`\`
   python main.py
   \`\`\`

## Author
**Jason Beryl**
" > README.md

# Add the README file to Git
git add README.md
git commit -m "Added README file"
git push origin main
