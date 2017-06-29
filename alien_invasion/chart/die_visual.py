from die import Diee
import pygal

die = Diee(6)
die2 = Diee(10)

results = []

for roll_num in range(5000):
    result = die.roll() + die2.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(2, die.num_sides + die2.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# 对结构进行可视化
hist = pygal.Bar()

hist.title = 'This is title'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "x's title"
hist.y_title = "y's title"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')
