from sklearn.svm import SVC
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
import numpy as np

# Create sample data for visualization
X, y = make_classification(
    n_features=2,        # Total number of features
    n_informative=2,     # Number of informative features
    n_redundant=0,       # Number of redundant features
    n_repeated=0,        # Number of repeated features
    n_classes=3,         # Number of classes
    n_clusters_per_class=1,
    n_samples=100,
    random_state=42
)

# Train the SVM model with a linear kernel and One-vs-Rest approach
svm = SVC(kernel='linear', decision_function_shape='ovr').fit(X, y)

# Plot decision boundaries
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# Create a grid to evaluate model
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = svm.decision_function(xy)

# Plot each decision boundary for the One-vs-Rest classifier
for i in range(Z.shape[1]):
    plt.contour(XX, YY, Z[:, i].reshape(XX.shape), levels=[0], linestyles=['--'], colors='k')

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("SVM Decision Boundary for Multi-Class Traffic Classification")
plt.show()
