import matplotlib.pyplot as plt
import numpy as np

##########################
## Este script plotea distintos samples de la distribución para mostrar la curva de esfuerzo
##########################
max_effort = 2
effort_increase = 0.1
effort_steps = np.arange(0, max_effort, effort_increase)

theta = 0.6
a = 1
tau = 0.5

mu = 0
sigma = 1
s = np.random.lognormal(mu, sigma, 20)

sample_values = []
max_values = []

# double value = (iota * (wealth * (1 - theta) + (eValue * theta))) * (1 - tau)
#          - (Math.pow(eValue, 2) / (2 * a));
# Como se calcula el esfuerzo en el modelo: pruebo a quitar tau.
for sample in s:
    step_values = []
    for step in effort_steps:
        # Coeficientes originales
        # wealth_values = (sample * (1 - theta))
        # work_payoff = (step * theta)
        # Coeficientes Cobb-Douglas
        wealth_values = pow(sample, (1 - theta))
        work_payoff = pow(step, theta)
        effort_cost = (pow(step, 2) / 2 * a)
        # Version anterior: se suman todos los factores.
        # this_values = wealth_values + work_payoff - effort_cost
        # Version donde se multiplica wealth_values por work_payoff
        # this_values = wealth_values * work_payoff - effort_cost
        # Version con coeficientes Cobb-Douglas
        # this_values = wealth_values * work_payoff - effort_cost
        # Version con coeficientes Cobb-Douglas y tau
        this_values = (wealth_values * work_payoff) * (1 - tau) - effort_cost
        step_values.append(this_values)
    sample_values.append(step_values)
    local_max = max(step_values)
    max_values.append([local_max, effort_steps[step_values.index(local_max)]])

fig, ax = plt.subplots()
fig.set_size_inches(10, 6)
for values_step in sample_values:
    plt.plot(effort_steps, values_step)
plt.axhline(y=0, color='black', linestyle='-')

for max_dots in max_values:
    plt.scatter(x=max_dots[1], y=max_dots[0], marker='x')

plt.title('Effort chart with theta=' + str(theta) + ', a=' + str(a) + ', and tau=' + str(tau))
plt.savefig('.\\' + str(theta) + '_' + str(a) + '_' + str(tau) + '.png')
plt.close(fig)
