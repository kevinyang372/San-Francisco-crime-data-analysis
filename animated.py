import matplotlib.animation as animation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = pd.read_csv('/Users/kevin/desktop/Datas/San_Francisco_Crime_Data/train.csv')

def examine_position(i,previous_list):
    for k in previous_list:
        if np.abs(k[0]-file["X"][i]) < 0.003 and np.abs(k[1]-file["Y"][i]) < 0.003:
            k[2] += 1
            return
    previous_list.append([file["X"][i],file["Y"][i],1])

blurred_list=[]
for i in range(10000):
    examine_position(i,blurred_list)

x = []
y = []
for i in range(len(blurred_list)):
    x.append(blurred_list[i][0])
    y.append(blurred_list[i][1])

def main(x1,y1):
    numframes = 10
    x,y = x1,y1
    fig = plt.figure()
    scat = plt.scatter(x, y, s=0)
    datas = np.zeros(len(x))

    ani = animation.FuncAnimation(fig, update_plot, frames=range(numframes),fargs=(x,y,datas,scat))
    ani.save('Crime_SF.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
    plt.show()

def update_plot(i,x,y,datas,scat):
    data = find_size(i,x,y,datas)
    scat.set_sizes(data)
    print("Completed one sequence")
    for i in datas:
        i = i * 0.8
    return scat,

def find_size(i,x,y,datas):
    length = len(file["X"])
    steps = int(length / 12)
    current_step = i * steps
    for k in range(length - current_step,length - current_step + steps):
        for l in range(0,len(x)):
            if np.abs(x[l]-file["X"][k]) < 0.003 and np.abs(y[l]-file["Y"][k]) < 0.003:
                data[l] += 0.1
                break
    return data

main(x,y)