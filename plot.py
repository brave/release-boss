import numpy as np
import matplotlib.pyplot as plt
from brave import config, util


def plot_prs_per_release(versions, master, uplifts):
    master.sort(key=util.sort_branch_count_pairs)
    uplifts.sort(key=util.sort_branch_count_pairs)

    N = len(versions)
    masterValues = [x[1] for x in master]
    upliftValues = [x[1] for x in uplifts]

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35        # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, masterValues, width)
    p2 = plt.bar(ind, upliftValues, width, bottom=masterValues)

    plt.ylabel('# of pull requests')
    plt.title('Pull Requests by Release')
    plt.xticks(ind, versions)
    plt.yticks(np.arange(0, 250, 10))
    plt.legend((p1[0], p2[0]), ('From master', 'Uplifted'))

    plt.show()


def main():
    version_to_brave_core_milestone_ids = config.version_to_brave_core_milestone_ids.copy()
    del version_to_brave_core_milestone_ids['1.6.x']
    versions = list(version_to_brave_core_milestone_ids.keys())

    master = [('1.7.x', 158), ('1.3.x', 140), ('1.10.x', 139), ('1.1.x', 139),
              ('1.8.x', 121), ('1.2.x', 79), ('1.9.x', 77), ('1.5.x', 75), ('1.4.x', 66)]
    uplifts = [('1.5.x', 99), ('1.7.x', 61), ('1.3.x', 56), ('1.4.x', 51),
               ('1.9.x', 50), ('1.8.x', 47), ('1.2.x', 38), ('1.1.x', 21), ('1.10.x', 15)]
    print('master sum: ', sum([int(x[1]) for x in master]))
    print('uplifts sum: ', sum([int(x[1]) for x in uplifts]))
    plot_prs_per_release(versions, master, uplifts)


if __name__ == '__main__':
    main()
