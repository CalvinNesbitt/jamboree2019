import matplotlib.pyplot as plt

def plot_one_trajectory(traj):
    """ plots one trajectory which is a dictionary"""
    plt.plot(traj['lon'],traj['lat'])



