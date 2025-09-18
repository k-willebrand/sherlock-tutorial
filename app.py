# app.py
import os, time, json
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.linspace(0, 10, 1000)
y = np.sin(x) + 0.1*np.random.randn(len(x))

# pretend "work"
time.sleep(3)

os.makedirs("results", exist_ok=True)
np.save("results/data.npy", y)

plt.figure()
plt.plot(x, y)
plt.title("Quick demo run")
plt.xlabel("x"); plt.ylabel("signal")
plt.savefig("results/figure.png", dpi=150)

# small summary
summary = {"mean": float(np.mean(y)), "std": float(np.std(y))}
with open("results/summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("Done. Results in ./results/")

