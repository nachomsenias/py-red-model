import matplotlib.pyplot as plt
import numpy as np


def compute_global_utility(sample_value, theta_value, effort_value):
    # Coeficientes Cobb-Douglas
    utility_wealth_values = pow(sample_value, (1 - theta_value))
    utility_work_payoff = pow(effort_value, theta_value)
    utility_effort_cost = (pow(effort_value, 2) / 2 * a)

    global_utility_value = (utility_wealth_values * utility_work_payoff) - utility_effort_cost
    return global_utility_value


def compute_best_utility(effort_step_values, theta_value, sample_value):
    computed_utility_values = []
    for effort_value in effort_step_values:
        computed_utility_values.append(compute_global_utility(sample_value, theta_value, effort_value))

    return max(computed_utility_values)


##########################
# Este script plotea la curva aplicando tau.
##########################
max_effort = 2
effort_increase = 0.1
effort_steps = np.arange(0, max_effort, effort_increase)

theta = 0.6
a = 1
tau_values = np.arange(0.0, 1, 0.05)

mu = 0
sigma = 1
num_samples = 10
# Valores extraidos de la lognormal
s = np.random.lognormal(mu, sigma, num_samples)

# Calcula utilidad máxima para todos los samples. Se usa para la distribucion
utility_values = []
for s_value in s:
    utility_values.append(compute_best_utility(effort_steps, theta, s_value))

computed_global_utility = sum(utility_values)

# Para cada valor de sample, busca la mejor combinación de tau y effort utilizando la redistribución.
for sample in s:
    sample_values = []
    max_values = []

    for tau in tau_values:
        step_values = []
        for step in effort_steps:
            share_value = (computed_global_utility / num_samples) * tau
            utility_with_share = compute_global_utility(sample, theta, step) * (1 - tau) + share_value
            step_values.append(utility_with_share)

        sample_values.append([step_values, tau])
        local_max = max(step_values)
        max_values.append([local_max, effort_steps[step_values.index(local_max)]])

    # Construye la gráfica
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    for values_step in sample_values:
        plt.plot(effort_steps, values_step[0], label=values_step[1])
    plt.axhline(y=0, color='black', linestyle='-')
    plt.legend(loc="upper right")

    for max_dots in max_values:
        plt.scatter(x=max_dots[1], y=max_dots[0], marker='x')

    plt.title('Effort chart with theta=' + str(theta) + ', a=' + str(a) + ', and sample=' + str(sample))
    plt.savefig('.\\taueffort_' + str(theta) + '_' + str(a) + '_' + str(sample) + '.png')
    plt.close(fig)
