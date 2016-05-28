class ScienceExperiment(object):
    def __init__(self):
        self.bouciness = 0.6
        self.init_height = input('Enter the height the ball will be dropped from(meters): ')
        self.number_of_times_of_bounce = input('Enter how many times you will let the ball bounce: ')
        self.distance_traveled = self.init_height

    def drop(self):
        for i in xrange(self.number_of_times_of_bounce):
            self.bouciness **= i+1
            self.distance_traveled += self.init_height*self.bouciness*2
        print 'Your ball traveled %d meters' % self.distance_traveled

if __name__ == '__main__':
    se = ScienceExperiment()
    se.drop()

#DONE
