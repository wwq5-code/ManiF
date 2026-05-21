

import numpy as np
import matplotlib.pyplot as plt

epsilon = 3
beta = 1 / epsilon


x=[1, 2, 3, 4, 5, 6]
# validation_for_plt =[97,95.8600, 94.9400, 93.5400, 93.2400]
# attack_for_plt=[0, 0.3524, 0, 0.1762, 0.1762]
# basic_for_plt=[99.8, 99.8, 99.8, 99.8, 99.8]

labels = ['200', '400', '600', '800', '1000', '1200']
# unl_org = [97.77, 97.55, 97.35, 97.29, 97.21, 97.21]




unl_ss_w = [94.78, 94.81, 94.33, 94.76, 93.39, 93.39]
unl_ss_wo = [93.15, 94.78, 94.89, 94.46, 93.0, 93.0]

org_acc = [49.39, 49.39, 49.39, 49.39, 49.39 , 49.39]

salun_acc = [55.00, 57.5,  58.1, 59.11, 59.500, 59.7]


unl_salun_runs = np.array([
    [54.36, 53.99,  54.74, 54.83, 53.83, 53.83],   # run 1
    [53.09, 55.85,  55.23, 54.70, 53.13, 53.13],   # run 2
    [55.00, 57.5,  58.1, 59.11, 59.500, 59.7],   # run 3
    [54.00, 53.63, 55.2, 54.80, 53.25, 53.25],    # run 4
    [55.17, 54.51, 54.33, 54.31, 53.49, 53.49],    # run 5
])
unl_salun_mean = np.mean(unl_salun_runs, axis=0)
unl_salun_std  = np.std(unl_salun_runs, axis=0, ddof=1)  # ddof=1 -> 除以 (n-1)



vbu_ldp_acc = [57.00, 58.81, 59.02, 59.90, 61.08, 62.03]




# 94.89, 95.51, 94.78, 93.68, 94.39
unl_ManiF_runs = np.array([
    [58.74, 64.89, 64.61, 65.63, 63.95, 63.95],   # run 1
    [51.99, 65.51, 66.03, 65.84, 62.45, 63.95],  # run 2
    [61.50, 61.00, 62.28, 61.2399, 63.094, 67.74],  # run 3
    [57.55, 63.68, 65.17, 64.60, 63.36, 63.95],  # run 4
    [69.52, 64.39, 64.83, 64.31, 64.11, 63.95],  # run 5
])

unl_ManiF_mean = np.mean(unl_ManiF_runs, axis=0)
unl_ManiF_std  = np.std(unl_ManiF_runs, axis=0, ddof=1)



plt.style.use('seaborn')
plt.figure(figsize=(5.5, 5.3))
l_w=5
m_s=15
marker_s = 3
markevery=1


plt.plot(x, org_acc, linestyle='--', color='#9BC985',  marker='s', fillstyle='full', markevery=markevery,
         label='Origin',linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)




plt.plot(x, unl_ManiF_mean, linestyle='-', color='#797BB7', marker='o', fillstyle='full', markevery=markevery,
         label='ManiF-SMC', linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)


plt.fill_between(
    x,
    unl_ManiF_mean - unl_ManiF_std,
    unl_ManiF_mean + unl_ManiF_std,
    color='#797BB7',
    alpha=0.2,
)

plt.plot(x, unl_salun_mean, linestyle='-.', color='#B595BF',  marker='d', fillstyle='full', markevery=markevery, label='SalUn',linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)

plt.fill_between(
    x,
    unl_salun_mean - unl_salun_std,
    unl_salun_mean + unl_salun_std,
    color='b',
    alpha=0.2,
)

plt.plot(x, vbu_ldp_acc, linestyle='-.', color='#E1C855',  marker='^', fillstyle='full', markevery=markevery,
         label='VBU',linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)


# plt.grid()
leg = plt.legend(fancybox=True, shadow=True)
# plt.xlabel('Malicious Client Ratio (%)' ,fontsize=16)
plt.ylabel('MIA (%)' ,fontsize=24)
my_y_ticks = np.arange(50., 71, 4)
plt.yticks(my_y_ticks,fontsize=20)
plt.xlabel('$\it USS$' ,fontsize=20)

plt.xticks(x, labels, fontsize=20)
plt.title('On MNIST',fontsize=24)

# plt.annotate(r"1e0", xy=(0.1, 1.01), xycoords='axes fraction', xytext=(-10, 10), textcoords='offset points', ha='right', va='center', fontsize=15)


# plt.title('(c) Utility Preservation', fontsize=24)
plt.legend(loc='best',          # same manual position
           fontsize=20,               # same font size
           ncol=2,
           columnspacing=1.,         # distance between the two columns
           handletextpad=0.8)         # gap between symbol and text



plt.tight_layout()
#plt.title("MNIST")
plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('MNIST_model_MIA_uss_new_fill.pdf', format='pdf', dpi=200)
plt.show()