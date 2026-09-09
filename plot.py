import matplotlib.pyplot as plt
import numpy as np

# Data matrix (Rows = Threads: 1, 2, 4, 8, 16, 32; Columns = MB: 1, 2, 4, 8, 16, 32)
data = np.array([
    [0.915439,  1.82753,   3.63775,   7.29031,  14.5707,   29.1676  ],
    [0.459391,  0.917048,  1.83063,   3.64831,   7.3049,   14.6222  ],
    [0.230885,  0.461432,  0.922046,  1.84075,   3.66834,   7.34489  ],
    [0.116822,  0.233468,  0.46747,   0.931052,  1.86304,   3.70571  ],
    [0.0600776, 0.11931,   0.237568,  0.474207,  0.948314,  1.8915   ],
    [0.0345714, 0.0679161, 0.133794,  0.265883,  0.530775,  1.056    ]
])

threads = [1, 2, 4, 8, 16, 32]
megabytes = [1, 2, 4, 8, 16, 32]

plt.figure(figsize=(9, 5.5))

# Loop through each thread count and plot on the same figure
for i, t in enumerate(threads):
    plt.plot(megabytes, data[i], marker='o', linewidth=2, label=f'{t} Thread(s)')

plt.xlabel('Megabytes (MB)')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time vs. Memory Size across Thread Counts')

# Set log base-2 scaling for x-axis to evenly space powers of 2
plt.xscale('log', base=2)
plt.xticks(megabytes, labels=[str(m) for m in megabytes])

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
import matplotlib.pyplot as plt
import numpy as np

# Data matrix (Rows = Threads: 1, 2, 4, 8, 16, 32; Columns = MB: 1, 2, 4, 8, 16, 32)
data = np.array([
    [0.915439,  1.82753,   3.63775,   7.29031,  14.5707,   29.1676  ],
    [0.459391,  0.917048,  1.83063,   3.64831,   7.3049,   14.6222  ],
    [0.230885,  0.461432,  0.922046,  1.84075,   3.66834,   7.34489  ],
    [0.116822,  0.233468,  0.46747,   0.931052,  1.86304,   3.70571  ],
    [0.0600776, 0.11931,   0.237568,  0.474207,  0.948314,  1.8915   ],
    [0.0345714, 0.0679161, 0.133794,  0.265883,  0.530775,  1.056    ]
])

threads = [1, 2, 4, 8, 16, 32]
megabytes = [1, 2, 4, 8, 16, 32]

plt.figure(figsize=(9, 5.5))

# Loop through each thread count and plot on the same figure
for i, t in enumerate(threads):
    plt.plot(megabytes, data[i], marker='o', linewidth=2, label=f'{t} Thread(s)')

plt.xlabel('Megabytes (MB)')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time vs. Memory Size across Thread Counts')

# Set log base-2 scaling for x-axis to evenly space powers of 2
plt.xscale('log', base=2)
plt.xticks(megabytes, labels=[str(m) for m in megabytes])

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("plot.png", dpi=300, bbox_inches='tight')