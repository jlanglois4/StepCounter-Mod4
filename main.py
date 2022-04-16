from steps import Steps

steps_object = Steps()
while not steps_object.stop:
    steps_object.set_steps(int(input("Number of steps (-1 when done): ")))
print(sum(steps_object.steps))
print(steps_object.calculate_avg_steps(int(input("Number of days: "))))
print(f"The most steps in one day is {steps_object.get_max()} and the least is {steps_object.get_min()}")
