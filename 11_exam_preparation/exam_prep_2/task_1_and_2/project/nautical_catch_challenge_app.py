from ex_1_and_2.project import FreeDiver
from ex_1_and_2.project import ScubaDiver
from ex_1_and_2.project import DeepSeaFish
from ex_1_and_2.project import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPES = {
        'FreeDiver': FreeDiver,
        'ScubaDiver': ScubaDiver
    }
    VALID_FISH_TYPES = {
        'PredatoryFish': PredatoryFish,
        'DeepSeaFish': DeepSeaFish
    }

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        try:
            diver = self.VALID_DIVER_TYPES[diver_type](diver_name)
        except KeyError:
            return f"{diver_type} is not allowed in our competition."

        try:
            next(filter(lambda d: d.name == diver_name, self.divers))
            return f"{diver_name} is already a participant."
        except StopIteration:
            self.divers.append(diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        try:
            fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        except KeyError:
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            next(filter(lambda f: f.name == fish_name, self.fish_list))
            return f"{fish_name} is already permitted."
        except StopIteration:
            self.fish_list.append(fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            message = f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                message = f"{diver_name} hits a {fish.points}pt. {fish_name}."
            elif not is_lucky:
                diver.miss(fish.time_to_catch)
                message = f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            message = f"{diver_name} hits a {fish.points}pt. {fish_name}."

        if diver.oxygen_level <= 0:
            diver.update_health_status()

        return message

    def health_recovery(self):
        divers_with_health_issues = list(filter(lambda d: d.has_health_issue, self.divers))

        for diver in divers_with_health_issues:
            diver.has_health_issue = False
            diver.renew_oxy()

        return f"Divers recovered: {len(divers_with_health_issues)}"

    def diver_catch_report(self, diver_name: str):
        diver = next(filter(lambda d: d.name == diver_name, self.divers))

        text = f"**{diver_name} Catch Report**"

        for fish in diver.catch:
            text += f"\n{fish.fish_details()}"

        return text

    def competition_statistics(self):
        healthy_divers = list(filter(lambda d: not d.has_health_issue, self.divers))

        sorted_divers = sorted(
            healthy_divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name)
        )

        text = f"**Nautical Catch Challenge Statistics**"

        for diver in sorted_divers:
            text += f"\n{str(diver)}"

        return text
