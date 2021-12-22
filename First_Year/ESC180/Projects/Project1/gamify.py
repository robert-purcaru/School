from enum import Enum 

class Activities(Enum):
    RUNNING = 1
    TEXTBOOKS = 2
    RESTING = 3

class Star():
    def __init__(self, activity, time_stamp):
        self.activity = activity
        self.time_stamp = time_stamp

class Runner():
    
    
    def __init__(self):
        super().__init__()
        self.health_points = 0
        self.hedons = 0

        self.time_running = 0
        self.continuous_rest = 0
        self.current_time = 0
        
        self.is_tired = False
        self.is_interested = True

        self.stars = []
    
    def star_can_be_taken(self, activity):
        """Determines if a star for a certain activity can be taken at the current moment in time  

        Args:
            activity (string): the activity

        Returns:
            boolean: true if the user is still interested, and the activity matches the activity of a star at the current timestamp
        """        
        runner.check_for_interest()
        if self.is_interested:
            for star in self.stars[::-1]:
                if(star.activity == activity and star.time_stamp == runner.current_time and runner.is_interested):
                    return True
                if star.time_stamp < runner.current_time:
                    return False
        return False
        
    def get_activity(self, string_activity):
        if (string_activity == "textbooks"):
            return Activities.TEXTBOOKS
        if (string_activity == "running"):
            return Activities.RUNNING
        if (string_activity == "resting"):
            return Activities.RESTING
        return None
        
    def perform_activity(self, activity, duration):
        if star_can_be_taken(activity):
            self.hedons += min(30, 3 * duration)

        if (activity == "textbooks"):
            self.carry_textbooks(duration)
        if (activity == "running"):
            self.run(duration)
        if (activity == "resting"):
            self.rest(duration)

        self.check_for_interest()
        self.current_time += duration

        return

    def check_for_interest(self):
        length = len(self.stars)
        if length < 3:
            return
        for i in range(2, length):
            if(self.stars[i].time_stamp - 120 <= self.stars[i - 2].time_stamp):
                self.is_interested = False
        return

    def run(self, duration):
        self.health_points += self.time_based_points(duration, 3, 180, 1, self.time_running)

        self.time_running += duration

        if self.is_tired:
            self.hedons += self.time_based_points(duration, -2)
        else:
            self.hedons += self.time_based_points(duration, 2, 10, -2)

        self.is_tired = True
        self.continuous_rest = 0
        
        return

    def carry_textbooks(self, duration):
        self.health_points += self.time_based_points(duration, 2)

        if self.is_tired:
            self.hedons += self.time_based_points(duration, -2)
        else:
            self.hedons += self.time_based_points(duration, 1, 20, -1)
            
        self.time_since_finish_moving = 0
        self.time_running = 0   #piazza question @187, please don't hurt us
        self.is_tired = True
        self.continuous_rest = 0
        
        return

    def rest(self, duration):
        self.time_running = 0
        self.continuous_rest += duration
        
        if(self.continuous_rest >= 120):
            self.is_tired = False

        return
    
    def most_fun_activity_minute(self):
        rest_hedons, running_hedons, textbook_hedons = 0, 0, 0
        
        if (self.is_tired):
            running_hedons -= 2
            textbook_hedons -= 2
            rest_hedons -= 0
        else:
            running_hedons += 2
            textbook_hedons += 1
            rest_hedons += 0
        
        if(self.star_can_be_taken("textbooks")): textbook_hedons += 3
        if(self.star_can_be_taken("running")): running_hedons += 3
        if(self.star_can_be_taken("resting")): rest_hedons += 3

        if(running_hedons > textbook_hedons and running_hedons > rest_hedons): return "running"
        if(textbook_hedons > rest_hedons): return "textbooks"
        return "resting"

    #works
    def time_based_points(self, duration, before_points, thresh = -1, after_points = 0, offset = 0):
        if thresh == -1: after_points = before_points
        thresh = max(thresh - offset, 0)
        delta = duration - thresh
        return before_points*(thresh + min(delta, 0)) + after_points*max(delta, 0)

################################################

def get_cur_hedons():
    global runner
    return runner.hedons

def get_cur_health():
    global runner
    return runner.health_points

def offer_star(activity):
    global runner
    runner.stars.append(Star(activity, runner.current_time))
    runner.check_for_interest()
    return

def perform_activity(activity, duration):
    global runner
    runner.perform_activity(activity, duration)
    
def star_can_be_taken(activity):
    global runner
    return runner.star_can_be_taken(activity)


def most_fun_activity_minute():
    global runner
    return runner.most_fun_activity_minute()

def initialize():
    """Initialize global variables
    """
    global runner
    runner = Runner()
    return

########################################################################
    
if __name__ == "__main__":
    
    initialize()