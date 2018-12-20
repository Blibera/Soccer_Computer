import tensorflow as tf
import re
tf.set_random_seed(777)  # for reproducibility

f_csv = open("C:/Users/Slayer/Desktop/축구분석/데이터/소프트맥스.csv", 'r', newline='')

x_data = []
y_data = []

un_learning_x_data = []
un_learning_y_data = []

stack = 1

def result_def(data):
    if data == 0:
        result = [0, 0, 1]

    elif data == 1:
        result = [0, 1, 0]

    elif data == 2:
        result = [1, 0, 0]

    return  result
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
            for i in range(1, 20):
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
            for i in range (1,20):
                add = line.split(',')[i]
                add = re.sub('\r\n','',add)
                add = float(add)
                add_list.append(add)
            x_data.append(add_list)
            stack = stack + 1

X = tf.placeholder("float", [None, 19])
Y = tf.placeholder("float", [None, 3])
nb_classes = 3
print(x_data)
print(y_data)
W = tf.Variable(tf.random_normal([19, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

# tf.nn.softmax computes softmax activations
# softmax = exp(logits) / reduce_sum(exp(logits), dim)
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

# Cross entropy cost/loss
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

# Launch graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(2001):
        sess.run(optimizer, feed_dict={X: x_data, Y: y_data})
        if step % 200 == 0:
            print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}))


    for i in range(0,31):
        a = sess.run(hypothesis, feed_dict={X: [un_learning_x_data[i]]})
        print(a, sess.run(tf.argmax(a, 1)))
        print(un_learning_y_data[i])