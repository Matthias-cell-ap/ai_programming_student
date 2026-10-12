"""
Oefening 2: Floor Cleaning Agent (Model-based Reflex Agent)
=============================================================
Implementeer een model-based reflex agent voor een robotstofzuiger.
Volg het stappenplan in opgave_week1.md.
"""


class FloorCleaningAgent:
    """
    Een model-based reflex agent die een kamer proper maakt.

    De kamer is een grid van `rows` × `cols` tegels.
    De robot start in de linkerbovenhoek (rij 0, kolom 0).
    """

    def __init__(self, rows=5, cols=10):
        """
        Initialiseer de robot met een lege kamer van `rows` × `cols`.

        Tip: gebruik een 2D-lijst om de status van elke tegel bij te houden.
        """
        self.rows = rows
        self.cols = cols

        # TODO: interne state initialiseren
        # - huidige positie (rij, kolom)
        # - grid met proper/vuil status per tegel (bv. True = proper, False = vuil)

        self.row = 0  # startrij (bovenaan)
        self.col = 0  # startkolom (links)

        self.grid = [[False for _ in range(cols)] for _ in range(rows)]

    # ---------- Basisbewegingen ----------

    def move_up(self):
        """Verplaats de robot één tegel omhoog (rij -1)."""
        if self.row > 0:
            self.row -= 1
            print(f"Verplaats naar ({self.row}, {self.col})")
        else:
            print("Kan niet omhoog: rand bereikt")

    def move_down(self):
        """Verplaats de robot één tegel omlaag (rij +1)."""
        if self.row < self.rows - 1:
            self.row += 1
            print(f"Verplaats naar ({self.row}, {self.col})")
        else:
            print("Kan niet omlaag: rand bereikt")

    def move_left(self):
        """Verplaats de robot één tegel naar links (kolom -1)."""
        if self.col > 0:
            self.col -= 1
            print(f"Verplaats naar ({self.row}, {self.col})")
        else:
            print("Kan niet naar links: rand bereikt")

    def move_right(self):
        """Verplaats de robot één tegel naar rechts (kolom +1)."""
        if self.col < self.cols - 1:
            self.col += 1
            print(f"Verplaats naar ({self.row}, {self.col})")
        else:
            print("Kan niet naar rechts: rand bereikt")

    # ---------- Stofzuigen ----------

    def clean_tile(self):
        """Stofzuig de huidige tegel (maak hem proper)."""
        self.grid[self.row][self.col] = True
        print(f"Tegel ({self.row}, {self.col}) is nu proper!")

    # ---------- Strategie ----------

    def clean_room(self):
        """
        Laat de robot de volledige kamer proper maken.
        Gebruik een systematische strategie (bv. zigzag-patroon).
        """
        # TODO: implementeer een strategie
        for i in range(self.rows):
            if self.col == 0:
                for j in range(self.cols):
                    self.move_to(i, j)
                    self.clean_tile()
            else:
                for j in range(self.cols):
                    self.move_to(i, self.cols - 1-j)
                    self.clean_tile()

    # ---------- Helper om naar een specifieke tegel te gaan ----------

    def move_to(self, target_row, target_col):
        """
        Verplaats de robot van huidige positie naar (target_row, target_col).
        Gebruik de basisbewegingen move_up/down/left/right.
        """
        # TODO: implementeer
        if target_row > self.row:
            while target_row != self.row:
                self.move_down()
        elif target_row < self.row:
            while target_row != self.row:
                self.move_up()

        if target_col > self.col:
            while target_col != self.col:
                self.move_right()
        elif target_col < self.col:
            while target_col != self.col:
                self.move_left()

    # ---------- Weergave ----------

    def print_status(self):
        """Toon de huidige status van de kamer."""
        print("\nKamer status (V = vuil, P = proper, R = robot):")
        for r in range(self.rows):
            rij_str = ""
            for c in range(self.cols):
                if r == self.row and c == self.col:
                    rij_str += " R "
                else:
                    if self.grid[r][c] == False:
                        rij_str += " V "
                    else:
                        rij_str += " P "
            print(rij_str)
        print()


if __name__ == "__main__":
    # Test je agent
    robot = FloorCleaningAgent()

    print("Beginstatus:")
    robot.print_status()

    robot.clean_room()

    print("Eindstatus:")
    robot.print_status()