import tensorflow as tf
import re
import numpy as np

tf.set_random_seed(777)  # for reproducibility

f_csv = open("C:/Users/Slayer/Desktop/축구분석/soccer.csv", 'r', newline='')

x_data = []
y_data = []

un_learning_x_data = []
un_learning_y_data = []

stack = 1
input_list = []

for i in range(0,17):
    add = input("원하는 경기의 데이터를 입력해주세요 (18개)")
    input_list.append(add)
def result_def(data):
    if data == 0:
        result = [0, 0, 1]

    elif data == 1:
        result = [0, 1, 0]

    elif data == 2:
        result = [1, 0, 0]

    return  result

def decode_result_def(list):
    if list == [1,0,0]:
        result = 2
    elif list == [0,1,0]:
        result = 1
    elif list == [0,0,1]:
        result = 0

    return result
while True:
        line = f_csv.readline()
        if not line: break

        if stack == 10:
            stack = 1
            # 승,무,패 변수를 y_data에 맞게 변경
            result = line.split(',')[0]
            result = int(result)
            result = result_def(result)
            un_learning_y_data.append(result)

            # 나머지 변수값을 x_data에 저장
            add_list = []
            for i in range(1, 18):
                add = line.split(',')[i]
                add = re.sub('\r\n', '', add)
                add = float(add)
                add_list.append(add)
            un_learning_x_data.append(add_list)

        else:
            # 승,무,패 변수를 y_data에 맞게 변경
            result = line.split(',')[0]
            result = int(result)
            result = result_def(result)
            y_data.append(result)

            # 나머지 변수값을 x_data에 저장
            add_list = []
            for i in range (1,18):
                add = line.split(',')[i]
                add = re.sub('\r\n','',add)
                add = float(add)
                add_list.append(add)
            x_data.append(add_list)
            stack = stack + 1

X = tf.placeholder("float", [None, 17])
Y = tf.placeholder("float", [None, 3])
nb_classes = 3
x_data = np.array(x_data)
X_MinMax = (x_data - x_data.min(axis=0)) / (x_data.max(axis=0) - x_data.min(axis=0))

x_data = np.array(un_learning_x_data)
un_learning_x_data = (x_data - x_data.min(axis=0)) / (x_data.max(axis=0) - x_data.min(axis=0))

W = tf.Variable(tf.random_normal([17, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

# tf.nn.softmax computes softmax activations
# softmax = exp(logits) / reduce_sum(exp(logits), dim)
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

# Cross entropy cost/loss
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

result_y = 0
right = 0

# Launch graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        sess.run(optimizer, feed_dict={X: X_MinMax, Y: y_data})
        if step % 500 == 0:
            print(step, sess.run(cost, feed_dict={X: X_MinMax, Y: y_data}))


    for i in range(0,552):
        a = sess.run(hypothesis, feed_dict={X: [un_learning_x_data[i]]})
        result_y = decode_result_def(un_learning_y_data[i])

        if (sess.run(tf.argmax(a, 1)) == result_y):
            right = right + 1
        else:
            pass
    a = sess.run(hypothesis, feed_dict={X: [input_list]})
    result_user = sess.run(tf.argmax(a, 1))
# print("정확도 : ", right/552)
print("사용자 결과 : ", result_user)