class validater:
    def __init__(self):
        self.function = None

    def yes_or_no_input(self, question):
        choice = input(f'{question} [Y/N]: ').upper()
        if choice == "N":
            self.correct_input = False
        elif choice == "Y":
            self.correct_input = False

        else:
            print("That is not a valid answer. Please type 'Y' or 'N': ")
            print()
            self.correct_input = True
        
        return choice
            

    def higher_lower_input(self, question):
        choice = input(f'{question} [H/L]:').upper()
        if choice == "H":
            self.correct_input = False
        elif choice == "L":
            self.correct_input = False
        else:
            print("That is not a valid answer. Please type 'H' or 'L': ")
            print()
            self.correct_input = True

        return choice

    def validate_input(self, prompt_question, inputWanted):
        self.correct_input = True
        while self.correct_input:
            if inputWanted == "H/L":
                answer = self.higher_lower_input(prompt_question)
            elif inputWanted == "Y/N":
                answer = self.yes_or_no_input(prompt_question)
            else:
                print('<That input type is not supported>')
        
        return answer