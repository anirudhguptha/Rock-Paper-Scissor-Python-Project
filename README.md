# Rock-Paper-Scissors Game 🎮

## 📌 Logic of the Program
1. Import the `random` module to allow the computer to pick a random choice.
2. Create a list `item_list = ["Rock", "Paper", "Scissor"]` containing the three possible moves.
3. Take user input (`Rock`, `Paper`, or `Scissor`) and store it in `user_choice`.
4. Let the computer randomly select one option from `item_list` and store it in `comp_choice`.
5. Print both choices (user and computer).
6. Compare both choices:
   - If **both choices are the same** → it's a **Tie**.
   - If user picks **Rock**:
     - Rock vs Paper → **Computer Wins** (Paper covers Rock)
     - Rock vs Scissor → **User Wins** (Rock smashes Scissor)
   - If user picks **Paper**:
     - Paper vs Scissor → **Computer Wins** (Scissor cuts Paper)
     - Paper vs Rock → **User Wins** (Paper covers Rock)
   - If user picks **Scissor**:
     - Scissor vs Paper → **User Wins** (Scissor cuts Paper)
     - Scissor vs Rock → **Computer Wins** (Rock breaks Scissor)
7. Print the result accordingly.
