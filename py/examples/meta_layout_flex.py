# Meta / Layout / Flex
#
# Allows building responsive layouts.
#
# Specify layout prop as flex and use card's box prop as a min width setter. Card's box prop
# now takes valid percentage value in range [0,1]. Please note that box will have no effect
# when card's content is longer that width specified.
#
# When no value is specified for box prop, card takes whole row.
# ---
from h2o_wave import site, ui

page = site['/demo']

page['meta'] = ui.meta_card(box='', layout='flex')

page['example1'] = ui.markdown_card(
    box='1 1',
    title='',
    content='<a href="/demo" target="_blank">Open this page in a new window</a> to view its title. 1',
)
page['example2'] = ui.markdown_card(
    box='1 2',
    title='',
    content='<a href="/demo" target="_blank">Open this page in a new window</a> to view its title. 2',
)
page['example3'] = ui.markdown_card(
    box='2 2',
    title='',
    content='<a href="/demo" target="_blank">Open this page in a new window</a> to view its title. 3',
)
page['example4'] = ui.markdown_card(
    box='1 3',
    title='',
    content='<a href="/demo" target="_blank">Open this page in a new window</a> to view its title. 4',
)
page['example5'] = ui.markdown_card(
    box='2 3',
    title='',
    content='<a href="/demo" target="_blank">Open this page in a new window</a> to view its title. 5',
)
page['example6'] = ui.markdown_card(
    box='3 3',
    title='',
    content='<a href="/demo" target="_blank">Open this page in a new window</a> to view its title. 6',
)
page['example7'] = ui.markdown_card(
    box='1 4',
    title='',
    content='<a href="/demo" target="_blank">Open this page in a new window</a> to view its title. 7',
)
page['example8'] = ui.markdown_card(
    box='2 4',
    title='',
    content='<a href="/demo" target="_blank">Open this page in a new window</a> to view its title. 8',
)
page['example9'] = ui.markdown_card(
    box='3 4',
    title='',
    content='<a href="/demo" target="_blank">Open this page in a new window</a> to view its title. 9',
)
page['zexample10'] = ui.markdown_card(
    box='4 4',
    title='',
    content='<a href="/demo" target="_blank">Open this page in a new window</a> to view its title. 10',
)
page['zexample11'] = ui.markdown_card(
    box='1 5 200px',
    title='',
    content='<a href="/demo" target="_blank">Open this page in a new window</a> to view its title. 11',
)
page['zexample12'] = ui.markdown_card(
    box='2 5',
    title='',
    content='<a href="/demo" target="_blank">Open this page in a new window</a> to view its title. 12',
)

page.save()