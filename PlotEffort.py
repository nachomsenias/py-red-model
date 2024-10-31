import matplotlib.pyplot as plt
import numpy as np

##########################
## Este script plotea distintas muestras de la distribución para mostrar la curva de esfuerzo
##########################

max_effort = 3
effort_increase = 0.01
effort_steps = np.arange(0, max_effort, effort_increase)

# output_folder = '.\\'
output_folder = '.\\Belgium\\'
# output_folder = '.\\mu0sigma1\\'
# output_folder = '.\\mu-sigma-gamma\\'

# theta = 0.6
theta_values = np.arange(0.1, 1, 0.1)

a = 1
tau = 0.5

# mu = 0
# sigma = 1
mu = 3.282889354203081
sigma = 0.3317059966157858
# gamma = 0.5
np.random.seed(89354203)
s = np.random.lognormal(mu, sigma, 20)

for theta in theta_values:
    sample_values = []
    max_values = []
    for sample in s:
        step_values = []
        for step in effort_steps:
            # Coeficientes Cobb-Douglas
            # wealth_values = pow(sample, (1 - theta))
            # work_payoff = pow(step, theta)
            wealth_values = pow(sample, theta)
            work_payoff = pow(step, (1 - theta))
            effort_cost = pow(step, 2) / (2 * a)
            # Version con coeficientes Cobb-Douglas y tau
            this_values = (wealth_values * work_payoff) * (1 - tau) - effort_cost
            step_values.append(this_values)
        sample_values.append(step_values)
        local_max = max(step_values)
        max_values.append([local_max, effort_steps[step_values.index(local_max)], sample])

    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    for values_step in sample_values:
        plt.plot(effort_steps, values_step)
    plt.axhline(y=0, color='black', linestyle='-')

    # Muestra los óptimos de las curvas.
    for max_dots in max_values:
        plt.scatter(x=max_dots[1], y=max_dots[0], marker='x')

    # Muestra los valores de payoff de los óptimos.
    # for max_dots in max_values:
    #     plt.scatter(x=max_dots[1], y=pow(max_dots[2], (1 - theta) * max_dots[1]) * pow(max_dots[1], theta + max_dots[2]), marker='*')

    plt.title('Effort chart with theta=' + str(theta) + ', a=' + str(a) + ', and tau=' + str(tau))
    plt.savefig(output_folder + str(theta) + '_' + str(a) + '_' + str(tau) + '.png')
    plt.clf()
