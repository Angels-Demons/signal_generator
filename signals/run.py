import datetime

from background_task import background


@background(schedule=5)
def run(counter=0):
    print(str(counter) + " :Running get_all_credits at: " + str(datetime.datetime.now()))
    run(counter + 1)
