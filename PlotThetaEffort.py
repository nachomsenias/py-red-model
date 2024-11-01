import matplotlib.pyplot as plt
import numpy as np

##########################
## Este script plotea la curva aplicando tau. Se fija el número de muestras en uno.
##########################
max_effort = 1
effort_increase = 0.01
effort_steps = np.arange(0, max_effort, effort_increase)

# theta = 0.6
# a = 1
a_values = np.arange(1, 3, 1)
tau = 0.5

mu = 0
sigma = 1
num_samples = 1
s = np.random.lognormal(mu, sigma, num_samples)
theta_values = np.arange(0.1, 1, 0.1)

# double value = (iota * (wealth * (1 - theta) + (eValue * theta))) * (1 - tau)
#          - (Math.pow(eValue, 2) / (2 * a));
# Como se calcula el esfuerzo en el modelo: pruebo a quitar tau.
sample = s[0]
for a in a_values:
    sample_values = []
    max_values = []
    for theta in theta_values:
        step_values = []
        for step in effort_steps:
            # Coeficientes originales
            # wealth_values = (sample * (1 - theta))
            # work_payoff = (step * theta)
            # Coeficientes Cobb-Douglas
            wealth_values = pow(sample, theta)
            work_payoff = pow(step, (1 - theta))

            # wealth_values = pow(sample, 1 - theta)
            # work_payoff = pow(step, theta)
            effort_cost = (pow(step, 2) / 2 * a)

            this_values = (wealth_values * work_payoff) * (1 - tau) - effort_cost
            step_values.append(this_values)

        sample_values.append([step_values, theta])
        local_max = max(step_values)
        max_values.append([local_max, effort_steps[step_values.index(local_max)]])

    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    for values_step in sample_values:
        plt.plot(effort_steps, values_step[0], label=values_step[1])
    plt.axhline(y=0, color='black', linestyle='-')
    plt.legend(loc="upper right")

    for max_dots in max_values:
        plt.scatter(x=max_dots[1], y=max_dots[0], marker='x')

    plt.title('Effort chart with tau=' + str(tau) + ', a=' + str(a) + ', and sample=' + str(sample))
    plt.savefig('.\\theta_effort\\' + str(tau) + '_' + str(a) + '_' + str(sample) + '.png')
    plt.close(fig)
    plt.clf()
