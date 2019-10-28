from pattern import *
from generator import *
import pdb


'''
Checker
'''
sample_checker = Checker(800,100)
sample_checker.draw()
sample_checker.show()

'''
Spectrum
'''

sample_spectrum = Spectrum(256)
sample_spectrum.draw()
sample_spectrum.show()

'''
Circle
'''

sample_circle = Circle(250, 50, (130,70))
sample_circle.draw()
sample_circle.show()

#########################
'''
Generator
'''

sample_ImageGenerator = ImageGenerator('data/exercise_data/', 'data/Labels.json', 8, (265,256,3), True, True, True)
sample_ImageGenerator.show()