"""
Oefening 3: Routeplanner (Utility-based Agent)
===============================================
Een utility-based agent maximaliseert een interne utility-functie.

Voor de route Antwerpen -> Parijs is een interessante utility:
    utility = -d(huidige stad, nieuwe stad)

De agent zoekt NIET (dit doen we in week 3): bij elke stap kiest hij greedy de
buur met de hoogste utility (kleinste afstand).
"""
from typing import Optional

CITIES = ["Antwerpen", "Brussel", "Gent", "Luik", "Doornik", "Reims", "Parijs"]

# Afstandsmatrix (onvolledig): wie met wie is er een weg?
ROADS: dict[tuple[str, str], float] = {
    ("Antwerpen", "Brussel"): 45,
    ("Antwerpen", "Gent"): 60,
    ("Brussel", "Luik"): 100,
    ("Brussel", "Gent"): 55,
    ("Brussel", "Doornik"): 90,
    ("Gent", "Doornik"): 65,
    ("Doornik", "Reims"): 130,
    ("Luik", "Reims"): 110,
    ("Reims", "Parijs"): 145,
    ("Gent", "Parijs"): 300,
}


def distance(a: str, b: str) -> Optional[float]:
    """Geef de afstand tussen twee steden, of None zonder weg."""
    if (a, b) in ROADS:
        return ROADS[(a, b)]
    if (b, a) in ROADS:
        return ROADS[(b, a)]
    return None


class RouteAgent:
    """Utility-based agent: kiest bij elke stap de dichtstbijzijnde buur."""

    def utility(self, from_city: str, to_city: str) -> float:
        """TODO: geef -d(from_city, to_city) terug."""
        dist = distance(from_city, to_city)
        if dist != None:
            return 0 - dist
        return dist

    def neighbours(self, city: str) -> list[str]:
        """TODO: geef alle steden met een directe weg naar `city`."""
        neighbours = [ab for ab in CITIES if distance(city, ab) != None] 
        return neighbours

    def choose_next(self, current_city: str, visited: set[str]) -> Optional[str]:
        """TODO: kies onder de niet-bezochte buren de buur met de
        hoogste utility. Geen buren meer? -> None.
        """
        valid = [b for b in self.neighbours(current_city) if b not in visited]
        if len(valid) > 0:
            return max(valid, key=lambda to_city: self.utility(current_city, to_city))
        return None

    """def plan_route(self, start_city: str, goal_city: str) -> list[str]:
        ""TODO: bouw de route stad per stad via choose_next.
        Stop zodra de goal bereikt is of de agent vastzit.
        ""
        current = start_city
        route = [current]
        visited = {current}

        while current != goal_city:
            next_city = self.choose_next(current, visited)

            if next_city is None:
                break

            route.append(next_city)
            visited.add(next_city)
            current = next_city

        return route"""
    
    def plan_route(self,start_city: str,goal_city: str,history: Optional[list[str]] = None,visited: Optional[set[str]] = None,) -> list[str]:

        if history is None:
            history = [start_city]
        if visited is None:
            visited = {start_city}

        current = start_city

        if distance(current, goal_city) is not None:
            history.append(goal_city)
            return history

        while True:
            next_city = self.choose_next(current, visited)

            if next_city is None:
                return None

            visited.add(next_city)
            history.append(next_city)

            result = self.plan_route(next_city, goal_city, history, visited)

            if result is not None:
                return result

            history.pop()


if __name__ == "__main__":
    agent = RouteAgent()
    route = agent.plan_route("Antwerpen", "Parijs")
    print("Route:", " -> ".join(route))

    totale_afstand = 0.0
    for a, b in zip(route, route[1:]):
        d = distance(a, b)
        if d is not None:
            totale_afstand += d
    print("Totale afstand:", totale_afstand, "km")

    # Vergelijk met wat we gaan doen in week 3: wat is de kortste route met de hand? (week 3: Dijkstra!)
