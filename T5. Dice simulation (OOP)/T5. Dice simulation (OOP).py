
import random 
import matplotlib.pyplot as plt
import time

# additional exercise - time decorator function
def time_decorator(original_function):
    '''Decorator that calculates the execution time of the original function'''
    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        result = original_function(*args, **kwargs)
        end_time = time.time()
        delta_time = end_time - start_time
        print(f'execution time of {original_function.__name__} is {delta_time}')
        return result
    return wrapper_function


class Dice:
    """Dice face with constant minimum (1) and maximum (6) face values"""
    FACE_MIN = 1
    FACE_MAX = 6
    
    def roll(self):
        """Generates a number from 1 to 6 (1 dice roll)"""
        return random.choice(range(self.FACE_MIN, self.FACE_MAX+1))

class Simulation:
    """Accepts number of dices to be rolled:
    For example 2, which means the max sum will be 12.
    The simulation class should accept number of rolls, for example 50000"""
    
    def __init__(self, dices_per_roll: int, number_of_rolls: int, dice: Dice):
        self.dices_per_roll = dices_per_roll
        self.number_of_rolls = number_of_rolls
        self.dice = dice
    
    def roll_total_sum(self):
        """Calculates total sum of dice face values per roll"""
        total_sum = 0
        for i in range(self.dices_per_roll):
            total_sum += self.dice.roll()
        return total_sum 

    @time_decorator
    def get_data(self):
        """Creates a data dictionary with keys as roll total sum, and values as frequency of the roll total sum"""
        data = dict()
        for i in range(self.number_of_rolls):
            k = self.roll_total_sum()
            if k not in data.keys():
                data[k] = 1
            else:
                data[k] += 1
        return data     

    def get_chart(self):
        """Creates a data chart"""
        data = self.get_data()
        roll_total_sum = list(data.keys())
        number_of_rolls_per_outcome = list(data.values())
        fig = plt.figure(figsize=(10,5))
        plt.bar(roll_total_sum, number_of_rolls_per_outcome, color='blue', width=0.6)
        plt.xlabel('Roll total sum')
        plt.ylabel('Number of rolls per outcome')
        plt.title('Dice outcomes')
        plt.show()


def main():
    dices_per_roll = input('Enter desired number of dices per roll: ') # 2
    try:
        dices_per_roll = int(dices_per_roll)
    except:
        raise Exception(f'Invalid input for number of dices per roll: {dices_per_roll}')
      
    number_of_rolls = input('Enter desired number of rolls: ') # 50000
    try:
        number_of_rolls = int(number_of_rolls)
    except:
        raise Exception(f'Invalid input for number of rolls: {number_of_rolls}')          
    
    return Simulation(dices_per_roll, number_of_rolls, Dice())


if __name__ == '__main__':
    main().get_chart()  

