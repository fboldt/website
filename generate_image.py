from operator import le
import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def california_housing(filename):
    housing = pd.read_csv("datasets/" + filename)
    print(len(housing))

    california_img=mpimg.imread("static/california.png")
    ax = housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1, figsize=(10,7))
    plt.imshow(california_img, extent=[-124.55, -113.80, 32.45, 42.05], alpha=0.5, cmap=plt.get_cmap("jet"))
    plt.savefig("static/california_housing.png", format="png")
    # plt.ylabel("Latitude", fontsize=14)
    # plt.xlabel("Longitude", fontsize=14)

    # plt.show()
