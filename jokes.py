"""
Title:  jokes
Desc:   Contains all the great jokes the slack bot has up it's sleeve
Author: Yassin Eltahir
Date:   2017-02-19
"""

import random

def jokes():

    options = ['Did you know that just under half of all data science jokes are below average?',
               'There are 2 kinds of data scientist: 1) Those who can extrapolate from incomplete data.',
               'In data science, 80% of time spent is preparing data, 20% of time is spent complaining about the need to prepare data.',
               'A physicist, a mathematician, and a statistician go hunting. They spot a deer, and take aim. The physicist shoots first and misses 10 meters to the right. The mathematician shoots next and misses 10 meters to the left. The statistician then throws down his gun and proclaims, "we got it!"',
               '''
               What's the difference between data science and a statistics?
               
               Data science is statistics on a Mac"
               '''
               ]
    
    # Select joke at random
    return random.choice(options)
