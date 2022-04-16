from days import Days


class Steps:

    def __init__(self):
        self.steps = []
        self.stop = False

    def set_steps(self, steps):
        if not steps == -1:
            self.steps.append(steps)
        else:
            self.stop = True

    def calculate_avg_steps(self, days):
        days = Days(days)
        return f"Average steps: {sum(self.steps) / days.number_of_days}"

    def get_min(self):
        return min(self.steps)

    def get_max(self):
        return max(self.steps)
