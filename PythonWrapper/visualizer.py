
from closeapproach import CloseApproach as ca


if __name__ == '__main__':

	floor = vpython.box(pos=vpython.vector(0,0,0), length=4, height=0.5, width=4, color=vpython.color.blue)

	ball = vpython.sphere(pos=vpython.vector(0,4,0), radius=1, color=vpython.color.red, make_trail=False)

	ball.velocity = vpython.vector(0,-1,0)

	dt = 0.01

	while True:

		vpython.rate(100)

		ball.pos = ball.pos + ball.velocity * dt

		if ball.pos.y < ball.radius:

			ball.velocity.y = abs(ball.velocity.y)

		else:

			ball.velocity.y = ball.velocity.y - 9.8 * dt



		

