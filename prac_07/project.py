"""
Name	Start Date	Priority	Cost Estimate	Completion Percentage

"""


class Project:
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def is_complete(self):
        return self.completion_percentage == 100

    def __lt__(self, other):
        return self.priority < other.priority
