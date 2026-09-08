from levels.level_5_story import INTRO, TRUTH_REVEAL, FINAL_CHOICE
from levels import level_5_endings as endings


class HeartOfDungeon:
    """Handles Level 5: The Heart of the Dungeon."""

    def __init__(self, game_state=None):
        self.game_state = game_state

    def play(self):
        """Run Level 5."""
        self.show_intro()
        self.reveal_truth()

        choice = self.get_final_choice()
        self.determine_ending(choice)

    def show_intro(self):
        print("\n" + "=" * 55)
        print("          LEVEL 5 — THE HEART OF THE DUNGEON")
        print("=" * 55)
        print(INTRO)

    def reveal_truth(self):
        print("\n" + "-" * 55)
        print("                     THE TRUTH")
        print("-" * 55)
        print(TRUTH_REVEAL)

    def get_final_choice(self):
        print("\n" + "=" * 55)
        print("                  FINAL CHOICE")
        print("=" * 55)

        print(FINAL_CHOICE)

        while True:
            choice = input("Choose 1, 2, or 3: ").strip()

            if choice in ("1", "2", "3"):
                return choice

            print("Invalid choice. Please enter 1, 2, or 3.")

    def get_heart_gem_value(self):
        """Read Elara's Heart Gem value."""

        if self.game_state is None:
            return 50

        if isinstance(self.game_state, dict):
            return self.game_state.get("heart_gem", 50)

        heart_gem = getattr(self.game_state, "heart_gem", 50)

        if hasattr(heart_gem, "value"):
            return heart_gem.value

        return heart_gem

    def remembers(self, memory):
        """Check whether an important event happened earlier."""

        if self.game_state is None:
            return False

        if isinstance(self.game_state, dict):
            memories = self.game_state.get("memories", [])
            return memory in memories

        if hasattr(self.game_state, "remembers"):
            return self.game_state.remembers(memory)

        return False

    def determine_ending(self, choice):
        """Determine the ending from Elara's choices and state."""

        heart_gem = self.get_heart_gem_value()

        if heart_gem <= 0:
            endings.loop()
            return

        if choice == "1":
            endings.runaway()

        elif choice == "2":
            endings.unmaking()

        elif choice == "3":
            if self.remembers("discovered_truth"):
                endings.new_law()
            else:
                endings.loop()


if __name__ == "__main__":
    test_state = {
        "heart_gem": 70,
        "memories": ["discovered_truth"]
    }

    level_five = HeartOfDungeon(test_state)
    level_five.play()