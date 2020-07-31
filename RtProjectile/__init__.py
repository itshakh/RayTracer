from RtTupple import RtVector, RtPoint
import matplotlib.pyplot as plt

class RtProjectile:

    def __init__(self, position=RtPoint(0, 0, 0), velocity=RtVector(0, 0, 0)):
        """

        :param position: [m]
        :param velocity: [m/s]

        """

        self.position = position
        self.velocity = velocity


class RtEnvironment:

    def __init__(self, gravity=RtVector(0, 0, -9.8), wind=RtVector(0, 0, 0)):
        """

        :param gravity: 9.8 [m/s^2]
        :param wind: [m/s]
        """
        self.gravity = gravity
        self.wind = wind


def tick(env, proj):

    # all accelerations are assumed to be multiplied by 1 [s]
    velocity = env.gravity + proj.velocity + env.wind
    position = proj.position + proj.velocity

    return RtProjectile(position, velocity)


if __name__ == '__main__':

    env = RtEnvironment(RtVector(0, -0.01, 0), RtVector(-0.001, 0, 0))

    number_of_second = 3000
    projections = [RtProjectile(RtPoint(0, 1, 0), RtVector(1, 1, 0).normalize())]

    x_ = []
    y_ = []

    for k in range(number_of_second):

        print("proj velocity: " + str(projections[k].velocity) + " proj position: " + str(projections[k].position))

        if projections[k].position.y <= 0:
            break

        projections.append(tick(env, projections[k]))

        x_.append(projections[k].position.x)
        y_.append(projections[k].position.y)

    plt.plot(y_, "x")
    plt.plot(x_, "x")
    plt.show()
