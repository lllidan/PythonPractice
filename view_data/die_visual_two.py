# -*- coding: utf8 -*-
# -*- coding: utf8 -*-
from die import Die
import pygal

# 创建两个D6骰子
die1 = Die()
die2 = Die()
# 投掷几次骰子， 并将结果存储在一个列表中
results = []

for roll_num in range(60000):
    result =die1.roll() + die2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    freuency = results.count(value)
    frequencies.append(freuency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "投掷60000次两个D6的结果"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist._x_title ="Result"
hist._y_title = "Frequency of Result"

hist.add('D6+D6', frequencies)
hist.render_to_file('die_visual.svg')