# Plot / Area + Line / Smooth
# No description available.
# ---
from synth import FakeTimeSeries
from telesync import site, data, ui

page = site['/demo']

n = 50
f = FakeTimeSeries()
v = page.add('example', ui.plot_card(
    box='1 1 4 5',
    title='Area + Line, smooth',
    data=data('date price', n),
    vis=ui.vis([
        ui.mark(mark='area', x_scale='time', x='=date', y='=price', curve='smooth', y_min=0),
        ui.mark(mark='line', x='=date', y='=price', curve='smooth')
    ])
))
v.data = [(t, x) for t, x, dx in [f.next() for _ in range(n)]]

page.sync()