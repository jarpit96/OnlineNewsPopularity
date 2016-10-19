import matplotlib.pyplot as plt
import numpy as np
import csv

#np.set_printoptions(threshold=np.inf)

# csv_x = np.genfromtxt('../test_data.csv', dtype=None, delimiter=',', names = True, usecols=( i for i in range(1, 56)))

# csv_y = np.genfromtxt('../test_data.csv', dtype=None, delimiter=',', names = True, usecols=(56))
# x = csv['data_channel_category']
# plt.plot(x, csv['shares']/csv['timedelta'])
# plt.ylabel('shares per unit time')
# plt.xlabel('data channel category')
# # my = ['Unknown', 'Lifestyle', 'Entertainment', 'Business', 'Social Media', 'Tech', 'World']
# # plt.xticks(x, my)
# plt.show()

#
# print(csv_x)
# print (csv_y)

with open('normalizedDataWithSharesReducedAttributes.csv', 'r') as f:
  reader = csv.reader(f)
  csv_x = list(reader)


#csv_x = np.delete(csv_x, (0), axis=0)
csv_x =  np.asarray(csv_x)
csv_y = csv_x[:, -1]  #last column (shares)

# print csv_y
#csv_x = np.delete(csv_x, (0), axis=1)
csv_x = np.delete(csv_x, (-1), axis=1) #delete last column from x

csv_x = np.array(csv_x).astype(np.float)
csv_y = np.array(csv_y).astype(np.float).reshape(-1, 1)

#print csv_x
#print csv_y

#m= 39640   #Number of instances
m, n = csv_x.shape  #Number of attributes

theta = np.zeros(shape = (n, 1))


num_iters = 8000
alpha = 0.2

def normalize(X):
    '''
    Normalize the values column-wise

    '''
    mean_r = []
    std_r = []

    X_norm = X

    n_c = X.shape[1]
    for i in range(n_c):
        m = np.mean(X[:, i])
        s = np.std(X[:, i])

        mean_r.append(m)
        std_r.append(s)
        if s==0:
            s=X[0, i]
        if s == 0:
            s = float("inf")

        X_norm[:, i] = (X_norm[:, i] - m) / s

    return X_norm, mean_r, std_r

def compute_cost(X, y, theta):

   # No of Training Samples
    m = y.size


    predictions = X.dot(theta)

    sqErrors = (predictions - y)

    J = (1.0 / (2 * m)) * sqErrors.T.dot(sqErrors)
    # J = (1.0/(2*m))*sqErrors.sum()
    # print J

    return J


def gradient_descent(X, y, theta, alpha, num_iters):
    '''
    Performs gradient descent to learn theta
    by taking num_items gradient steps with learning
    rate alpha
    '''

    m = y.size
    J_history = np.zeros(shape=(num_iters, 1))

    for i in range(num_iters):
        # print X.shape
        # print theta.shape
        predictions = X.dot(theta)

        theta_size = theta.size

        for it in range(theta_size):

            temp = X[:, it]
            temp.shape = (m, 1)

            errors_x1 = (predictions - y) * temp

            theta[it][0] = theta[it][0] - alpha * (1.0 / m) * errors_x1.sum()

        J_history[i, 0] = compute_cost(X, y, theta)
        print i, J_history[i, 0]
        if(i > 0):
            print i, J_history[i, 0] - J_history[i-1, 0]
    return theta, J_history

#normalize(csv_x)
theta, J_history = gradient_descent(csv_x, csv_y, theta, alpha, num_iters)
print theta
# print J_history
plt.plot(J_history)
plt.show()