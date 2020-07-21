widget_weight = 75
gizmo_weight = 112
widgets_bought = int(input('How many widgets you want to buy?: '))
gizmos_bought = int(input('How many gizmos you want to buy?: '))
total_weight = (widget_weight*widgets_bought) + (gizmo_weight*gizmos_bought)
print(f'The total weight of your purchase is {total_weight} grams')
