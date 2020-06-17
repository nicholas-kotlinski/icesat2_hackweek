def shortname():
    names = ['ATL03', 'ATL06', 'ATL07']
    shortname_widget = wg.Dropdown(
        options=names,
        value=names[0],
        description='Short Name:'
    )

    return shortname_widget

def on_value_change(change):
    dc = change.new
    shortname.options = names

short_name = domain.observe(on_value_change, 'value')